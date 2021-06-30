#!/usr/bin/python3

import time
import requests


mytime = time.time()
myip = requests.get("http://ip.jsontest.com/").json()['ip']
with open("myservers.txt", 'r') as servers:
     myservers = servers.readlines()


mydict01 = {}
mydict01["time"] = mytime
mydict01["ip"] = myip
mydict01["mysrvrs"] = myservers

mydata = {}
mydata["json"] = str(mydict01)

resp = requests.post("http://validate.jsontest.com/", data=mydata)
respjson = resp.json()
print(respjson)


