from authorize import *
from auth import *
from config import *
from certs import decryptData

uin = '9713809251'
# token = Authenticate(urlBase,userId,password, appId)

# resp = sendOtp(urlBase,  mispLicenceKey, partnerId, partnerAPIKey,uin,"ekyc",token)
# print('otp - ', resp)

# resp = createOTPekycRequest(uin,'111111')
# print('create - ', resp)

# identity = sendOTPekycRequest(urlBase, mispLicenceKey,partnerId,partnerAPIKey, resp['response'], resp['signature'],token)

# print('"' + identity + '"')


identity = "k3lWOGKODdz2S6pm0ESjRS9J7RunMkThK8sloHryTtFJn8l_HCs5ZkT3B63FpQmsOreHgAJupFf7_W1yF80p7l6LA_k30NY_hmiLJSOyyZqtZXxdiMnHvwFAVQtmSmZpFEfsnq2aVqCPcJ-IRj9z5uRxoDwd4HT46oFFZc074ir7Q-xGt7u6n8o6820AGvfjjNzd6SFM2uMw9D2BblcTjSraaxBQFM3Jn1mEXgyOCVZDxzGYsBmrR-muDUqnl_saA99coS764JLSf2Cydps7KmOORgAKIIYTouBAxFaM3Wjv4i4m0Yppp4gyIaPVgjhyd5UjA00z-ujkZ1q6N2WzfyNLRVlfU1BMSVRURVIjO-ucA_v3Pq4IpdFEoQVH9Q6iexsURvwl4ON6iY46b_c7K88Lwj0u07YDtFQOmQXtfk8RC4IlUhFTy9Kt4vRBItx0yWq-OfeSzyHpF4z9Zsp2dGg9-j-Pc7B-YVvzgDB-inBRhwEWay9WeDcwIO5oqG3fWW6Vcz5WR--czlRE9ZmS7LKNy3GQtxQlvJpCcaBmOcC8xj1JzHI2HmT7cSE1MNhTF5_qIj-dvjjtbpVY28iyCrFcvEMECMYxypQNkfOBWtnpobO5fVzf1ePu9iw6A4bDwTQFkqmFcTLUf1ZtmjVG2oPNuq6kIcFt"

decrIdentity = decryptData(identity,"certificates\\XYZBank\\hcc_bank.p12")
print(decrIdentity)