# Registration Client Setup in local environment 
 
1. Add Environment variable as follow : 
	```
	variable name : mosip.hostname
	variable value: aws.digitalid.lgcc.gov.lk
	```
2. Download java 11 with fx using the following link (https://www.azul.com/downloads/zulu-community/?version=java-11-lts&os=windows&package=jdk-fx)
3. Clone https://github.com/ICTASL/registration & check out to version 1.1.3 for ICTSL/UDI POC
4. Go inside the directory named as registration.
5. Import maven changes
6. Make sure that the correct jdk with fx is pointed in ide
7. Travers the following way and get to initialization.java
cd registration-client/src/main/java/io/mosip/registration/controller
8. Make sure the following value is present in the file on line 39
private static String upgradeServer = "http://localhost:80";
9. Then come back to registration-services and add the following snippet into pom.xml file
	       <dependency>
			<groupId>io.mosip.mock.sdk</groupId>
			<artifactId>mock-sdk</artifactId>
			<version>0.9-rc1</version>
		</dependency>
10. Import the maven changes again.
11. Switch to registration-services/src/main/resources/ and edit spring.property, change the value as given below
	```
	mosip.hostname = aws.digitalid.lgcc.gov.lk
	```
Now run the initialization.java inside registration.client file ( Refer screenshot for run configurations)



# Common Issues & Resolutions


#### 1. Registration client being run before 

If you have ran the Registration client prior to this you may have faced an error as below:

![Intellij IDE Error](https://github.com/ICTASL/UDI-poc/blob/master/documentations/registration_modules_setup/registration_client/local_setup/IntelliJ_Error.png)

This error comes due to the manifest file missing based on your db.conf. 
In order to resolve this you may have to visit the place you built the registration client prior to this and locate the MANIFEST.MF and copy it to the main directory of your cloned registration repo.



#### 2. Error running 'Initialization': Command line is too long. Shorten command line for Initialization.

This error comes due to the IDE configuration of command line execution. Mostly this issue comes in Intellij IDE. To resolve this you need to do the following: 
Open ‘edit run/debug configuration’ dialog.
Select Edit configurations and select Initialization.
As shown in the below image the shorten command line is set to ‘user-local default none’. You need to change that to ‘@argFiles (java9+)’. If that also throws the same error try other options in the dropdown.
![Configuration dialog](https://github.com/ICTASL/UDI-poc/blob/master/documentations/local_setup_guide/registration-client/configuration_dialog.JPG)

#### 3. Error running 'Initialization': REG-INIT-001 --> Application found in invalid state, tampering detected ! 

This error due to inconsistencies either in .mosipkeys or db folders.  to resolve clear those entries and re attempt 
