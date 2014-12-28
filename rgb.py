import requests
import time

while True:
	r = requests.get('http://localhost:8000/overview')
	f = open('rgb','w')
	for line in r.content.splitlines():
		if '<task name' in line:
			f.write(line[26:-7]+'\n') # python will convert \n to os.linesep
	f.close()
	print "."
	time.sleep(5)
