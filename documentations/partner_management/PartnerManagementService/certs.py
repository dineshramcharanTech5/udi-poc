import requests
import json
from datetime import datetime
import os
from OpenSSL import crypto
import rsa
import base64
import ast
from cryptography.fernet import Fernet


def decryptData(encrypedData, certFile):
    certKeys = readRawCertificate(certFile)
    print('1 - ',certKeys)
    p12 = crypto.load_pkcs12(certKeys,"123456")
    print('2 - ',p12)
    privateKey = p12.get_privatekey()
    print('3 - ',privateKey)
    pemKey = crypto.dump_privatekey(crypto.FILETYPE_PEM,privateKey, cipher=None, passphrase=None)
    print('4 - ',pemKey)
    byteData = bytes(encrypedData, 'utf-8')
    #byteData =base64.b64decode(encrypedData)
    #fernet = Fernet()
    
    #decodedData = fernet.decrypt(encrypedData).decode()
    decodedData = rsa.decrypt(byteData, pemKey ).decode()
    return decodedData

def readCertificate(certFile):
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, certFile)

    with open(filename, 'r') as file:
        data = file.read()
    return(data)
def readRawCertificate(certFile):
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, certFile)

    with open(filename, 'rb') as file:
        data = file.read()
    return(data)


def uploadPartnerCertificate(urlBase, certFile, orgName, partnerId,partnerDomain, token):

    url = urlBase +  "v1/partnermanager/partners/certificate/upload"

    certData = readCertificate(certFile)


    payload = json.dumps({
    "id": "string",
    "metadata": {},
    "request": {
        "certificateData": certData,
        "organizationName": orgName,
        "partnerDomain": partnerDomain,
        "partnerId": partnerId,
        "partnerType": "Auth_Partner"
    },
    "requesttime":  str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "version": "v1.0"
    })
    headers = {
    'Content-Type': 'application/json',
    'Cookie': 'Authorization=' + token}

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        jsonObj = json.loads(response.text)
        if jsonObj['response'] != None:
            signedCertificateData = jsonObj['response']['signedCertificateData']
            certificateId = jsonObj['response']['certificateId']
            return { "signedCertificateData" : signedCertificateData,"certificateId" : certificateId }
        return jsonObj['errors']

    return(response.text)

def uploadCACertificate(urlBase,certFile,partnerDomain,token):

    url = urlBase +  "v1/partnermanager/partners/certificate/ca/upload"
    certData = readCertificate(certFile)
    payload = json.dumps({
    "id": "string",
    "metadata": {},
    "request": {
        "certificateData": certData ,
        "partnerDomain": partnerDomain
    },
    "requesttime": str(datetime.utcnow().isoformat()[:-3]+'Z'),
    "version": "string"
    })
    headers = {
    'Content-Type': 'application/json',
    'Cookie': 'Authorization=' + token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        jsonObj = json.loads(response.text)
        if jsonObj['response'] != None:
            return(jsonObj['response']['status'])
        return(jsonObj['errors'])    
    print(response.text)
    return(response.text)
