# warning: do not use the certificates produced by this tool in production. This is for testing purposes only

# certificate authority
echo "==================== Creating CA certificate"
openssl genrsa -out RootCA.key 4096
openssl req -new -x509 -days 1826 -extensions v3_ca -key RootCA.key -out RootCA.crt
openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt -in RootCA.key -out RootCA.key.pkcs8


# intermediate CA
echo "==================== Creating Intermediate CA certificate"
openssl genrsa -out IntermediateCA.key 4096
openssl req -new -key IntermediateCA.key -out IntermediateCA.csr
openssl x509 -req -days 1000 -extfile ./openssl.cnf -extensions v3_intermediate_ca -in IntermediateCA.csr -CA RootCA.crt -CAkey RootCA.key -out IntermediateCA.crt -set_serial 01
openssl verify -CAfile RootCA.crt IntermediateCA.crt
openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt -in IntermediateCA.key -out IntermediateCA.key.pkcs8


# client certificate from IntermediateCA
echo "==================== Creating Device Provider certificate"
openssl genrsa -out Client.key 4096
openssl req -new -key Client.key -out Client.csr
openssl x509 -req -extensions usr_cert -extfile ./openssl.cnf -days 1000 -in Client.csr -CA IntermediateCA.crt -CAkey IntermediateCA.key -set_serial 04 -out Client.crt
openssl verify -CAfile RootCA.crt -untrusted IntermediateCA.crt Client.crt
openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt -in Client.key -out Client.key.pkcs8