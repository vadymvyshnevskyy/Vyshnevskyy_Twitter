import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

acct = input('Enter Twitter Account:')
number = int(input("Enter number of person:"))
url = twurl.augment(TWITTER_URL,
                    {'screen_name': acct, 'count': number})
print('Retrieving', url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

js = json.loads(data)


lst = []
result = {}
keys = ["id", "name", "location"]
with open("file.json", "w", encoding="utf-8") as f:

    for i in js["users"]:
        diction = {}
        for y in i:
            if y in keys:
                diction1 = {}
                diction1[y] = i[y]
                diction.update(diction1)
        lst.append(diction)
    result["users"] = lst

    js1 = json.dump(result, f, indent=4)