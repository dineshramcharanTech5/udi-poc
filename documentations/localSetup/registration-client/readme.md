# Registration Client Setup in local 
 

1. Download java 11 with fx using the following link (https://www.azul.com/downloads/zulu-community/?version=java-11-lts&os=windows&package=jdk-fx)
2. Clone https://github.com/mosip/registration.git
3. Go inside the directory named as registration.
4. Import maven changes
5. Make sure that the correct jdk with fx is pointed in ide
6. Travers the following way and get to initialization.java
cd registration-client/src/main/java/io/mosip/registration/controller
7. Make sure the following value is present in the file on line 39
private static String upgradeServer = "http://localhost:80";
8. Then come back to registration-services and add the following snippet into pom.xml file
	<dependency>
			<groupId>io.mosip.mock.sdk</groupId>
			<artifactId>mock-sdk</artifactId>
			<version>0.9-rc1</version>
		</dependency>
9. Import the maven changes again.
Now run the initialization.java inside registration.client file.



# You may face the following issues


#### 1. Registration client being run before 

If you have ran the Registration client prior to this you may have faced an error as below:

![Intellij IDE Error](https://github.com/ICTASL/UDI-poc/blob/master/documentations/localSetup/registration-client/IntelliJ_Error.png)

This error comes due to the manifest file missing based on your db.conf. 
In order to resolve this you may have to visit the place you built the registration client prior to this and locate the MANIFEST.MF and copy it to the main directory of your cloned registration repo.



#### 2. Error running 'Initialization': Command line is too long. Shorten command line for Initialization.

This error comes due to the IDE configuration of command line execution. Mostly this issue comes in Intellij IDE. To resolve this you need to do the following: 
Open ‘edit run/debug configuration’ dialog.
Select Edit configurations and select Initialization.
As shown in the below image the shorten command line is set to ‘user-local default none’. You need to change that to ‘@argFiles (java9+)’. If that also throws the same error try other options in the dropdown.
![Configuration dialog](configuration_dialog.jpg?raw=true)
