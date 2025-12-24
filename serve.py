import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map['.js'] = 'application/javascript'
Handler.extensions_map['.json'] = 'application/json'

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"✓ Server running at http://localhost:{PORT}")
    print(f"✓ Open http://localhost:{PORT}/index.html in your browser")
    print("✓ Press Ctrl+C to stop")
    httpd.serve_forever()
