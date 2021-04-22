# Pre Registration

1. Login to console server.
2. Go to /srv/nfs/mosip/mosip-config/sandbox
3. Open and edit pre-registration-demographic.json according to the requirement JSON similar to the RegClient you did above. (Keep in mind that variables are same but content on how it is created is different so don't copy paste from Reg client) 
   Note: currently there are two fields types : default & dynamic. Ref : Reg client section for adding dynamic fields through API
5. Next open and edit pre-registration-mz.properties. Change the idschema version in this according to your regclient schema version.
6. Once all the changes are done in the file level you need to commit the changes
7. Git add the files which you have changed.
8. Git commit with an appropriate message.

>	You don't have to push the changes as it is pointed to the local setup as it refers only to mosip-config inside /srv/nfs/mosip. Please make sure your changes are committed by checking git status before going to the next step.

6. Now once all the changes are committed you need to restart the relevant services to get the pre registration changes to be effected.
    - Do a kc1 get pods
    - Search for a pod with name of prereg-application-service which may look like below : 
Prereg-application-service-5dc8c8b68b-744c9
(The above is the pod name at the moment when this document is created) 
    - Do a delete in for that pod: 
    ``` Kc1 delete pod <pod-name> ```
    - It will automatically restart the pod. This pod will be sufficient for the changes done to pre pre-registration json file.



 #### Facts to Remember
> 1. If you need to disable UMC validation go to registration-processor-mz.properties and change the boolean value.
2. If you need to point the registrations centers to another location code go to pre-registration-mz.properties and change preregistration.recommended.centers.locCode value.
4. If you need to change secondary language details go to application-mz.properties and edit the mosip.secondary-language.	
5. The other pods and the relevant changes require to restart: 
    - Kernel-syncdata-service      :  Language Changes such as removing secondary language
    - Prereg-batchjob-service       :  Once a new Registration center is added.
    - Regproc-osi-validator-stage :  When UMC validation is disabled

