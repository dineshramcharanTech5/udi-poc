# Biometrics Device Set up in Windows environment

This guide lists out all the required steps and supportive materials in setting up biometric devices especially Manthra Dual IRIS & Fingerprint Device) in windows environment.

1. Set up following device drivers as shown in **i** to **iii** and follow the MDS User manual


      i.    MATISX Driver Setup (Dual IRIS)
            - MATISXDriver.zip

      ii.   MORPHS60 Driver Setup (Fingerprint Device - Ten print)
            - MORPHS60Driver.zip

      iii.  MDS Setup
            - Mantra_MDS_2.0.6_Spec_0.9.5.zip

      iv.   MDS User Manual
            - Refer Mantra_MDS_L0_Manual_Windows.pdf

      v.    MDT Testing Kit Url
            - http://test.mosip.io/phase2/run



2. Set up client utility to populate device information to mosip platform

	Please find below steps to run DeviceRegisterAndDeRegister utility using any IDE

	 
	  i.  Import the project https://github.com/mosip/mds-testing-kit/tree/master/mosip-device-reg/DeviceRegisterAndDeRegister into IDE
	 
  	  ii.  Check/put your login credential  in DeviceRegisterAndDeRegister\src\main\resources\commonData.properties
		    E.g partner_user/admin_user	& their passwords

	  iii. Check environment related files here DeviceRegisterAndDeRegister\src\main\resources\dbFiles
		    E.g masterdatasl.cfg.xml, pmssl.cfg.xml, regdevicesl.cfg.xml  ( append <sl> suffix at the end)

	  iv.  Check provider details or prerequisite data to run the application here  DeviceRegisterAndDeRegister\dataFolder\deviceData.csv
		    E.g
                                  
            dType,deviceId,deviceCode,purpose,serviceVersion,deviceSubId,firmware,deviceStatus,env,certification,callbackId,serialNo,make,model,type,deviceSubType,deviceProvider,deviceProviderId,name,description,deviceTypeCode,zoneCode,regCenterId,partnerType,policyGroup
                 
            Iris,9f6b499b-09b7-4867-a032-a9ebfb1af1fa,9f6b499b-09b7-4867-a032-a9ebfb1af1fa,Registration,1.0.0,[1-2-3],1.0.0,READY,Staging,L0,http://127.0.0.1:4501/,000003621382,MANTRA,MATISDX,Iris,Double,Mantra Softech India Pvt. Ltd.,729aaa95-d812-4285-9231-c0200a970401,Double Iris,To capture Iris,IRS,RBT,99999,Device_Provider,Device_Provider
                     
            Finger,b85f19d8-01da-43b6-b3a1-c8ee92fd3cac,b85f19d8-01da-43b6-b3a1-c8ee92fd3cac,Registration,1.0.0,[1-2-3],1.0.0,READY,Staging,L0,http://127.0.0.1:4501/,000055555555,MANTRA,MORPHS60,Finger,Slap,Mantra Softech India Pvt. Ltd.,729aaa95-d812-4285-9231-c0200a970401,Finger Scanner,To capture FRS,FRS,RBT,99999,Device_Provider,Device_Provider
                     
            Face,6f3811f4-1b09-4570-be27-1a1792c1e28c,6f3811f4-1b09-4570-be27-1a1792c1e28c,Registration,1.0.0,[0],1.0.0,READY,STAGING,L0,http://127.0.0.1:4501/,98AE05C0,MANTRA,MFACE,Face,Full face,Mantra Softech India Pvt. Ltd.,729aaa95-d812-4285-9231-c0200a970401,Camera,To capture photo,CMR,RBT,99999,Device_Provider,Device_Provider


	  v.   Go to Runner.java class (DeviceRegisterAndDeRegister\src\main\java\com\mosip\io\Runner.java) right click on class and click on java application 		select run as run configuration.

      vi.  Give the vm arumgent 
		       E.g 
		       -Dtype=<Finger -Denv.user=<dev> -DbaseUrl=<https://dev.mosip.net>

		       -Dtype=All -Denv.user=sl -DbaseUrl=https://aws.digitalid.lgcc.gov.lk		

      vii.   vm arumgent -Dtype values can be either Finger,Face,Iris and Auth or All (to run all types at one-shot) and sl as Denv.user

	  viii. After running deviceRegistration steps at last we can see option for de-registration of devices like

		         Do you want to de-register the device  press Y/N  Press Y for de-register the deivce  or Press N to exit the program execution.

      ix.   Logs can be found here DeviceRegisterAndDeRegister\testRun\logs.


#### Note : Above functionality can be achieved through device registration API's and in practice vendor invoke these APIS as part of the registration of respective  		  bio metrice devices to mosip platform


### API Flow for Registering a Device (IRIS/FINGER PRINT/FACIAL) with Mosip as device partner

    Ref : https://github.com/ICTASL/UDI-poc/blob/master/documentations/postman_collection/Device%20Registration%20Flow.postman_collection.json

* Running  Authentication for Admin/Partner Login    
    - https://aws.digitalid.lgcc.gov.lk/v1/authmanager/authenticate/useridPwd

* Running Partner Self Registration    
    - https://aws.digitalid.lgcc.gov.lk/partnermanagement/v1/partners/devicedetail

* Running Save/Approve Device Detail
    - https://aws.digitalid.lgcc.gov.lk/partnermanagement/v1/partners/devicedetail

* Running Save/Approve SecureBiometricInfo  
    -  https://aws.digitalid.lgcc.gov.lk/partnermanagement/v1/partners/securebiometricinterface

* Running CreateDevice Specification 
    - https://aws.digitalid.lgcc.gov.lk/v1/masterdata/devicespecifications

* Running Save Device Detail  
    - https://aws.digitalid.lgcc.gov.lk/v1/masterdata/devices

* Running SignedRegisteredDevice
    - https://aws.digitalid.lgcc.gov.lk/partnermanagement/v1/partners/registereddevices


### Related Databases & their tables 


* pms : partner
* regdevice : secure_biometric_interface, registered_device_master, device_detail
* master.device_spec, device_master

####Note : for a comprehensive guide on Device Registration API Flow With Postman can be found from
Ref: https://github.com/ICTASL/UDI-poc/blob/master/mosip_device_registration/device_registration_api_setup_guide.docx	

