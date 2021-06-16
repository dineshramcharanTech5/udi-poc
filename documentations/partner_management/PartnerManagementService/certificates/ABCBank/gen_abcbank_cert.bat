keytool -genkeypair -alias abc_bank -keyalg RSA -keysize 2048 -sigalg SHA256WithRSA -dname "CN=Partner,O=ABC Bank,S=KA,C=IN" -validity 365 -keystore abc_bank.p12 -storetype PKCS12
