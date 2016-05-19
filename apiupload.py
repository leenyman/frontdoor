import requests, json

data = json.load(open("data.json","rb"))
f = {"file": open("capture.jpg", "rb")}
url = "https://slack.com/api/files.upload"
payload = {"token": data['token'], "filename" : "front door capture", "channels": "#tap_u_tigers", "fileype": "jpg", "pretty" : 1}
r = requests.post(url,params=payload,files = f)
