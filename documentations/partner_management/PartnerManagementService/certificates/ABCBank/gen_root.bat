REM passwrd:123456
keytool -genkeypair -alias root_tiger_ca -keyalg RSA -keysize 2048 -sigalg SHA256WithRSA -dname "CN=ROOT-CA,O=Tiger,S=KA,C=IN" -validity 1095 -keystore root_tiger_ca.p12 -storetype PKCS12
