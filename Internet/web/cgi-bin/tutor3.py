import cgi
form = cgi.FieldStorage()
print('Content-type: text/html')

html = """
<TITLE>tutor3.py</TITLE>
<H1>Greetings</H1>
<HR>
<P>%s<P>
<HR>"""

if not 'user' in form:
	print(html % 'Who are you?')
else:
	print(html % ('Hello, %s.' % form['user'].value))