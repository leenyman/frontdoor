import requests, json

data = json.load(open("data.json","rb"))
f = {"file": open("capture.jpg", "rb")}
url = "https://slack.com/api/files.upload"
payload = {"token": data['token'], "filename" : "front door capture", "channels": "#tap_u_tigers", "fileype": "jpg", "pretty" : 1}
message = {"token": data['token'], "text": "@channel someone is at the front door", "channel": "#tap_u_tigers", "parse": "full", "as_user": "true", "pretty" : 1}
resp = requests.post("https://slack.com/api/chat.postMessage",params=message)
r = requests.post(url,params=payload,files = f)