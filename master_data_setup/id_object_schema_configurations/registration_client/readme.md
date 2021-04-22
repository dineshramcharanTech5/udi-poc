# Reg Client

1. Change latest schema JSON ( **E.g SCHEMA_1.4** ) in reg client setup according to the requirement.
     Note : for creating dynamic fields, pls Refer **dynamic-field-sample.json**  and make use following 
     API : **https://aws.digitalid.lgcc.gov.lk/v1/masterdata/swagger-ui.html#/Dynamic%20Field/createDynamicFieldUsingPOST
     **
2. Copy the contents of the schema section after applying changes on it.
3. Authenticate with API : https://aws.digitalid.lgcc.gov.lk/v1/authmanager/swagger-ui.html#/authmanager/authenticateUseridPwdUsingPOST** or
 **https://aws.digitalid.lgcc.gov.lk/v1/authmanager/swagger-ui.html#/operations/authmanager/userIdOTPUsingPOST** and use the following to authenticate :
``` 
{
  "id": "string",
  "metadata": {},
  "request": {
    "appId": "admin",
    "password": "mosip",
    "userName": "110006"
  },
  "requesttime": "2018-12-10T06:12:52.994Z",
  "version": "string"
}
```
4. Next, call all the API: **https://aws.digitalid.lgcc.gov.lk/v1/masterdata/swagger-ui.html#/Identity%20Schema/createSchemaUsingPOST** and replace the contents of the schema which you has copied in step 2.
 Lastly, add a title. Try to keep it consistent with the actual versioning by refering latest ones. Once this is executed get the id inside the response.

5. Next, call the API **https://aws.digitalid.lgcc.gov.lk/v1/masterdata/swagger-ui.html#/Identity%20Schema/publishSchemaUsingPUT** and add the id which you copied from step 4. At first when you execute the api will fail. Get the timestamp in the response you get and add 1 minute extra and assign it to effectiveFrom value. try publish

6. To verify the changes done. Pls, restart the reg client module and sync. Sometimes it will require you to restart reg clinet and related docker services.
   Double check if your json changes are there in the latest schema json inside reg client after syncing.
