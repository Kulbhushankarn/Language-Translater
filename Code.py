import http.client
import json
conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")
mymessage=input("Enter Your Text For Translation")
payload = "q="+mymessage+"&target=hi&source=en"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "9bb5d2bd5emsh3ee83c63eb98159p1f27c2jsn8905f37ab9f6",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

conn.request("POST", "/language/translate/v2", payload, headers)

res = conn.getresponse()
data = res.read()

mydata=json.loads(data.decode("utf-8"))
print(mydata['data']['translations'][0]['translatedText'])
