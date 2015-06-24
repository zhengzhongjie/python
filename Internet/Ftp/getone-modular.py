import getfile
from getpass import getppass
filename = 'monkeys.jpg'

getfile.getfile(file=filename,
				site='ftp.rmi.net',
				dir='.',
				user=('lutz', getpass('Pswd?')),
				refetch=True)

