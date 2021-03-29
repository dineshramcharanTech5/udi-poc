## The flow of overall SLUID will be as follow : 

1. Open Pre Registration. Fill data and get the Pre Registration ID.
2. Open Reg Client Enter that ID and fetch the data.
3. Proceed with giving documents and biometric data.
4. Login with Supervisor credentials and approve the resident data.
5. Upload the approved data.
6. Data will be going to ABIS to check for biometric deduplication.
    a. If the data is genuine then it will pass ABIS and continue to generate UIN and the resident will get an email saying UIN is generated for their RID.
    b.If the data is duplicate the process will stop there and the Regclient will get a notification to inform the resident.

#### Testing ABIS through activeMQ

1. Login to https://aws.digitalid.lgcc.gov.lk/activemq/admin/queues.jsp with following creds
```
	Username : admin
	Password  : abc123
```
2. In queues click on Send to operation in mosip-to-abis1
3. Paste the insert body in message body
4. Click send

#### Listening in ABIS plugin

1. Login to ABIS installed lgcc infrastructure
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
	
5. start abis   
	```for i in Master FingerTC FingerM IrisTC IrisM; do sh /opt/Tech5/T5-ABIS/$i/bin/catalina.sh start; sleep 10; done```	
	
6. start t5plugin
	 nohup java -jar t5plugin1.3r20210319.jar &
	 tailf nohup.out
7. getStatus of abis

	```curl http://localhost:9090/T5CloudService/1.0/getStatus```


Once the above steps are complete the ABIS will be fresh as new.
