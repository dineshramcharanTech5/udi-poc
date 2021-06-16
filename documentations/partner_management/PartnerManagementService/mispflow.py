from authorize import *
from misp import *
from certs import *
from config import *
from Partner import *


token = Authenticate(urlBase,userId,password, appId)
mispPartnerID = "misp100"
mispOrgName = "ABC MISP"
mispCertFile = "certificates\\ABCMISP\\abc_misp.cer"
#Step 1: Create MISP Partner
#Step 2: Upload Certificate
resp = selfRegisterMISPPartner(urlBase,mispPartnerID,mispOrgName, token)
print(resp)
resp = uploadPartnerCertificate(urlBase,mispCertFile,mispOrgName, mispPartnerID,"Auth", token)
print(resp)
resp = UpdatePartnerStatus(urlBase,mispPartnerID,"Active",token)
print(resp)
resp = generateMISPLicense(urlBase, mispPartnerID, token)
print(resp)