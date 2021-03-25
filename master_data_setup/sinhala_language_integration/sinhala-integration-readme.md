# Sinhala Language Integration

#### Steps to integrate sinhala as the secondary language

1. Add relevant sinhala data records to the master data to following tables
``` 
individual_type (required)
gender (required)
loc_hierarchy_list (required)
location (required)
title
daysofweek-list
```
2. Existing data records should be duplicated for the sin language code as well
3. Create sin.json file in mosip-ref-impl/pre-registration-ui/src/assets/i18n folder with the sinhala translation values.
4. Build and deploy the pre-registration application
5.  Add sinhala labels to the pre-registration and reg-client schema and update using the guide in the link. ``` (https://github.com/ICTASL/UDI-poc/tree/master/documentations/id_object_schema_configurations) ```
6. Login to console server.
7. Go to /srv/nfs/mosip/mosip-config/sandbox
8. Open and edit application-mz.properties file and change the following properties.
``` 
mosip.supported-languages=eng,ara,fra,sin
mosip.secondary-language=sin
mosip.left_to_right_orientation=eng,fra,sin
mosip.kernel.transliteration.sinhala-language-code=sin
```
9. Open and edit admin-mz.properties file and add masterdata table names in sinhala unicode, also chhange the following property. ``` mosip.admin.masterdata.lang-code=eng,ara,fra,sin ```

10. Open and edit registration-mz.properties file and add the following properties.
``` 
mosip.registration.consent_sin = <message>
mosip.registration.important_guidelines_sin=<message>
```

11. Open and edit print-mz.properties file and update the following properties.
``` 
mosip.supported-languages=eng,ara,fra,sin
mosip.primary-language=eng
mosip.secondary-language=sin
```

12. sudo git add the files which you have changed.
13. sudo git commit with an appropriate message.
14. Now once all the changes are committed you need to restart the relevant services to get the changes to be effected.
    - Do a kc1 get pods
    - Search for a pod with name of kernel-masterdata-service and pre-registration-ui-service
    - Do a delete in for those pods: 
    ``` Kc1 delete pod <pod-name> ```
    - It will automatically restart the pod. These pods will be sufficient for the changes done to integrate sinhala language.