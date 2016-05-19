#!\user\bin\python

import requests
import json
import time

data = json.load(open("data.json","rb"))

def pres_chk():
	url="https://slack.com/api/users.getPresence"
	payload={"token":data["token"],"user":data["user"]}
	headers={}
	r=requests.post(url,data=payload,headers=headers)
	response = json.loads(r.text)
	resp = response["presence"]
	return resp
	
