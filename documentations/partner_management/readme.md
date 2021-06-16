# Partner Management steps

## Auth partner onboarding steps

1. Create the root ca certificate using java keytool (batch files are provided in ABCBank folder)
2. Create a partner certificate and sign it using the root certificate (batch files are provided in ABCBank folder)
3. Excecute the steps in main.py to onboard a partner

## MISP partner onboarding steps

1. Create a misp partner certificate and sign it using the same troot certificate (batch files are provided in ABCMISP folder)
2. Execute the steps in mispflow.py to onboard a misp partner

## Authentication using auth-ui steps

1. Get the misplicence key, partnerId and partnerAPIkey from db
2. Clone the following repo https://github.com/ICTASL/udi-poc-mosip-ref-impl/tree/1.1.5-develop-sl and run the auth ui
3. replace the misplicence key, partnerId and partnerAPIkey in application.properties
4. Try otp authentication by providing a valid UIN

## Authentication using python scripts and demo utility

1. Get the misplicence key, partnerId and partnerAPIkey from db
2. Replace the misplicence key, partnerId and partnerAPIkey in config.py
4. Run the runLocal.bat file in demo utility folder
5. Execute the authflow.py to test otp authentication