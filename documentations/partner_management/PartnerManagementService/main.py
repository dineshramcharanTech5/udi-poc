from authorize import *
from PolicyGroup import *
from policy import *
from Partner import *
from certs import *
from config import *



token = Authenticate(urlBase,userId,password, appId)
print(token)


# resp =getAllAPIKeyRequests(urlBase, partnerId, token)
# print(resp)


# #Step 1 : Pre requistes - onboard all truested ROOT CAs of the Country 
# # This is done by Country Implementation - Not by Partner

# CARootCert = "certificates\\XYZBank\\root_lion2_ca.cer"
# partnerDomain  = "Auth"

# resp = uploadCACertificate(urlBase,CARootCert,partnerDomain,token)
# print(resp)

# #end Step 1

# #Step 2: Create Policy Group and Required Policies

# policyGroupName = "policyGroupTest1"

# resp =createPolicyGroup(urlBase,policyGroupName,"Policy Group for Testing One", token)
# #Get Policy ID by Group Name
# policyGroupId = getPolicyGroupByName(urlBase, policyGroupName, token)
# print('policyGroupId=' +policyGroupId)
# policyGroupId=323996

# #Step 3: Define and publish the Policy

policyName = "KYC_dfcc_Acc"
# policyId = definePolicy(urlBase,policyGroupName,policyName, token)

# if type(policyId) != int:
#     print(policyId)
#     policyId = getPolicyByName(urlBase,policyName, token)

# print(policyId) = 233647

# resp = publishPolicy(urlBase,policyId,policyGroupId,token)

# #Step 4: Self Register Partner



# resp = selfRegister(urlBase,partnerName,policyGroupName,partnerId, token)
# print(resp)

# #Step 5: Upload Partner Certificate  and Activate
# partnerCertFile = "certificates\\XYZBank\\def_bank.cer"

# resp = uploadPartnerCertificate(urlBase,partnerCertFile,partnerName, partnerId,partnerDomain, token)
# print(resp)

# resp = UpdatePartnerStatus(urlBase,partnerId,"Active",token)
# print(resp)

# #Step 6: Request for API Key for the policy

usecaseDesc = "Test partner API key"

#669663
# apiKeyRequestID = submitPartnerAPIKeyRequest(urlBase,partnerId,policyName,usecaseDesc, token)
# print(apiKeyRequestID)
apiKeyRequestID = "882156"
resp = ApprovePartnerAPIKeyRequest(urlBase,apiKeyRequestID,token)
print(resp)





