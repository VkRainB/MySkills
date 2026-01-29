#!/usr/bin/env python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def _send(self, payload, code=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length > 0 else b"{}"
        try:
            data = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            data = {"raw": raw.decode("utf-8", errors="ignore")}

        if self.path.endswith("/wechat-upload-image"):
            payload = {
                "success": True,
                "media_id": "TEST_MEDIA_ID",
                "url": "https://example.com/fake.png",
                "received": {
                    "filename": data.get("filename"),
                    "type": data.get("type"),
                },
            }
            self._send(payload)
            return

        if self.path.endswith("/wechat-create-draft"):
            payload = {
                "success": True,
                "draft_id": "TEST_DRAFT_ID",
                "received": {
                    "title": data.get("title"),
                    "author": data.get("author"),
                },
            }
            self._send(payload)
            return

        self._send({"success": False, "error": "unknown webhook"}, code=404)


def main():
    server = HTTPServer(("127.0.0.1", 5679), Handler)
    print("Mock n8n server on http://127.0.0.1:5679")
    server.serve_forever()

if __name__ == "__main__":
    main()
