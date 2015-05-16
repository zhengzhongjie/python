"""
Implement an HTTP web server in Python that knows how to run server-side
CGI scripts coded in Python; serves files and scripts from current working
dit; Python scripts must be stored in webdir\cgi-bin or webdir\htbin;
"""
#!/usr/local/bin/python3
import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port   = 80

os.chdir(webdir)
srvraddr = ("", port)
srvrobj  = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()