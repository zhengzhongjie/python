import hello
print(hello.message('c'))
print(hello.message('module' + hello.__file__))

for i in range(3):
	reply = hello.message(str(i))
	print(reply)