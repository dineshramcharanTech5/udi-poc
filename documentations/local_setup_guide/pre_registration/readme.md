# Pre Registration Setup in local 

#### Steps to setup pre registration on local environment

1. Clone https://github.com/mosip/mosip-ref-impl.git
2. Open directory of pre-registration-ui
3. Run npm install
4. Run ng serve / npm run start
5. Open http://localhost:4200 in the web browser you should be able to see the login screen.

#### You may face the following issues

1. CORS: 
	If you face this issue you need to do the following :
Step one create  a proxy.conf.json file inside src and add the following content : 
 ``` 
{
  "/api/*": {
    "target": "https://aws.digitalid.lgcc.gov.lk/",
    "secure": false,
    "logLevel": "debug"
  }
}
```
 
1. Go to angular.json and travers 
projects -> pre-registration -> architect -> serve -> options

2. Then add "proxyConfig": "src/proxy.conf.json" beside browsertarget.
Go to config.json and environment.ts and change the base url to https://aws.digitalid.lgcc.gov.lk/
3.  Now do a ng serve and you would not face the issue

>	If you still face the issue enable CORS plugin in the browser level and that should let you send and receive different origin requests. You could use the following plugins for Chrome and Firefox : \
Chrome : https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf?hl=en \
Firefox : https://addons.mozilla.org/en-US/firefox/addon/cors-everywhere/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search
 
