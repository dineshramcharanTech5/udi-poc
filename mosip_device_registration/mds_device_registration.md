### Bio-Metrices Device Set up ( Dual IRIS & Fingerprint Devic)

1. Set up following device drivers  as in 1.1 to 1.3


MDS for Enrollment Device(L0) Setups

1.1     MATISX Driver Setup (Dual IRIS) 
         - MATISXDriver.zip

1.2     MORPHS60 Driver Setup (Fingerprint Device - Ten print)
        - MORPHS60Driver.zip

1.3     MDS Setup 
        - Mantra_MDS_2.0.6_Spec_0.9.5.zip

1.4     MDS User Manual 
          - Refer Mantra_MDS_L0_Manual_Windows.pdf 

1.5      MDT Testing Kit Url
          http://test.mosip.io/phase2/run


### 2. Set up client utility as below


Please find the Steps to run DeviceRegisterAndDeRegister utility using any IDE

 1.     Import the project mds-testing-kit/mosip-device-reg/DeviceRegisterAndDeRegister  into IDE

 2.     Check/put your login credential  in DeviceRegisterAndDeRegister\src\main\resources\commonData.properties

 3.     Check environment related files here DeviceRegisterAndDeRegister\src\main\resources\dbFiles

 4.     Check provider details or prerequisite data to run the application here  DeviceRegisterAndDeRegister\dataFolder\deviceData.csv

 5.     Go to Runner.java class (DeviceRegisterAndDeRegister\src\main\java\com\mosip\io\Runner.java) right click on class and click on java application select run as run         configuration.

 6.     Give the vm arumgent -Dtype=<Finger -Denv.user=<dev -DbaseUrl=<https://dev.mosip.net

 7.     vm arumgent -Dtype values can be either Finger,Face,Iris and Auth or All (to run all types at one-shot)

 8.     After running deviceRegistration steps at last we can see option for de-registration of devices like

  
    Do want to de-register the device  press Y/N  Press Y for de-register the deivce  or

    Press N to exit the program execution.

 9.     Logs can be found here DeviceRegisterAndDeRegister\testRun\logs.



 ### Data to be inserted In Eclipse

 *Fields*

 *Value can be fetched from below*

 deviceId

 Random

 deviceCode

 Random

 purpose

 MDS

 serviceVersion

 MDS

 deviceSubId

 MDS

 firmware

 MDS

 deviceStatus

 MDS

 env

 MDS

 certification

 MDS

 callbackId

 MDS

 serialNo

 MDS

 make

 MDS

 model

 MDS

 type

 MDS

 deviceSubType

 MDS

 deviceProvider

 MDS

 deviceProviderId

 MDS

 name

 MDS

 description

 Modality based decscription

 deviceTypeCode

 master.device_type DBTable

 zoneCode

 master.zone DBTable

 regCenterId

 master.reg_center DBTable

 policyGroup

 pms_policy DBTable

 partnerType

 pms_partner DBTable
