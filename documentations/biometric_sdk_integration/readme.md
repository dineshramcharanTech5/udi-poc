# Bio-metric SDK Integration with mosip registration client module :

Pre-requisite : Download the relavant exteranl bio-sdk vendor's setup files from below location & refer respective user guides
                URL : https://nextcloud.internal.icta.lk/index.php/apps/files/?dir=/SLUID/PoC/BiometricSDK&fileid=2839310


  
# Bio-SDK integration with reg-client module-1.1.5 :

This guide lists out all the steps and supportive materials on

   ## How to package exteranl bio-sdk dependencis with mosip reg-client-1.1.5 as a standalone application
 
 

# How to package exteranl bio-sdk dependencis with mosip reg-client-1.1.5 as a standalone application
   
1.  Clone https://github.com/ICTASL/udi-poc-registration-client.git & switch to relavant feature branch  
2.  Commit and push bio-sdk dependencies in a zip file located in persistent volume location
        E.g sdkDependency.zip 
		
3.  Run mvn install -DskipTests -Dgpg.skip
4.  Change docker build & run command properties  accordingly       
	
	E.g :
	
	
	In Linux Environment : 
	----------------------
	
	client_version_env='1.1.5'
	crypto_key_env='bBQX230Wskq6XpoZ1c+Ep1D+znxfT89NxLQ7P4KFkc4='
	db_bootpwd_env='bW9zaXAxMjM0NQ=='
	tpm_enabled_env='Y'
	client_certificate_env='mosip_cer.cer'
	client_upgrade_server_env='http://localhost:80'
	reg_client_sdk_url_env='true'   
	persistent map file : /opt/mosip/build_files:/build_files
	
	


	In Windows Environment : 
	-------------------------
	
	
	Use above values without quotes and map the persistent volume created accordingly in your local path
	
	persistent map file : C:/icta/1.1.5/icta-reg-client/registration/build_files:/build_files #create a directory :build_files  to map a persistence volume 
	

5.  Buid the reg-client docker image with tagging appropriately
	
	E.g  docker build . --tag reg-cli:1.1.5-tech5-biosdk-2


6. Run the above image after setting properties as in Step 2 and modifying Dockerfile & configure.sh accrodingly
	
	E.g 
	
	  docker run --rm  -p 80:80  -e reg_client_sdk_url_env=true -e client_version_env=1.1.5 -e crypto_key_env=bBQX230Wskq6XpoZ1c+Ep1D+znxfT89NxLQ7P4KFkc4= -e db_bootpwd_env=bW9zaXAxMjM0NQ== -e tpm_enabled_env=Y -e client_certificate_env=mosip_cer.cer -e client_upgrade_server_env=http://localhost:80 -v :/build_files --entrypoint /bin/bash -it reg-cli:1.1.5-tech5-biosdk-2
	  
	  
	  
	  docker run --rm  -p 80:80  -e reg_client_sdk_url_env=true -e client_version_env=1.1.5 -e crypto_key_env=bBQX230Wskq6XpoZ1c+Ep1D+znxfT89NxLQ7P4KFkc4= -e db_bootpwd_env=bW9zaXAxMjM0NQ== -e tpm_enabled_env=Y -e client_certificate_env=mosip_cer.cer -e client_upgrade_server_env=http://localhost:80 -v C:/icta/1.1.5/icta-reg-client/registration/build_files:/build_files --entrypoint /bin/bash -it reg-cli:1.1.5-tech5-biosdk-3



7. run configure.sh in bash shell

8. if step 7 gets completed , then reg-client.zip can be downloaded in your local environment as below
	E.g http://localhost:80/registration-client/1.1.5/reg-client.zip
	
9. Extract the reg-client.zip   
	
10. Extract the bio-sdk license files,config.properties within above extracted reg-client 

11. Update ‘registration-mz.properties’  with all properties given in bio-sdk-properties.txt 
    
12. Run the run.bat and monitor the sdk log traces for successful bio-sdk intilizations and their fucntionality 



Note : Currently ,Step 10 is being optimizated for smooth integration with reg-client
	
