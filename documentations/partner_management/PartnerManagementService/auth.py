import requests
import json
from datetime import datetime
import base64
import rsa

def createOTPAuthRequest(uin,otp):

    url = "http://localhost:8384/v1/identity/createAuthRequest?id=" + uin

    payload = json.dumps({
    "otp": otp,
    "transactionId": "1234567890",
    "timestamp": str(datetime.utcnow().isoformat()[:-3]+'Z'),
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        signature = response.headers.get("signature")
        print("response - ", response.text)
        print("signature - ", signature)
        return { "response": response.text, "signature": signature}
    return(response.text)

def createOTPekycRequest(uin,otp):

    url = "http://localhost:8384/v1/identity/createAuthRequest?id=" + uin +"&isKyc=true"

    payload = json.dumps({
    "otp": otp,
    "transactionId": "1234567890",
    "timestamp": str(datetime.utcnow().isoformat()[:-3]+'Z'),
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        signature = response.headers.get("signature")
        return { "response": response.text, "signature": signature}
    return(response.text)

def sendOTPAuthRequest(urlBase, MISPLicKey, partnerId, partnerAPIKey, reqPayload, signature,token):

    url = urlBase +  "idauthentication/v1/auth/" +MISPLicKey + "/" + partnerId + "/" + partnerAPIKey

    payload = reqPayload
   
    headers = {
    'Content-Type': 'application/json',
    'signature': signature,
    'Authorization': token
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return(response.text)

def sendOTPekycRequest(urlBase, MISPLicKey, partnerId, partnerAPIKey, reqPayload, signature,token):

    url = urlBase +  "idauthentication/v1/kyc/" +MISPLicKey + "/" + partnerId + "/" + partnerAPIKey

    payload = reqPayload
   
    headers = {
    'Content-Type': 'application/json',
    'signature': signature,
    'Authorization': token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        jsonObj = json.loads(response.text)
        identity = jsonObj["response"]["identity"]
        return(identity)
    print(response.text)
    return(response.text)


def sendOtp(urlBase,  MISPLicKey, partnerId, partnerAPIKey,uin,type, token):

    url = urlBase + "idauthentication/v1/otp/"+ MISPLicKey +"/"+ partnerId + "/"+ partnerAPIKey
    id ="mosip.identity.otp"
    #if type =='ekyc':
    #    id = "mosip.identity.kyc"

    payload = json.dumps({
    "id":  id,
    "version": "1.0",
    "requestTime":  str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "transactionID": "1234567890",
    "individualId": uin,
    "individualIdType": "UIN",
    "otpChannel": [
        "EMAIL",
        "PHONE"
    ]
    })
    
    #payloadB64 = base64.b64encode(bytes(payload, 'utf-8'))

    payloadB64 = base64.b64encode(payload.encode()).decode()

    signature = jwtEncode(urlBase, payloadB64,token)

    headers = {
    'Content-Type': 'application/json',
    'signature' : signature,
    'Authorization': token
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        jsonObj = json.loads(response.text)
        if jsonObj['response'] != None:
            return(jsonObj['response'])
    return(response.text)



def jwtEncode(urlBase, dataToSign, token):
    
    url = urlBase + "idauthentication/v1/internal/jwtSign"
    
    payload = json.dumps({
    "id": "string",
    "metadata": {},
    "request": {
        "applicationId": "IDA",
        "certificateUrl": "string",
        "dataToSign": str(dataToSign),
        "includeCertHash": True,
        "includeCertificate": True,
        "includePayload": False,
        "referenceId": "SIGN"
    },
    "requesttime":str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "version": "v1"
        
     })
    
    headers = {
    'Content-Type': 'application/json',
      'Cookie': 'Authorization=' + token
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        jsonObj = json.loads(response.text)
        if jsonObj['response'] != None:
            return(jsonObj['response']['jwtSignedData'])
        
    return(response.text)
