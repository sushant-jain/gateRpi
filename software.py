import urllib.request
import json

def auth(uid):
	string = "http://ediome.com:3001/rfid"
	mystring = ""
        for digit in uid:
            mystring += str(digit)
	string = string + "/add?uid=" + str(mystring)
	print(string)
	content = urllib.request.urlopen(string).read()
	print(uid)
	content = str(content,'utf-8')
	print(uid)
	content = json.loads(content)
	# print(content["success"])
	if(content["success"]):
		status = 1
	else:
		status = 0
	return status
auth(2864538765487356)
