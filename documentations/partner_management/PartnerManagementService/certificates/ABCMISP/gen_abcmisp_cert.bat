keytool -genkeypair -alias abc_misp -keyalg RSA -keysize 2048 -sigalg SHA256WithRSA -dname "CN=MISP,O=ABC MISP,S=KA,C=IN" -validity 365 -keystore abc_misp.p12 -storetype PKCS12
