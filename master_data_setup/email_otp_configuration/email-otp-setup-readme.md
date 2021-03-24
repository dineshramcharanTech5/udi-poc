# Email & OTP Configuration

#### Steps to configure email service

1. Login to console server.
2. Go to /srv/nfs/mosip/mosip-config/sandbox
3. Open and edit kernel-mz.properties file and change the following properties according to your email server.
``` 
mosip.kernel.notification.email.from=mosipuser@gmail.com
spring.mail.host=smtphost
spring.mail.username=username
spring.mail.password=password
spring.mail.port=587
```
4. sudo git add the files which you have changed.
5. sudo git commit with an appropriate message.
6. Now once all the changes are committed you need to restart the relevant services to get the changes to be effected.
    - Do a kc1 get pods
    - Search for a pod with name of kernel-notification-service
    - Do a delete in for that pod: 
    ``` Kc1 delete pod <pod-name> ```
    - It will automatically restart the pod. This pod will be sufficient for the changes done to configure email server.

#### Steps to configure email templates

1. Connect to the master database
2. Select the template table and edit or add templates according to your requirement.
3. Make sure the velocity template placeholders are valid for the relevant module.
4. Once the master data has been changed restart the kernel-masterdata-service
    - Do a kc1 get pods
    - Search for a pod with name of kernel-masterdata-service
    - Do a delete in for that pod: 
    ``` Kc1 delete pod <pod-name> ```
    - It will automatically restart the pod.

5. If you need to receive emails in only the primary language, do the following changes
    - Login to console server.
    - Go to /srv/nfs/mosip/mosip-config/sandbox
	- Open and edit application-mz.properties file and change the following property ``` mosip.notification.language-type=PRIMARY ```.
    - git add and commit the changes
	- restart the registration-processor-message-sender-service pod

#### Steps to configure proxy otp to random otp

1. Login to console server.
2. Go to /srv/nfs/mosip/mosip-config/sandbox
3. Open and edit application-mz.properties file and change the following properties.
``` 
mosip.kernel.sms.proxy-sms=false
mosip.kernel.auth.proxy-otp=false
mosip.kernel.auth.proxy-email=false

```
4. sudo git add the files which you have changed.
5. sudo git commit with an appropriate message.
6. Now once all the changes are committed you need to restart the relevant services to get the changes to be effected.
    - Do a kc1 get pods
    - Search for a pod with name of kernel-otp-manager-service and pre-registration-ui-service
    - Do a delete in for those pods: 
    ``` Kc1 delete pod <pod-name> ```
    - It will automatically restart the pod. These pods will be sufficient for the changes done to the proxy otp.

