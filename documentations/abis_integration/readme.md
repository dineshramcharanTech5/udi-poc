# ABIS Integration in mosip
Go to the following location inside cloned repo (for now it will be in lgc1) https://github.com/mosip/mosip-infra/tree/1.1.3/deployment/sandbox-v2/utils/onboard/partner
 
   lgc1 : 192.168.204.5 / 10.250.1.100

## There are 4 json files to be edited 

1. ABIS Partner - 
	Navigate to utils/onboard/partner/data/partner and edit abis.json. Update the details in that as per the ABIS vendor. As in our case it's tech5-abis.

2. Partner Policy Mapping - 
Navigate to utils/onboard/partner/data/policy_groups and edit the abis.json. This 
	Is to make sure a policy and partner mapping.

3. ABIS Policy -
	Navigate to utils/onboard/partner/data/policies and edit abispolicy.json. Update the details as required. Keep in mind here we define whether the policy accepts which biometrics. Also make sure policy_group is correctly mentioned.

4. ABIS Certificates - 
	Navigate to utils/onboard/partner/certs/abis and add the ABIS certificates. These certificates are provided by ABIS providers in our case Tech5.

## Once the above jsons are edited then execute the following commands :

1. .onboard.py policy_group data/policy_groups/abis.json
2. .onboard.py policy_group data/policies/abispolicy.json
3. .onboard.py policy_group data/partners/abis.json

> You can verify the above details correctly added to mosip database by trying out swagger urls

## Next login to the sandbox and follow the below steps
1. navigate to mosip-config and editing Registration-processor-mz.properties. Change the following : 
```
registration.processor.policy.id=tech5-abis
registration.processor.subscriber.id=tech5-abis
```
2. Restart the regproc services

After the restart your changes in the mosip side is completed.

# Starting ABIS (LGC1)

1. Navigate to /opt/Tech5/T5-Plugin-R20210210 
Edit the following fields in config.properties
```
consumeURL=tcp://aws.digitalid.lgcc.gov.lk:30616
publishURL=tcp://aws.digitalid.lgcc.gov.lk:30616

consumeQueue=mosip-to-abis1
publishQueue=abis1-to-mosip

authenticationUrl=https://aws.digitalid.lgcc.gov.lk/v1/authmanager/authenticate/clientidsecretkey

appId=regproc
clientId=mosip-abis-client
secretKey=abc123
```


2. Once the above is edited now execute the following command
	
    ```java -jar T5-Plugin-R20210210.jar```

Now wait for the activeMQ data to be feeded from device registration.




#### Testing ABIS through ActiveMQ

1. Login to https://aws.digitalid.lgcc.gov.lk/activemq/admin/queues.jsp with following creds
```
	Username : admin
	Password  : abc123
```
2. In queues click on Send to operation in mosip-to-abis1
3. Paste the insert body in message body
4. Click send

#### Listening in ABIS plugin

1. Login to ABIS installed lgc1 infrastructure
2. Navigate to /opt/Tech5/T5-Plugin-R20210210
3. Check if nohup is running if its running tailf or cat nohup.out
4. If nohup is not running run the following command to listen 
 ```java -jar T5-Plugin-R20210210.jar```
>Always make sure the jar is running in nohup, as we cant come and listen to it every single time. Command to start the jar in nohup
 nohup java -jar T5-Plugin-R20210210.jar &
Once it's running you can look at the print screen on what happens to the data packet which comes in through activeMQ.


#### Issues faced 
1. Mock Abis was listening to the topic which had to be removed. We removed it through the kube8 dashboard.
2. The reference URL has http instead of https. This was changed in  data-share-mz.properties.
3. Java 11 was not installed in the ABIS lgcc environment. It was installed and configured.
4. Even though the ABIS plugin was running, ABIS was not started at the initial stage.


#### How to see the where the process has gone through in mosip db level

1. Open regprc.registration_transaction. In this table we can see the complete transaction of a job. Using reg_id should be able to narrow the transaction down and check its status in status comment.
2. To see the request body sent to ABIS you need to open regprc.abis_request.Query with ref_regtrn_id and get your checking specific record. Add the following with it to get the req_text to be readable.

		```select encode(regprc.abis_request.req_text, 'escape') as your_alias_name from regprc.abis_request;```


#### How to clear the ABIS cache
   navigate to the following 
   ```cd /opt/Tech5/T5-Plugin-R20210210/```
   
1. Use the following command to check what java services are running 
        ```ps aux | grep java```
2. Stop all the java services

   ```kill -9 `pgrep java` ```  

3. Removing ABIS services logs
```      
	rm -rf /opt/Tech5/T5-ABIS/IrisTC/logs/*
	rm -rf /opt/Tech5/T5-ABIS/IrisM/logs/*
	rm -rf /opt/Tech5/T5-ABIS/Master/logs/*
	rm -rf /opt/Tech5/T5-ABIS/FaceM/logs/*
	rm -rf /opt/Tech5/T5-ABIS/FaceTC/logs/*
	rm -rf /opt/Tech5/T5-ABIS/FingerM/logs/*
	rm -rf /opt/Tech5/T5-ABIS/FingerTC/logs/*
```	
	
4. clear the cache :
	```rm -rf /opt/Tech5/T5-ABIS/cache/*```
	
5. start abis :
	```for i in Master FingerTC FingerM IrisTC IrisM; do sh /opt/Tech5/T5-ABIS/$i/bin/catalina.sh start; sleep 10; done```	
	
6. start t5plugin :
	 ```nohup java -jar t5plugin1.3r20210319.jar &```
	 ```tailf nohup.out```
7. getStatus of abis

	```curl http://localhost:9090/T5CloudService/1.0/getStatus```


	Once the above steps are complete the ABIS will be fresh as new.
	
	
#### Technical Guides 

- T5-ABIS Developer Guide :  http://wiki.tech5.tech/Tech5-AbisDeveloperGuide.html
	
	
