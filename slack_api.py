import requests, json

data = json.load(open("data.json","rb"))
upload_url = "https://slack.com/api/files.upload"
message_url = "https://slack.com/api/chat.postMessage"
presence_url="https://slack.com/api/users.getPresence"


def upload():
	f = {"file": open("capture.jpg", "rb")}
	payload = {"token": data['token'], "filename" : "front door capture", "channels": "#tap_u_tigers", "fileype": "jpg", "pretty" : 1}
	message = {"token": data['token'], "text": "@channel someone is at the front door", "channel": "#tap_u_tigers", "parse": "full", 	"as_user": "true", "pretty" : 1}
	requests.post(message_url, params=message)
	requests.post(upload_url,params=payload,files = f)
	return

def check():
	payload={"token":data["token"],"user":data["user"]}
	headers={}
	r=requests.post(presence_url,data=payload,headers=headers)
	response = json.loads(r.text)
	resp = response["presence"]
	return resp
