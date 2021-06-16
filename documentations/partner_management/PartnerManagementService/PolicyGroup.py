import requests
import json
from datetime import datetime
  
#url = "https://qa2.mosip.net/"

def createPolicyGroup(urlBase, name, desc, token):

    url = urlBase + "v1/policymanager/policies/group/new"
    
    payload = json.dumps({
        "id": "string",
        "metadata": {},
        "request": {
        "desc": desc,
        "name": name
    },
    "requesttime": str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "version": "v1.0"
    })
   
    print(payload)
    
    headers = {
    'Content-Type': 'application/json',
    'Cookie': 'Authorization='+ token
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.status_code)
    return(response.text)
