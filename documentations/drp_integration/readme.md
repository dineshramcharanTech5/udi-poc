#### DRP Configuration/Integration 

 - Follow the steps mentioned in the document, to setup the External stage locally.
 - Follow Keycloak cloud/local setup doc to configure a realm for the DRP app.
 - Follow client & backend service setup doc to setup the Drp Anngular client & DRP Spring Boot service.


Note: Make sure the pre-requisites have been setup correctly beofer proceeding with the setup.

Pre-requisites:

- Configure VPN (pritunnel) profile to access LGC2 DB
- Clone config repository(https://github.com/ICTASL/udi-poc-mosip-config/tree/1.1.5-drp-mosip-config)
- Clone registration-processor repository(https://github.com/ICTASL/udi-poc-registration/tree/1.1.5-drp-external-stage )
- Clone Backend Service (Auth Service) - https://github.com/ICTASL/udi-poc-drp-backend/tree/development
- Clone DRP Angular Client - https://github.com/ICTASL/udi-poc-drp-frontend/tree/development


DRP application flow:


![DRP-New update Flow (1)](https://user-images.githubusercontent.com/11026172/124411635-8ace9b80-dd6a-11eb-8fab-2f339fbcbfc1.png)
