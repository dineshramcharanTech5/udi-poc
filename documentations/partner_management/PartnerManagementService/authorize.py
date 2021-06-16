import requests
import json
from datetime import datetime

#url = "https://qa2.mosip.net/v1/authmanager/authenticate/useridPwd"
def Authenticate(urlBase,userName,passwd, appId):
    url = urlBase + "v1/authmanager/authenticate/useridPwd"

    payload = json.dumps({
    "id": "mosip.authentication.useridPwd",
    "metadata": {},
    "request": {
        "userName": userName,
        "password": passwd,
        "appId": appId
    },
    "requesttime": str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "version": "1.0"
    })
    headers = {
    'Content-Type': 'application/json',
    }
    #cleprint(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    #print(response.text)
    jsonObj = json.loads(response.text)
    if(jsonObj["response"]["status"] =="success"):
 #       print(response.headers)
        #print([x.name + '=' + x.value for x in response.cookies])

        token = response.cookies.get("Authorization")
        #token = response.headers.get("Authorization")
        return(token)
    return( jsonObj["errors"])
