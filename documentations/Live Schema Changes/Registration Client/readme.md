# Reg Client

1. Change schema JSON in regclient according to the requirement.
2. Copy the schema section in it.
3. Open https://aws.digitalid.lgcc.gov.lk/v1/authmanager/swagger-ui.html#/authmanager/authenticateUseridPwdUsingPOST and use the following to authenticate :
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
4. Then open https://aws.digitalid.lgcc.gov.lk/v1/masterdata/swagger-ui.html#/Identity%20Schema/createSchemaUsingPOST replace the schema in the body which you copied. Lastly add a title. Try to keep it consistent with the actual versioning. Once this is executed get the id inside the response.

5. Then go to https://aws.digitalid.lgcc.gov.lk/v1/masterdata/swagger-ui.html#/Identity%20Schema/publishSchemaUsingPUT and add the id which you copied from step 4. At first when you execute the api will fail. Get the timestamp in the response you get and add 1 minute extra and assign it to effectiveFrom value. Then publish

6. To see the effect go and restart the reg client docker services. Sometimes it will require you to restart again. Double check if your json changes are there in the latest schema json inside reg client.