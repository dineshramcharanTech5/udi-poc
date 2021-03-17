## AWS Server

* aws.digitalid.lgcc.gov.lk
* ip  :13.127.255.199  / 10.20.20.10


* sandbox : /home/mosipuser/mosip-infra/deployment/sandbox-v2
* keys	: /srv/nfs/mosip/

## DB Server

* port:30090
* user: postgres
* pass: <>


##Mosip Modules 

Module : Admin

* URL    :https://aws.digitalid.lgcc.gov.lk/admin-ui
* username : 110122

Module : Pre-Registration Client

* prerequisites :
   refer guides on https://github.com/ICTASL/UDI-poc/tree/master/documentations/local_setup_guide/registration_client/
   E.g
    - successful registration of host machine's master data
    - mock MDS / mosip whitelisted biometrics devices 
                 
* Action    : Run the run.batch of reg-client upon success on above prerequisites
* username  : operator1

Module : Pre-Registration UI
* URL    : https://aws.digitalid.lgcc.gov.lk/pre-registration-ui
* username : email/OTP
