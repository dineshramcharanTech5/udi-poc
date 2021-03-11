### Bio-Metrices Device Set up in windows environment ( Dual IRIS & Fingerprint Device)


 1.     Set up following device drivers as shown in 1.1 to 1.3 and follow the MDS User manual 


 1.1    MATISX Driver Setup (Dual IRIS) 
         - MATISXDriver.zip

 1.2     MORPHS60 Driver Setup (Fingerprint Device - Ten print)
        - MORPHS60Driver.zip

 1.3     MDS Setup 
        - Mantra_MDS_2.0.6_Spec_0.9.5.zip

 1.4     MDS User Manual 
          - Refer Mantra_MDS_L0_Manual_Windows.pdf 

 1.5     MDT Testing Kit Url
          http://test.mosip.io/phase2/run


 
 ### 2. Set up client utility to feed device information


	Please find the below steps to run DeviceRegisterAndDeRegister utility using any IDE

	 
	 1.     Import the project https://github.com/mosip/mds-testing-kit/tree/master/mosip-device-reg/DeviceRegisterAndDeRegister  into IDE

	 
  	 2.     Check/put your login credential  in DeviceRegisterAndDeRegister\src\main\resources\commonData.properties
		   E.g partner_user/admin_user	& their passwords

	 3.     Check environment related files here DeviceRegisterAndDeRegister\src\main\resources\dbFiles
		   E.g masterdatasl.cfg.xml, pmssl.cfg.xml, regdevicesl.cfg.xml  ( append <sl> suffix at the end)

	 4.     Check provider details or prerequisite data to run the application here  DeviceRegisterAndDeRegister\dataFolder\deviceData.csv
		 E.g
                                  
		dType,deviceId,deviceCode,purpose,serviceVersion,deviceSubId,firmware,deviceStatus,env,certification,callbackId,serialNo,make,model,type,deviceSubType,deviceProvider,deviceProviderId,name,description,deviceTypeCode,zoneCode,regCenterId,partnerType,policyGroup
             
	Iris,9f6b499b-09b7-4867-a032-a9ebfb1af1fa,9f6b499b-09b7-4867-a032-a9ebfb1af1fa,Registration,1.0.0,[1-2-3],1.0.0,READY,Staging,L0,http://127.0.0.1:4501/,000003621382,MANTRA,MATISDX,Iris,Double,Mantra Softech India Pvt. Ltd.,729aaa95-d812-4285-9231-c0200a970401,Double Iris,To capture Iris,IRS,RBT,99999,Device_Provider,Device_Provider
             
	Finger,b85f19d8-01da-43b6-b3a1-c8ee92fd3cac,b85f19d8-01da-43b6-b3a1-c8ee92fd3cac,Registration,1.0.0,[1-2-3],1.0.0,READY,Staging,L0,http://127.0.0.1:4501/,000055555555,MANTRA,MORPHS60,Finger,Slap,Mantra Softech India Pvt. Ltd.,729aaa95-d812-4285-9231-c0200a970401,Finger Scanner,To capture FRS,FRS,RBT,99999,Device_Provider,Device_Provider
             
	Face,6f3811f4-1b09-4570-be27-1a1792c1e28c,6f3811f4-1b09-4570-be27-1a1792c1e28c,Registration,1.0.0,[0],1.0.0,READY,STAGING,L0,http://127.0.0.1:4501/,98AE05C0,MANTRA,MFACE,Face,Full face,Mantra Softech India Pvt. Ltd.,729aaa95-d812-4285-9231-c0200a970401,Camera,To capture photo,CMR,RBT,99999,Device_Provider,Device_Provider



	 5.     Go to Runner.java class (DeviceRegisterAndDeRegister\src\main\java\com\mosip\io\Runner.java) right click on class and click on java application 		select run as run configuration.

	 6.     Give the vm arumgent 
		       E.g 
		       -Dtype=<Finger -Denv.user=<dev> -DbaseUrl=<https://dev.mosip.net>

		       -Dtype=All -Denv.user=sl -DbaseUrl=https://aws.digitalid.lgcc.gov.lk		

	 7.     vm arumgent -Dtype values can be either Finger,Face,Iris and Auth or All (to run all types at one-shot) and sl as Denv.user

	 8.     After running deviceRegistration steps at last we can see option for de-registration of devices like

		 Do you want to de-register the device  press Y/N  Press Y for de-register the deivce  or Press N to exit the program execution.

	 9.     Logs can be found here DeviceRegisterAndDeRegister\testRun\logs.


	
 ### Note : Above functionality can be achieved through device registration API's and in practice vendor invoke these APIS as part of the registration of respective  		  bio metrice devices to mosip platform
		

 ### API Flow for Registering a Device (IRIS/FINGER PRINT/FACIAL) with Mosip as device partner 
    REf : https://github.com/ICTASL/UDI-poc/blob/master/documentations/postman_collection/Device%20Registration%20Flow.postman_collection.json

    Running  Authentication for Admin/Partner Login    
      https://aws.digitalid.lgcc.gov.lk/v1/authmanager/authenticate/useridPwd

  
    Running Partner Self Registration    
        https://aws.digitalid.lgcc.gov.lk/partnermanagement/v1/partners/devicedetail


    Running Save/Approve Device Detail
      https://aws.digitalid.lgcc.gov.lk/partnermanagement/v1/partners/devicedetail

   
    Running Save/Approve SecureBiometricInfo  
      https://aws.digitalid.lgcc.gov.lk/partnermanagement/v1/partners/securebiometricinterface

    
    Running CreateDevice Specification 
      https://aws.digitalid.lgcc.gov.lk/v1/masterdata/devicespecifications


    Running Save Device Detail  
      https://aws.digitalid.lgcc.gov.lk/v1/masterdata/devices

  
    Running SignedRegisteredDevice
      https://aws.digitalid.lgcc.gov.lk/partnermanagement/v1/partners/registereddevices




### Related Tables & Queries

E.g

  Select * FROM pms.partner where id='729aaa95-d812-4285-9231-c0200a970401'

  Select id FROM regdevice.device_detail where dprovider_id='729aaa95-d812-4285-9231-c0200a970401'and make='MANTRA'and model='MATISDX'

  Select id FROM regdevice.secure_biometric_interface where device_detail_id='67a99507-5ac1-455a-8c9f-50bc3cbcb4dd'

  select * from master.device_spec where id='444' and lang_code='eng'

  Select id from master.device_master where serial_num='000003621382' and is_active='true' and lang_code='eng'

  Select code FROM regdevice.registered_device_master where device_id='1f4a6922-7040-48c5-a2f4-6879d3ae5ecd'and serial_number='000003621382'


### for comprehensive guide on Device Registration API Flow With Postman can be found from 
    Refer : https://github.com/ICTASL/UDI-poc/blob/master/mosip_device_registration/device_registration_api_setup_guide.docx	

 
 
 
 





