"""Free CI trial inside a private Linux network namespace, using only synthetic routes."""
import http.client
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.request import urlopen

from policy import INVENTORY, assess, decode


BASE_URL = "https://raw.githubusercontent.com/alphastartix26-ops/scopeledger-local"
CANDIDATES = (
    ("baseline", "a40d737349880407c3b83153a0093f8c03e79108", "allow"),
    ("safe", "6bbbaab8e56408ddcee37ead08e5fa9009cdc215", "allow"),
    ("staff", "7b7e99d6e5db8be5130f75e8cc5d44d4d831d654", "block"),
    ("admin", "4b169253605926cdc4efadfc38af71a917739cc3", "block"),
)
PORTS = {route: 26000 + i for i, route in enumerate(INVENTORY)}


def run(*args, **kwargs):
    return subprocess.run(list(args), check=True, **kwargs)


def check_namespace():
    if os.stat("/proc/self/ns/net").st_ino == os.stat("/proc/1/ns/net").st_ino:
        raise RuntimeError("A separate test network namespace is required")


def admit(candidate):
    check_namespace()
    proposal = decode(Path(candidate).read_bytes())
    verdict = assess(proposal)
    print(json.dumps(verdict), flush=True)
    if verdict["decision"] == "block":
        return 42
    rules = ["*filter", ":INPUT DROP [0:0]", ":FORWARD DROP [0:0]", ":OUTPUT ACCEPT [0:0]",
             "-A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT",
             "-A INPUT -d 127.0.0.2 -p tcp -j ACCEPT"]
    rules.extend(f"-A INPUT -d 127.0.0.1 -p tcp --dport {PORTS[path]} -j ACCEPT"
                 for path in proposal["public_routes"])
    rules.append("COMMIT")
    run("iptables-restore", "--wait", input="\n".join(rules) + "\n", text=True)
    return 0


class Origin(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"staging-origin")

    def log_message(self, fmt, *args):
        pass


def connect(address, port):
    conn = http.client.HTTPConnection(address, port, timeout=1.0)
    try:
        conn.request("GET", "/")
        resp = conn.getresponse()
        if resp.status != 200 or resp.read() != b"staging-origin":
            raise AssertionError("Unexpected origin response")
        return 200
    except socket.timeout:
        return "DROP"
    finally:
        conn.close()


def sample(stage, hours_open):
    data = {path: connect("127.0.0.1", port) for path, port in PORTS.items()}
    internal = {path: connect("127.0.0.2", PORTS[path]) for path in ("/team-notes", "/admin")}
    print(json.dumps({"stage": stage, "public": data, "trusted_test_interface": internal}), flush=True)
    if data != {"/health": 200, "/catalog": 200, "/hours": 200 if hours_open else "DROP",
                "/team-notes": "DROP", "/admin": "DROP"} or set(internal.values()) != {200}:
        raise AssertionError("Firewall behavior differed from the expected policy")


def exercise(folder):
    check_namespace()
    run("ip", "link", "set", "lo", "up")
    servers = []
    try:
        for port in PORTS.values():
            server = ThreadingHTTPServer(("0.0.0.0", port), Origin)
            Thread(target=server.serve_forever, daemon=True).start()
            servers.append(server)
        for name, sha, decision in CANDIDATES:
            proc = subprocess.run([sys.executable, __file__, "admit", str(Path(folder) / name)], check=False)
            if proc.returncode != (0 if decision == "allow" else 42):
                raise AssertionError(f"Unexpected decision on {sha}")
            # The policy evaluator has already exited; only kernel rules can enforce here.
            sample(f"{name}, evaluator exited", name != "baseline")
        run("iptables", "-nvL", "INPUT")
    finally:
        for server in servers:
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        with tempfile.TemporaryDirectory() as tmp:
            for name, sha, _ in CANDIDATES:
                with urlopen(f"{BASE_URL}/{sha}/staging/firewall-policy.json", timeout=15) as response:
                    data = response.read(4097)
                if len(data) > 4096:
                    raise ValueError("Policy too large")
                (Path(tmp) / name).write_bytes(data)
            run("sudo", "--non-interactive", "unshare", "--net", sys.executable, __file__, "exercise", tmp)
    elif sys.argv[1] == "admit":
        sys.exit(admit(sys.argv[2]))
    elif sys.argv[1] == "exercise":
        exercise(sys.argv[2])
