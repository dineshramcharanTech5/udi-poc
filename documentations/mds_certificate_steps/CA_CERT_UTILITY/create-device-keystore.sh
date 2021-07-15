# Device key
echo "==================== Creating Device keys and export to keystore"
echo "Note: mosip-signed-client.crt is the certificate issued by mosip after successful onboard of device provider"
openssl genrsa -out Device.key 4096
openssl req -new -key Device.key -out Device.csr
openssl x509 -req -extensions usr_cert -extfile ./openssl.cnf -days 30 -in Device.csr -CA mosip-signed.crt -CAkey Client.key -set_serial 05 -out signed-Device.crt
openssl pkcs12 -export -in signed-Device.crt -inkey Device.key -out Device.p12 -name "Device"