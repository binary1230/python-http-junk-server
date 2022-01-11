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
          <head>
            <title>Backend!</title>
            <style>
              body { background-color: black; color: #77FF77; }
              a { color: yellow; }
              h1 {color: #55FFFF; }
            </style>
          </head>
          <body>
            <h1>Hello from the backend python test page.</h1>
            <p>Incoming URL: <font color=#FFFFFF><b>"""+s.path+"""</b></font></p>
            <p>Current time: """+str(datetime.datetime.now())+"""</p>
            <p>If this is not what you were expecting to see, please contact your sysadmin.</p>
          </body>
        </html>
        """
        s.wfile.write(html.encode())

if __name__ == '__main__':
    httpd = http.server.HTTPServer(('', 8080), MyWebpage)
    httpd.serve_forever()