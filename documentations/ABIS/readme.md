# ABIS Integration in mosip
Go to the following location inside cloned repo (for now it will be in lgcc) https://github.com/mosip/mosip-infra/tree/1.1.3/deployment/sandbox-v2/utils/onboard/partner

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

# Starting ABIS(LGCC)

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
