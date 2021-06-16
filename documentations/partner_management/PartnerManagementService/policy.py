import requests
import json
from datetime import datetime

def createPolicyGroup(urlBase,grpName, grpDesc, token):

    url =  urlBase + "v1/policymanager/policies/group/new"

    payload = json.dumps({
    "id": "string",
    "metadata": {},
    "request": {
        "desc": grpDesc,
        "name": grpName
    },
    "requesttime": str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "version": "string"
    })
    headers = {
  'Content-Type': 'application/json',

  'Cookie': 'Authorization=' + token
  
  
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    jsonObj = json.loads(response.text)
    if(response.status_code == 200):
      if jsonObj["response"]:
        id = jsonObj["response"]["id"]
        return(response.text)

    return(-1)

def getPolicyGroupByName(urlBase, groupName, token):


  url = urlBase + "v1/policymanager/policies/group/all"

  
  headers = {
    'Content-Type': 'application/json',
    'Cookie': 'Authorization=' + token
  }

  response = requests.request("GET", url, headers=headers, data=None)

  #print(response.text)
  if(response.status_code == 200):
    jsonObj = json.loads(response.text)
    jsonArr = jsonObj["response"]
    for policyGrp in jsonArr:
      if policyGrp['policyGroup']['name'] == groupName:
        return( policyGrp['policyGroup']['id'])
    
  return(-1)

def definePolicy(urlBase, policyGroup,policyName, token):


  url = urlBase + "v1/policymanager/policies"

  payload = json.dumps({
    "id": "string",
    "metadata": {},
    "request": {
      "desc": "Account Opeing Policy  for Auth & KYC",
      "name": policyName,
      "version": "1.0",
      "policies": {
        "allowedAuthTypes": [
          {
            "authSubType": "IRIS",
            "authType": "bio",
            "mandatory": False
          },
          {
            "authSubType": "FACE",
            "authType": "bio",
            "mandatory": False
          },
          {
            "authSubType": "",
            "authType": "otp",
            "mandatory": False
          },
          {
            "authSubType": "",
            "authType": "otp-request",
            "mandatory": False
          },
          {
            "authSubType": "",
            "authType": "kyc",
            "mandatory": False
          },
          {
            "authSubType": "",
            "authType": "demo",
            "mandatory": False
          }
        ],
        "allowedKycAttributes": [
          {
            "attributeName": "fullName"
          },
          {
            "attributeName": "gender"
          },
          {
            "attributeName": "residenceStatus"
          },
          {
            "attributeName": "dateOfBirth"
          }
        ],
        "authTokenType": "policy"
      },
      "policyGroupName": policyGroup,
      "policyType": "Auth"
    },
    "requesttime": str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "version": "string"
  })
  headers = {
    'Content-Type': 'application/json',
    'Cookie': 'Authorization=' + token
  }

  print(payload)
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.status_code)
  if response.status_code == 200:
    jsonObj = json.loads(response.text)
    if jsonObj['response'] != None:
      jsonResp = jsonObj["response"]  
      return(jsonResp["id"])
    return(jsonObj['errors'])


  return(-1)

def publishPolicy(urlBase,policyId, groupId, token):

  url = urlBase + "v1/policymanager/policies/"+ policyId + "/group/" + groupId +"/publish"

  payload = ""
  headers = {
    'Cookie': 'Authorization='+ token
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  if response.status_code == 200:
    jsonObj = json.loads(response.text)
    jsonResp = jsonObj["response"]
    if jsonObj["response"] != None:
      return(jsonResp["status"])
      
  return("FAILED")

def getPolicyByName(urlBase,  policyName, token):
  
  url = urlBase + "v1/policymanager/policies" 
  payload = ""
  headers = {
    'Cookie': 'Authorization='+ token
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  if response.status_code == 200:
      jsonObj = json.loads(response.text)
      if jsonObj["response"] != None:

        jsonArr = jsonObj["response"]
      for policy in jsonArr:
        if policy['policyName'] == policyName:
          return( policy['policyId'])
   
  return(-1)
   


