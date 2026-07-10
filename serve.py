#!/usr/bin/env python3
"""Optional local dev server for the demo (the pages also open fine via file://)."""
import os, http.server, socketserver

os.chdir("/Users/richardkirk/Documents/GitHub/economist-demo-mockup")
PORT = 8123
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"serving on http://127.0.0.1:{PORT}")
    httpd.serve_forever()
