import requests
import json
from datetime import datetime

def selfRegister(urlBase, orgName,policyGroup,partnerId, token):
    url = urlBase + "v1/partnermanager/partners"

    payload = json.dumps({
    "id": "string",
    "metadata": {},
    "request": {
        "address": "some where in India",
        "contactNumber": "9232121217",
        "emailId": "auth."+ partnerId +"@mailinator.com",
        "organizationName": orgName,
        "partnerId": partnerId,
        "partnerType": "Auth_Partner",
        "policyGroup": policyGroup
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

def submitPartnerAPIKeyRequest(urlBase,partnerId,policyName,usecaseDes,token):


    url = urlBase + "v1/partnermanager/partners/"+ partnerId +"/apikey/request"

    payload = json.dumps({
    "id": "string",
    "metadata": {},
    "request": {
        "policyName": policyName,
        "useCaseDescription": usecaseDes
    },
    "requesttime": str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "version": "v1.0"
    })
    headers = {
    'Content-Type': 'application/json',
    'Cookie': 'Authorization=' + token
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)
    if response.status_code == 200:
        jsonObj = json.loads(response.text)
        if jsonObj["response"] != None:
            return(jsonObj["response"]["apiRequestId"])
        return(jsonObj["errors"])
     
    
    return(response.text)

#status =>   "Active", "inactive"

def UpdatePartnerStatus(urlBase,partnerId,status,token):

    url = urlBase + "v1/partnermanager/partners/" + partnerId
    strStatus = status
    payload = json.dumps({
    "id": "string",
    "metadata": {},
    "request": {
        "status": status
    },
    "requesttime": str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "version": "v1.0"
    })
    headers = {
    'Content-Type': 'application/json',
    'Cookie': 'Authorization=' + token
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    print(response.text)

def ApprovePartnerAPIKeyRequest(urlBase,apiKeyRequestId,token):


    url = urlBase + "v1/partnermanager/partners/apikey/" + str(apiKeyRequestId)

    payload = json.dumps({
    "id": "string",
    "metadata": {},
    "request": {
        "status": "Approved"
    },
    "requesttime": str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "version": "v1.0"
    })
    headers = {
    'Content-Type': 'application/json',
    'Cookie': 'Authorization=' + token
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)
    if response.status_code == 200:
        jsonObj = json.loads(response.text)
        if jsonObj["response"] != None:
            return(jsonObj["response"])
        
    #print(response.text)
    return(response.text)

def getAllAPIKeyRequests(urlBase, partnerId, token):


    url = urlBase + "v1/partnermanager/partners/" + partnerId + "/apikey/request"

    payload={}
    headers = {
    'Cookie': 'Authorization=' + token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        jsonObj = json.loads(response.text)
        return(jsonObj['response'])
    print(response.text)
