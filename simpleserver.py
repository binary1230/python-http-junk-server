import http.server
import datetime

# a simple HTTPServer that responds to any URL and prints the URL in the string

class MyWebpage(http.server.BaseHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200)
        s.send_header('Content-Type', 'text/html')
        s.end_headers()
        html = """
                <!DOCTYPE html>
                <html>
                    <head><title>Backend!</title></head>
                <body>
                    <h1>Backend demo page!</h1>
                    <p>Incoming URL="""+s.path+"""</p>
                    <p>Current time: """+str(datetime.datetime.now())+"""</p>
                </body>
                </html>
                """
        s.wfile.write(html.encode())

if __name__ == '__main__':
    httpd = http.server.HTTPServer(('', 8080), MyWebpage)
    httpd.serve_forever()