
import requests
import json
from datetime import datetime

def selfRegisterMISPPartner(urlBase, partnerId,orgName, token):
    url = urlBase +  "v1/partnermanager/partners"

    payload = json.dumps({
    "id": "string",
    "metadata": {},
    "request": {
        "address": "Some where in India",
        "contactNumber": "9232121217",
        "emailId": "misp_" + partnerId + "@mailinator.com",
        "organizationName": orgName,
        "partnerId": partnerId,
        "partnerType": "MISP_Partner",
        "policyGroup": ""
    },
    "requesttime": str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "version": "v1.0"
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'Authorization=' + token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        jsonObj = json.loads(response.text)
        if jsonObj["errors"] == None:
            jsonResp = jsonObj["response"]
            return(jsonResp)
    return(response.text)
    
    
def generateMISPLicense(urlBase, mispPartnerId, token):


    url = urlBase + "v1/partnermanager/misps"

    payload = json.dumps({
    "id": "string",
    "metadata": {},
    "request": {
        "providerId": mispPartnerId
    },
    "requesttime": str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "version": "v1.0"
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'Authorization=' + token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        jsonObj = json.loads(response.text)
        if jsonObj['response'] != None:
            return jsonObj['response']
    return(response.text)
