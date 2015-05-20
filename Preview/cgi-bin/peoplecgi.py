"""
Implement a web-based interface for viewing and updating class instances
stored in a shelve; the shelve lives on server (same machine if localhost)
"""

import cgi, shelve, sys, os
shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()
print('Content-type: text/html')
sys.path.insert(0, os.getcwd())

#main html template
replyhtml = """
<html>
<title>People Input Form</title>
<boddy>
<form method=POST action="peoplecgi.py">
	<table>
	<tr><th>key<td><input type=text name=key value="%(key)s">
	$ROWS$
	</table>
	<p>
	%(action)s
	<input type=submit value="Fetch",name=action>
	<input type=submit value="Update", name=action>
</from>
</body></html>
"""

# insert html for data rows at $ROWS$
rowhtml  = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s">'
rowshtml = ''
for fieldname in fieldnames:
	rowshtml += (rowhtml % ((fieldname,) * 3))
replyhtml = replyhtml.replace('$ROWS$', rowshtml)

def htmlize(adict,action):
	new = adict.copy()
	for field in fieldnames:
		value = new[field]
		new[field] = cgi.escape(repr(value))
	new['action'] = action
	return new

def fetchRecord(db, form):
	try:
		key = form['key'].value
		record = db[key]
		fields = record.__dict__
		fields['key'] = key
	except:
		fields = dict.fromkeys(fieldnames, '?')
		fields['key'] = 'Missing or invaliid key!'
	return fields

def updateRecord(db, form):
	if not 'key' in form:
		fields = dict.fromkeys(fieldnames,'?')
		fields['key'] = 'Missing key input!'
	else:
		key = form['key'].value
		if key in db:
			record = db[key]
		else:
			from person import person
			record = Person(name='?', age='?')
		for field in fieldnames:
			setattr(record, field, eval(form[field].value))
		db[key] = record
		fields = record.__dict__
		fields['key'] = key
	return fields

db = shelve.open(shelvename)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
	fields = fetchRecord(db, form)
elif action == 'Update':
	fields = updateRecord(db, form)
else:
	fields = dict.fromkeys(fieldnames, '?')
	fields['key'] = 'Missing or invalid action!'
db.close()
#print(replyhtml)
#print(htmlize(fields))
print(replyhtml % htmlize(fields,action))