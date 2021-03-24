# Adding machine to mosip

Inorder to get few auto generated keys need to run a utility file. Download the tpm utility file using this link and follow the following steps : 
 1. Extract the zip file
 2. Run ``` java -jar tpmutility-0.0.2.jar ```
You will get an output like following : 
``` 
{"machineName" : "S540-14IWL", "publicKey" : "AAEACwACAHIAIINxl2dEhLP4GpDMjUal1yT9UtduBlILZPKh2hszFGmqABAAFwALCAAAAQABAQDiSa_AdVmDrj-ypFywexe_eSaSsrIoO5Ns0jp7niMu4hiFIwsFT7yWx2aQUQcdX5OjyXjv_XJctGxFcphLXke5fwAoW6BsbeM__1Mlhq9YvdMKlwMjhKcd-7MHHAXPUKGVmMjIJe6kWwUWh7FaZyu5hDymM5MJyYZRxz5fRos_N9ykiBxjWKZK06ZpIYI6Tj9rUNZ6HAdbJH2RmBHuO0knpbXdB-lnnVhvArAt3KWoyH3YzodHeOLJRe_Y8a-p8zRZb5h1tqlcLgshpNAqb-WJgyq2xDb0RJwzuyjjHPmJrDqlBMXHestz-ADRwXQL44iVb84LcuMbQTQ1hGcawtBj", "signingPublicKey": "AAEABAAEAHIAAAAQABQACwgAAAEAAQEAw6CuS_sekZ02Z9_N3zz1fK_V3wm01PBcFM0nURerczjO2wqIxfmXpQQql3_S819nj_MwtkZ8K2ja0MRUJzJrmmbgBreFIGTa7Zhl9uAdzKghAA5hEaXV1YcxIl8m72vZpVX_dgqYzU8dccfRChsA-FxkVe5DCr_aXjVOUHjeXZRhQ1k-d7LzpBPVz-S69rx6W3bbxaZfV25HM93Hfm5P4aarYy0Wt0fJvv-Lmbyt0SIZFOQkYS8coW0-u8OiXm3Jur2Q8pu16q4F-Qpxqym-ACBFIsbkSCngQ_y4zGniK7WnS-dCSVhC-x1NscCq3PyXhoJOjSOdNqUkDX606Ic3SQ", "keyIndex": "BD:11:54:33:44:F9:5A:0B:B5:A6:B3:C1:F7:A8:28:47:0E:AA:20:21:01:16:37:89:D1:9C:8D:EC:96:5D:F5:A6", "signingKeyIndex": "41:EB:7E:7F:4F:A9:24:55:4C:5F:AB:3A:94:81:CF:75:C2:0B:92:DF:9B:89:47:D1:AD:B0:84:7A:F7:65:6A:88"}
```

After you have the keys generated populate the machine csv files located in here.
1. Open machine_master.csv
Edit the following fields : 

| Column        | Explaination           |
| ------------- |:-------------:|
| ID       | This should be a unique id based on database indexing. Check the machine master table and give an increment number from the previous index.
| Name |Give the name of your pc/laptop |
|MAC Address      | Get the mac Address of your pc/laptop      |
| serialNumber | Get the serial number of your pc/laptop      |
| IP Address | Get the IP Address of your pc/laptop      |
| validityDateTime | This will tell from when the machine is effective in the system.      |
| machineSpecId | For now let it be as 1001. Later we can add machine spec and change accordingly.      |
| publicKey | This will be generated with the tpm utility.    |
| zoneCode | Give the zone where the machine gets installed.      |
| regCenterId | Give the registration center where the machine will be installed.      |
| langCode | This will bind the machine to accommodate  language.     |
| isActive | This will make the machine active or not.    |
| keyIndex | This will be generated with the tpm utility.     |
| signPublicKey |This will be generated with the tpm utility.     |
| signKeyIndex | This will be generated with the tpm utility.   |

2. Open master_machine_h.csv
 Edit the following : 

| Column        | Explaination           |
| ------------- |:-------------:|
| ID       | This should be a unique id based on database indexing. Check the machine master table and give an increment number from the previous index.
| Name |Give the name of your pc/laptop |
|MAC Address      | Get the mac Address of your pc/laptop      |
| serialNumber | Get the serial number of your pc/laptop      |
| IP Address | Get the IP Address of your pc/laptop      |
| validityDateTime | This will tell from when the machine is effective in the system.      |
| machineSpecId | For now let it be as 1001. Later we can add machine spec and change accordingly.      |
| publicKey | This will be generated with the tpm utility.    |
| zoneCode | Give the zone where the machine gets installed.      |
| regCenterId | Give the registration center where the machine will be installed.      |
| langCode | This will bind the machine to accommodate  language.     |
| isActive | This will make the machine active or not.    |
| keyIndex | This will be generated with the tpm utility.     |
| signPublicKey |This will be generated with the tpm utility.     |
| signKeyIndex | This will be generated with the tpm utility.   |
| effectDateTime | This is a must in all the history files. Make sure you have a similar format as 2018-12-10T06:12:52.994Z. |

                                   
                               
Once you have populated the csvs login to admin in https://aws.digitalid.lgcc.gov.lk/admin-ui. 

Navigate to Bulk Upload
![Bulk Upload](https://github.com/ICTASL/UDI-poc/blob/master/documentations/local_setup_guide/registration_client/standalone/masterUpload.JPG)


Click on upload data
![Upload File](https://github.com/ICTASL/UDI-poc/blob/master/documentations/local_setup_guide/registration_client/standalone/uploadFile.JPG)


Select insert operation and select machine table and choose your machine_master.csv file.
Once upload is successful do the same for machine history. 
