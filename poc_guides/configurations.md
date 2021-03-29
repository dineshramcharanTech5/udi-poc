#### SLUDI-POC Server Details   

## AWS Server

* aws.digitalid.lgcc.gov.lk
* ip  :13.127.255.199  / 10.20.20.10


* sandbox : /home/mosipuser/mosip-infra/deployment/sandbox-v2
* keys	: /srv/nfs/mosip/

## DB Server

* port:30090
* username: postgres
* password: mosip123



## ICTA DockerHub

* URL:https://hub.docker.com
* username: udipoc
* password: 1qaz2wsx@0okm


#### SLUDI-POC Sandbox Modules 


Module : Admin

* URL    :https://aws.digitalid.lgcc.gov.lk/admin-ui
* username/password : 110122/Techno@123, 110006/mosip

Module : Pre-Registration Client

* prerequisites :
   refer guides on https://github.com/ICTASL/UDI-poc/tree/master/documentations/local_setup_guide/registration_client/
   E.g
    - successful registration of host machine's master data
    - mock MDS / mosip whitelisted biometrics devices 
                 
* Action    : Run the run.batch of reg-client upon success on above prerequisites
* username/password  : operator1/root



Module : Pre-Registration UI
* URL    : https://aws.digitalid.lgcc.gov.lk/pre-registration-ui
* username/password : email/OTP


Module : IAM/Keyclock
* URL    :   https://aws.digitalid.lgcc.gov.lk/keycloak/auth/
* username/password : admin/admin


Module : ActiveMQ
* URL    :  https://aws.digitalid.lgcc.gov.lk/activemq/admin/queues.jsp
* username/password : admin/abc123


Module : Minio
* URL    :   https://aws.digitalid.lgcc.gov.lk/minio/login
* username/password : 



## Monitoring Modules

K8s Dashboard - MZ
* URL    :   https://aws.digitalid.lgcc.gov.lk/mz-dashboard
* Token  : 	 
	eyJhbGciOiJSUzI1NiIsImtpZCI6Il9oOXdEZ2M2MDdtNlRRZ0FheVJPaDRCY1RGZm5TcERsMm11VjJacnFhSFEifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLXJkbjdxIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIzMmQyNmU3MS1jZDM0LTQ2MjYtYjRlYy05NzJmZWViNDk3NDciLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZXJuZXRlcy1kYXNoYm9hcmQ6YWRtaW4tdXNlciJ9.anjj4wZEcRhGvoklAsBHXDelyY202KQEE8NVjiXLCe01dlSYEtGD0DzOfL2gnkuSaJRVnXyejRGwYOZHDK58qy8_xhFnbP247vuZ-fy3tDhCROIdK-XYSODuysDVb5ncXROuHZYRyqVkTtIeOILcoK7_lBT3HDk2Oclqisp066LWBHn-3dFVhjQUE0Ft_FyzwQJe_l805G2YTHf_p9y1yFyH-TBSGTtl_YVANO99hY-zFGcSCz6PhFMfkvvCku-34n9P9yI-BBJWRer2oj68i16QWzRtZoOewMfmLVdoY-wv61YZm7YczodVBdAQmGgX6bek3u1cklJ_fYBAF6au1A


K8s Dashboard - MDMZZ
* URL   :   https://aws.digitalid.lgcc.gov.lk/dmz-dashboard
* Token : 

eyJhbGciOiJSUzI1NiIsImtpZCI6IktjYWlOZVFac3NfX1BVYV9UaWJ1NGdkbHU4WWNFZUM4MktuSEc3cGhwSG8ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLThqbW5sIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIwNzQ2YTE4Zi1kZTJkLTQ4MzMtYThiMi0zMGY3MWE0OGJlODIiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZXJuZXRlcy1kYXNoYm9hcmQ6YWRtaW4tdXNlciJ9.m5jGIC67wg6C1pkSHSQWApBFlGZhzbk9ygwFEYDO0yhAnmmLA8_jqctnl2vZQj8tTUAockhP-UCgVc5ZimqQ8sDk1hvIWi9oEWqvONS0YrtiCkyaZN5oZwMSOVM_twa7LrSVbOi3MrOCJmE0xNs6Cy40yzBl1x2Zs6Qj_SP47A_DlrgqXOjNUkGdYKPbHc13U8cr8m5dAXeDfpZV2Fw3j5a_Mc2GJQ4iTBuxQyeiueaTuP8JlcVEarnO5zsoNsH8LmG0ywpWzO1DJ5d3cLji5qoqFsZu_BZgVABSCOgyx0OWIfcfeTeg4kLKBrp9agSRMBf31_BQRsc7WSH0EVBoEA


Grafana - MZ
* URL   :   https://aws.digitalid.lgcc.gov.lk/mz-grafana/login
* Email/username/token/password : ISPfGJZ2S4saNjkBJHsaaEPeTftkBfLYU67dEjxq


Grafana - DMZ
* URL   :    https://aws.digitalid.lgcc.gov.lk/dmz-grafana/
* Email/username/token/password : hStHWZyypSP2k3DzcjCyKRQxl51gFy9C4Q0kENim


Kibana 
* URL   :  https://aws.digitalid.lgcc.gov.lk/kibana/
* Email/username/token/password : 

