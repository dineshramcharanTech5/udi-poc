# Registration client customization and deployment 

1. Fork https://github.com/mosip/registration
2. Edit all.yml(in sandbox in console) with the following details : 
	```
	docker:
	    hub:
	        private : true
	        keyname: udipockey
	```
3. Edit config.py
	```server = ‘https://aws.digitalid.lgcc.gov.lk’```
4. Edit versions.yml
	```
	registration_client:
       downloader:
        	'reg-client-downloader': 'udipoc/registration-client:1.1.3-michael'
       version: 1.1.3
    ```
5. Go to the forked registration repository
6. Go to settings -> Secrets
    Then update the ACTOR and RELEASE of DOCKER_HUB(username and password respectively)
7. After the above change go to    
https://github.com/ICTASL/udi-poc-registration/blob/1.1.3-michael/.github/workflows/push_trigger.yml
Apply the following changes : 
```
	build_client:
   runs-on: ubuntu-latest
   env:
     NAMESPACE: mosipdev
     SERVICE_NAME: registration-client
     SERVICE_LOCATION: registration
** update the maven builds section in push trigger of build client by appending this
mvn clean install -U -s $GITHUB_WORKSPACE/settings.xml -DskipTests -Dgpg.skip --file pom.xml
```
8. Go into helm2 and delete reg-client-downloader
9. Install reg-client-downloader using ansible

>Once you pushed the above changes to github with the above changes it will automatically detect the changes through github Action and will deploy the changes in dockerhub. 

You can check the deployments & their status in https://github.com/ICTASL/udi-poc-registration/actions

