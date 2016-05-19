import requests
import json
import time
import data.json as data

url="https://slack.com/api/users.getPresence"
payload={"token":data.token,"user":data.user}
headers={}
r=requests.post(url,data=payload,headers=headers)

response = json.loads(r.text)

while response["presence"] == "away":
	time.sleep(5)
	print (response["presence"])
	
