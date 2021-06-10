# Restarting Kafka

Follow the below steps to restart Kafka in console

1. Delete Kafka using helm
    ```helm1 delete kafka```

2. Get pvc 
    ```kc1 get pvc | grep kafka```
3. Delete all under the above get

    ```kc1 delete pvc <pvc id>```
    
4. Get pv
    ```kc1 get pv | grep kafka```

5. Delete everything in the above list 
    ```kc1 delete pv <pv id>```

6. Go to mosip section in local
    ``` 
    cd /srv/nfs/mosip/ 
    ```
7. Remove all of kafka related persistence

    ```sudo rm -rf default-data-kafka-*```
8. Install the relevant kafka back
    ```
    an playbooks/mzkafka.yml
    ```
    
> The above mentioned one is for mz and it can be done for dmz which will replace mz with dmz and kc1 to kc2