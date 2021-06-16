from authorize import *
from auth import *
from config import *
uin = '9713809251'
token = Authenticate(urlBase,userId,password, appId)
print(token)

resp = sendOtp(urlBase,  mispLicenceKey, partnerId, partnerAPIKey,uin,"auth",token)
print(resp)

resp = createOTPAuthRequest(uin,'111111')
print("create - ",resp)

resp = sendOTPAuthRequest(urlBase, mispLicenceKey,partnerId,partnerAPIKey, resp['response'], resp['signature'],token)
print("send - ",resp)