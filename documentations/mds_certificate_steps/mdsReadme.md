# Steps to create and add mds certificates and build the mockMDS

We need to make sure that the MOSIP ROOT and MOSIP PMS certificates are available in MOSIP's master.ca_cert_store table. If not these needs to be added post deployment may be using a database script.

#### Steps to add the MOSIP ROOT certificate

1. Get a authentication token Request URL: POST https://testsludi.lgcc.gov.lk/v1/authmanager/authenticate/clientidsecretkey Request Body:

```
{
  "id": "string",
  "metadata": {},
  "request": {
    "appId": "ida",
    "clientId": "mosip-ida-client",
    "secretKey": "<secret>"
  },
  "requesttime": "2018-12-10T06:12:52.994Z",
  "version": "string"
}
```

2. Fetch the ROOT certificate from MOSIP's key manager API. Request URL: GET https://testsludi.lgcc.gov.lk/v1/keymanager/getCertificate?applicationId=ROOT Response:

```
{
    "id": null,
    "version": null,
    "responsetime": "2021-05-06T08:42:34.697Z",
    "metadata": null,
    "response": {
        "certificate": "-----BEGIN CERTIFICATE-----\nMIIDmjCCAoKgAwIBAgIIaKo5PFVO9QcwDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE\nBhMCSU4xCzAJBgNVBAgMAktBMRIwEAYDVQQHDAlCQU5HQUxPUkUxDTALBgNVBAoM\nBElJVEIxGjAYBgNVBAsMEU1PU0lQLVRFQ0gtQ0VOVEVSMRUwEwYDVQQDDAx3d3cu\nbW9zaXAuaW8wHhcNMjEwNDMwMTMyMjAzWhcNMjQwNDI5MTMyMjAzWjB2MQswCQYD\nVQQGEwJJTjELMAkGA1UECAwCS0ExEjAQBgNVBAcMCUJBTkdBTE9SRTENMAsGA1UE\nCgwESUlUQjEgMB4GA1UECwwXTU9TSVAtVEVDSC1DRU5URVIgKFBNUykxFTATBgNV\nBAMMDHd3dy5tb3NpcC5pbzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\nALWmQA+UlfT4n/DBUUyixUvOeH9siJa0UgcHRmYAkoVDLspPdc7lxPKcuHkQybAW\n9AMs1RFxtsF2dUEtXGpxvrP1Y4cVLxICZRJWvKlxOZ2Sj03zhqMH3hDXNtoPpEiU\nXdw3W6WSBTcdZJ2rBNk3ucV3knE4FnBLJ6P+SxFw3uB6gVwUEASJRs2JnJVdhD2H\n4bEjm/t1fpKEC1rUdmFi6ZQhjseVWSUh7Jwv4FCXieBtIL4MUs3WbkXIybytLsf6\nXHqL5JzEn0dOHKYiA9bqjlmXh8l7Z7r91E+UwCsb9lmiHlXm3g0GegRXHZwArkad\nIbNjAcTwzDHQZ+zQhKhiXjcCAwEAAaMyMDAwDwYDVR0TAQH/BAUwAwEB/zAdBgNV\nHQ4EFgQUvkXvEFHK3kJjsjPSRvEp6QRPjt4wDQYJKoZIhvcNAQELBQADggEBALiF\n5Xurad1U7SxTgviV1SeA1mInFw9jqD7y/xK/NFsPnV9Dm673u4ll2z+EqM19NeAn\nZEsIdOgWTm8+5sZDO02PksC7z96O7R/ZIL4eium1o4Mm0WdO6jhDR/4jVkvXu0PF\nU/UHSLKrS3XGRcHATAM5vWf8exla3S2OeNR+M+edSWv+2XdCpOJsFadIlFpvyHK8\nukD1iHK6GBDnMoUzCxmfyJ/kkStChDaLudoHmRokVMFrNEmvh3vyASbtNGg7du/2\n9YS2bxzpgAz99I719r/zyiXEJ5yheJKtlugvgacgwie+FFs+AZ81PTYU7T/8AJR+\n7gas1HC23MdBp4e7l0c=\n-----END CERTIFICATE-----\n",
        "certSignRequest": null,
        "issuedAt": "2021-04-30T13:22:03.000Z",
        "expiryAt": "2024-04-29T13:22:03.000Z",
        "timestamp": "2021-05-06T08:42:34.698Z"
    },
    "errors": null
}
```

3. Insert the certificate in the master.ca_cert_store table using following insert statement

```
INSERT INTO master.ca_cert_store (cert_id, cert_subject, cert_issuer, issuer_id, cert_not_before, cert_not_after, crl_uri, cert_data, cert_thumbprint, cert_serial_no, partner_domain, cr_by, cr_dtimes, upd_by, upd_dtimes, is_deleted, del_dtimes)

VALUES('f393dfb4-7361-4a7a-8ec1-690d9036cc08', 'CN=www.mosip.io,OU=MOSIP-TECH-CENTER,O=IITB,L=BANGALORE,ST=KA,C=IN', 'CN=www.mosip.io,OU=MOSIP-TECH-CENTER,O=IITB,L=BANGALORE,ST=KA,C=IN', 'f393dfb4-7361-4a7a-8ec1-690d9036cc08', '2021-04-24 20:59:33.000', '2026-04-24 20:59:33.000', NULL, '-----BEGIN CERTIFICATE-----
MIIDkzCCAnugAwIBAgIHbzkIyF4JZzANBgkqhkiG9w0BAQsFADBwMQswCQYDVQQG
EwJJTjELMAkGA1UECAwCS0ExEjAQBgNVBAcMCUJBTkdBTE9SRTENMAsGA1UECgwE
SUlUQjEaMBgGA1UECwwRTU9TSVAtVEVDSC1DRU5URVIxFTATBgNVBAMMDHd3dy5t
b3NpcC5pbzAeFw0yMTA3MDkxMzMyMDZaFw0yNjA3MDkxMzMyMDZaMHAxCzAJBgNV
BAYTAklOMQswCQYDVQQIDAJLQTESMBAGA1UEBwwJQkFOR0FMT1JFMQ0wCwYDVQQK
DARJSVRCMRowGAYDVQQLDBFNT1NJUC1URUNILUNFTlRFUjEVMBMGA1UEAwwMd3d3
Lm1vc2lwLmlvMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4KrPw0ub
FAIoybnVWSnILSp0BhDmvAo9Mvx88yiaInTpMD7UIifURHVO6QVByftIoxTbt62f
NvttWv9AzoQZPZ40l8WztOA9XCkexxal4tbVGD/m2238hAcidE40XMZl1oIy7A1p
qaqNGqjH2OTl+GkdqSDQP45sJpeADYssomta1/L3xwQxHZ6e7wJbff638WTVcf2T
0BFxElM3dl7aWG771dNCT3VqlVO57LZ34cZ3um2k+POhPFXnIOHzOfxAZcvrRpLb
MO/LWLPvCqLOP4EjPFbCM9Po4q2vscNoEs22jp9cN68KP4e6vUmISiloQqOtrdD9
f4jQlW6Bj4yAkwIDAQABozIwMDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBSm
vgQSZvcYQ4hUUufoxo6K1bksizANBgkqhkiG9w0BAQsFAAOCAQEAofcfN76qEO8v
/+ubzuLFUrlVwOMlJPdunVoGuQsFnaaSYEaUN5Pyq3tgjT2qArk7zSjnOI2zg3S2
kdHgIyLAmlkzjeAFNisH7wwxC0XKGHOHkjf910hW8tYIAvaUC9WS/3uT2gZ0GExF
NFeOGLJrz266ne7W4m6AclAD9LwEIc5k2dPQipXBAyqv/mzWpp23tJufJIdBJS4R
UPZcgghObYIlJvJQ+IJuCykC0pEA7im0hhDeTeDU6CqNqB/ZYQm/Jedwf8SZwThN
BON+LRNKwMqJ6ra8Ar6RFf68TUaGGta0FvxelS02XqexyIGh/iApX//Z5Yb97xeO
zpylrqMd8Q==
-----END CERTIFICATE-----
', 'fef34d3ed7c2025be31c6ff5406db8941a2d9ed3', '31306432299010407', 'DEVICE', 'SYSTEM', '2021-04-29 23:41:59.696', NULL, NULL, false, NULL);
```

The cert_subject and cert_issuer should be the same for the root certificate.

Retrieve the thumbprint and serial no by saving the certificate data as a .cer file.

The cert_id (randomly generated) and issuer_id is also the same for the root certificate

#### Steps to add the MOSIP PMS certificate

1. Get a authentication token same as before.

2. Fetch the PMS certificate from MOSIP's key manager API. Request URL: GET https://testsludi.lgcc.gov.lk/v1/keymanager/getCertificate?applicationId=PMS Response:

```
{
    "id": null,
    "version": null,
    "responsetime": "2021-05-06T08:42:34.697Z",
    "metadata": null,
    "response": {
        "certificate": "-----BEGIN CERTIFICATE-----\nMIIDmjCCAoKgAwIBAgIIaKo5PFVO9QcwDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE\nBhMCSU4xCzAJBgNVBAgMAktBMRIwEAYDVQQHDAlCQU5HQUxPUkUxDTALBgNVBAoM\nBElJVEIxGjAYBgNVBAsMEU1PU0lQLVRFQ0gtQ0VOVEVSMRUwEwYDVQQDDAx3d3cu\nbW9zaXAuaW8wHhcNMjEwNDMwMTMyMjAzWhcNMjQwNDI5MTMyMjAzWjB2MQswCQYD\nVQQGEwJJTjELMAkGA1UECAwCS0ExEjAQBgNVBAcMCUJBTkdBTE9SRTENMAsGA1UE\nCgwESUlUQjEgMB4GA1UECwwXTU9TSVAtVEVDSC1DRU5URVIgKFBNUykxFTATBgNV\nBAMMDHd3dy5tb3NpcC5pbzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\nALWmQA+UlfT4n/DBUUyixUvOeH9siJa0UgcHRmYAkoVDLspPdc7lxPKcuHkQybAW\n9AMs1RFxtsF2dUEtXGpxvrP1Y4cVLxICZRJWvKlxOZ2Sj03zhqMH3hDXNtoPpEiU\nXdw3W6WSBTcdZJ2rBNk3ucV3knE4FnBLJ6P+SxFw3uB6gVwUEASJRs2JnJVdhD2H\n4bEjm/t1fpKEC1rUdmFi6ZQhjseVWSUh7Jwv4FCXieBtIL4MUs3WbkXIybytLsf6\nXHqL5JzEn0dOHKYiA9bqjlmXh8l7Z7r91E+UwCsb9lmiHlXm3g0GegRXHZwArkad\nIbNjAcTwzDHQZ+zQhKhiXjcCAwEAAaMyMDAwDwYDVR0TAQH/BAUwAwEB/zAdBgNV\nHQ4EFgQUvkXvEFHK3kJjsjPSRvEp6QRPjt4wDQYJKoZIhvcNAQELBQADggEBALiF\n5Xurad1U7SxTgviV1SeA1mInFw9jqD7y/xK/NFsPnV9Dm673u4ll2z+EqM19NeAn\nZEsIdOgWTm8+5sZDO02PksC7z96O7R/ZIL4eium1o4Mm0WdO6jhDR/4jVkvXu0PF\nU/UHSLKrS3XGRcHATAM5vWf8exla3S2OeNR+M+edSWv+2XdCpOJsFadIlFpvyHK8\nukD1iHK6GBDnMoUzCxmfyJ/kkStChDaLudoHmRokVMFrNEmvh3vyASbtNGg7du/2\n9YS2bxzpgAz99I719r/zyiXEJ5yheJKtlugvgacgwie+FFs+AZ81PTYU7T/8AJR+\n7gas1HC23MdBp4e7l0c=\n-----END CERTIFICATE-----\n",
        "certSignRequest": null,
        "issuedAt": "2021-04-30T13:22:03.000Z",
        "expiryAt": "2024-04-29T13:22:03.000Z",
        "timestamp": "2021-05-06T08:42:34.698Z"
    },
    "errors": null
}
```

3. Insert the certificate in the master.ca_cert_store table using following insert statement

```
INSERT INTO master.ca_cert_store (cert_id, cert_subject, cert_issuer, issuer_id, cert_not_before, cert_not_after, crl_uri, cert_data, cert_thumbprint, cert_serial_no, partner_domain, cr_by, cr_dtimes, upd_by, upd_dtimes, is_deleted, del_dtimes)

VALUES('ab6466be-b0db-4104-9fdc-8fb84880598a', 'CN=www.mosip.io,OU=MOSIP-TECH-CENTER (PMS),O=IITB,L=BANGALORE,ST=KA,C=IN', 'CN=www.mosip.io,OU=MOSIP-TECH-CENTER,O=IITB,L=BANGALORE,ST=KA,C=IN', 'f393dfb4-7361-4a7a-8ec1-690d9036cc08', '2021-04-24 21:04:32.000', '2024-04-23 21:04:32.000', NULL, '-----BEGIN CERTIFICATE-----
MIIDmjCCAoKgAwIBAgIIUNrEvJ3qg50wDQYJKoZIhvcNAQELBQAwcDELMAkGA1UE
BhMCSU4xCzAJBgNVBAgMAktBMRIwEAYDVQQHDAlCQU5HQUxPUkUxDTALBgNVBAoM
BElJVEIxGjAYBgNVBAsMEU1PU0lQLVRFQ0gtQ0VOVEVSMRUwEwYDVQQDDAx3d3cu
bW9zaXAuaW8wHhcNMjEwNzA5MTMzMjUyWhcNMjQwNzA4MTMzMjUyWjB2MQswCQYD
VQQGEwJJTjELMAkGA1UECAwCS0ExEjAQBgNVBAcMCUJBTkdBTE9SRTENMAsGA1UE
CgwESUlUQjEgMB4GA1UECwwXTU9TSVAtVEVDSC1DRU5URVIgKFBNUykxFTATBgNV
BAMMDHd3dy5tb3NpcC5pbzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
AK6wcz07grCxwE4R9pRZyt6L276n4GZs6slTspj6LlbmHDTXwL2mCSw2LTOuTKxO
K0/+ri81CHhdWsvvSRh79Q4ZTFxSoeLTmrzwpIM3Ze+RqPyvRXa+zfsGDAxOEl0E
kGNuEL/O6VzOsuJc28NyD3ezAo9rvV4OfnI5VmU7gTFqgtJUwogvQZu0/IiH+IXr
5uxlBLCWA50TDZp8zP6CTcMUoN+RnVqh+ON/PlzPVz7WbrnRl9lZEZelViygNJKJ
zl1tzs7YNMNI79Y4yCpitPxY9R7FKkNVPQmWICc2NFEHzWs2BL/omctXXwCS3bfy
YFgTEsUD14tS63ZohD3WFGsCAwEAAaMyMDAwDwYDVR0TAQH/BAUwAwEB/zAdBgNV
HQ4EFgQU2Z68UyamGM+1lnddzJp7BTvVtTIwDQYJKoZIhvcNAQELBQADggEBAIdh
uoVqtlcPg5oeB4A1YmahZ8J0dbvniuEvzxil+JSs6VvuLz4tnPsqhsPCMioZKAiw
c6kCq92tp/7UKTUmJV9yd3m5sPZ9/XZXhSfY8ZPbz2dATrkkyqdPCBrtiWoJlmrU
i/zyrRujXkUMpqlq/iC3ILH6k808YKv17R35iyoJM3sC+ucSKsXH+/vrMd+Ga2qe
ZqPZzyIh9kc2czCdKrNMfyka9TH4hnKvBa6EJIViP/1TgjZICe4wQuJLsGHBHbYR
R2Df0+6S4CvivmQuCY5sufQMFY71lz9pGsupOwmld/h0RWOKeS2XYik6G4vx5Kue
3WC2bM8tzKm5U1CGCdI=
-----END CERTIFICATE-----
', 'e7df1de3abda64c7ecc4614cf0402fabafd3f128', '5826185382339445661', 'DEVICE', 'SYSTEM', '2021-04-29 23:47:05.275', NULL, NULL, false, NULL);
```

The cert_issuer should contain the cert_subject details of root certificate.

Retrieve the thumbprint and serial no by saving the certificate data as a .cer file.

The issuer_id should be the same as the cert_id of the root certificate

#### Device certificate upload steps

The attachment here CA_CERT_UTILITY is a certificate creation utility that uses shell script commands being executed sequentially to generate valid certificates. For linux machine running the script is easy but for windows machine will need the git being installed or need the openssl application installed in the machine.

1. Authenticate yourself using swagger first.

2. Go to https://testsludi.lgcc.gov.lk/v1/partnermanager/swagger-ui.html#/Partner%20Service%20Controller/partnerSelfRegistrationUsingPOST and create a partner using below request.

```
{
  "id": "string",
  "metadata": {},
  "request": {
    "address": "sri lanka",
    "contactNumber": "0777123456",
    "emailId": "icta@gmail.com",
    "organizationName": "slmds",
    "partnerId": "slmds",
    "partnerType": "Device_Provider",
    "policyGroup": ""
  },
  "requesttime": "2018-12-10T06:12:52.994Z",
  "version": "string"
}
```

3. -Run the “create-certs.sh” in the CA_CERT_UTILITY and create the CA,SUBCA and Partner certificates (Use the same name used to create the partner tpo create the partner certificate), 3 ceretificates will be created in this directory.

4. Go to https://testsludi.lgcc.gov.lk/v1/partnermanager/swagger-ui.html#/Partner%20Service%20Controller/uploadCACertificateUsingPOST and upload the RootCA.crt (copy the contents inside) certificate using below request.

```
{
  "id": "string",
  "metadata": {},
  "request": {
    "certificateData": "-----BEGIN CERTIFICATE-----\r\nMIIF3zCCA8egAwIBAgIBATANBgkqhkiG9w0BAQsFADB9MQswCQYDVQQGEwJTTDEQ\r\nMA4GA1UECAwHV0VTVEVSTjEQMA4GA1UEBwwHQ09MT01CTzENMAsGA1UECgwEU0xD\r\nQTENMAsGA1UECwwEU0xDQTENMAsGA1UEAwwEU0xDQTEdMBsGCSqGSIb3DQEJARYO\r\naWN0YUBnbWFpbC5jb20wHhcNMjEwNzEzMDczNzI1WhcNMjQwNDA4MDczNzI1WjCB\r\ngDELMAkGA1UEBhMCU0wxEDAOBgNVBAgMB1dFU1RFUk4xEDAOBgNVBAcMB0NPTE9N\r\nQk8xDjAMBgNVBAoMBVNMU0NBMQ4wDAYDVQQLDAVTTFNDQTEOMAwGA1UEAwwFU0xT\r\nQ0ExHTAbBgkqhkiG9w0BCQEWDmljdGFAZ21haWwuY29tMIICIjANBgkqhkiG9w0B\r\nAQEFAAOCAg8AMIICCgKCAgEAu9waVA6PTwCc4bxiu2YJ\/f6N72m+ognGz0t\/Ppy1\r\nTt1pxaRm9tND9CJGcDl5bt67K+8UrlhcTNNKOC8iOkKwP1zjY\/YbbPrKIrcHzES3\r\n72T\/JdXqGOfIh1JDvX2bcN5yRLf6Wq1ozdtSsBLbnKfudhsHi\/cYXDZNKFf22O9o\r\nIV7SoGk8TVhXzWpie23oNKTVoEvLgczS8lwgqXPvNox7ZVV0Y9gOM2WlCT99SGuf\r\nBvStmGkazm9gieLwMLXIPTw6oj1Ympj\/rVeFNBk\/KT1BGA3huDLWNSfcb1uyRXsK\r\neTQaqEJ+NARvD\/yOL0owMLBRZYutw2ZQsxZxKGlGDVo2ZFRnoeE3ppWNgFwcMtbW\r\nX2PNsSKNV0xD+ssSTh073\/EvPqb9SkJMW2Pn5fuSWzS+5z23Hj7qUVqIBLCz6D2K\r\nya7Hb8+J+SEdGTjzTrSdUJSU7HjucD7G\/YC3fXz+\/Vq9noYGtyGSbkgJBhsOVSo9\r\nln41AmZvES8qxaB19qlM40qO4P6JgBYoxMiqihT0XZZSfcPIAdGHQKSWw5EWDb5s\r\nos52R4wE0kCjj8O\/RazxWLV2TIxG9HJyHqrmfiY9ATuUYQLn89rFR7hqVAwAX39w\r\nekynnRBVbVquL3h3tshyWLKHm+hnOzANWRBImGVhOUVuSYJRWOCt6vY5stZC4CAk\r\nDZ0CAwEAAaNmMGQwHQYDVR0OBBYEFOPNxa8yjLM58SRZgClwo6wlJuvzMB8GA1Ud\r\nIwQYMBaAFPnXpRGBYTBRdqfqHvYm3Lxdf3P5MBIGA1UdEwEB\/wQIMAYBAf8CAQAw\r\nDgYDVR0PAQH\/BAQDAgGGMA0GCSqGSIb3DQEBCwUAA4ICAQAUu+bn5GimLOQr9kra\r\nKGk6XOY+zPy8gLxVcqCHauQeHv2bjPMwypkDhjFLNMaiWY5ELdgbbpGWYCUw5o8m\r\nDdv6IaGyuBZ9BaDR6GzbixJ2eQZu+xh7nt9HGRQVX2XkJS6uL2Gxx8fceZffyKMp\r\naLsRc0MMIcEpj2nuYVbrDR03ZEbwv\/dKKJ+pDIooS0gbFrFsYxHjFI1oEUVhHnSQ\r\nKDs0UmTau7Lgx4z8e7rUI6JFA9EzdeUghmrM2KjFDbnmwLTLVAa1QykpCZwD650o\r\n1yzZXmvO2hgHAyhQqLluhCGPr2svgroAEvmdHX3TsC6F2Vz1I6\/7pzu5V8+Q\/iJZ\r\n6lL7bTtL\/WcXCYTNw8CJ4GhA\/1BGo3zPk8CSO9LlSdrBwCeg5jV2p0yJxmuNed3\/\r\nBDsb5n+TdWC2IYPqGXVcTclj+w4V4VRqb6AzEH+eieMusJ8BsyyhewAhlapnKKHi\r\nh2rboZQ3WtKKwB1dlHLpp1ViUSAJTC5a\/Ih7ZhdanJ4V7isCn4xZsuAEfZuoHyMR\r\nXmsqzGqklcGVB\/UMfY4mIJJfF8n5sp5TZIJ4qA1WT17L0\/zQVP4Rn3YPPRrJDlKy\r\nEqBcTgGYJkfMv5ROJnZY44LiuXlsQ80moh7GtVg74XYo7mSUAjRequ\/n4XKp\/dlq\r\n6R3r34gY\/9pD1rd8u2cpWPsw7Q==\r\n-----END CERTIFICATE-----\r\n",
    "partnerDomain": "DEVICE"
  },
  "requesttime": "2018-12-10T06:12:52.994Z",
  "version": "string"
}
```

5. Repeat above step for the IntermediateCA.crt.

6. Go to https://testsludi.lgcc.gov.lk/v1/partnermanager/swagger-ui.html#/Partner%20Service%20Controller/uploadPartnerCertificateUsingPOST_1 and upload the contents of the Client.crt using the below request.

```
{
  "id": "string",
  "metadata": {},
  "request": {
    "certificateData": "-----BEGIN CERTIFICATE-----\r\nMIIGQzCCBCugAwIBAgIBBDANBgkqhkiG9w0BAQsFADCBgDELMAkGA1UEBhMCU0wx\r\nEDAOBgNVBAgMB1dFU1RFUk4xEDAOBgNVBAcMB0NPTE9NQk8xDjAMBgNVBAoMBVNM\r\nU0NBMQ4wDAYDVQQLDAVTTFNDQTEOMAwGA1UEAwwFU0xTQ0ExHTAbBgkqhkiG9w0B\r\nCQEWDmljdGFAZ21haWwuY29tMB4XDTIxMDcxMzA3MzgxMFoXDTI0MDQwODA3Mzgx\r\nMFowgYAxCzAJBgNVBAYTAlNMMRAwDgYDVQQIDAdXRVNURVJOMRAwDgYDVQQHDAdD\r\nT0xPTUJPMQ4wDAYDVQQKDAVzbG1kczEOMAwGA1UECwwFc2xtZHMxDjAMBgNVBAMM\r\nBXNsbWRzMR0wGwYJKoZIhvcNAQkBFg5pY3RhQGdtYWlsLmNvbTCCAiIwDQYJKoZI\r\nhvcNAQEBBQADggIPADCCAgoCggIBAPaVLVJrc9RrLUwBAp9awKj6tGzjhtp4Wflj\r\nYUCBitY80kJx+Fpyvh7oKWSwQLjvB8BR7oxQvG4NLtcZsGbwQqupcLhSAW8UJ\/oU\r\nF9BAD8VuiSNLcmj3YcL\/gFBkYKSqQw9gW1zXbEmPr6NpVAtiG9oPPu0ySskoto\/B\r\nizaGAinNJKo+oXVvWGZdix38W6gTd46Sz3I3cjXJcOymly\/ccItkdRVbU7FwKGrR\r\n+BKBoddlAq8FCW4QPUR0PfuMUwYuCOREQdRSCA6SLZLbmjdVEPklfouxwMPDxlUS\r\nhx91ZP6EoRorG9ptRMet1G8ZhMrN+ptRDGLWZ0Cc3DdxV\/oN3gFLfbyFQ\/MAS3dT\r\ntBGdEdOIX3PvgnjBQ0y571ORGzJLiyE\/bjpZjquo+xZKrR9FxMMwLrfXW\/dHW20T\r\nDw5ZZIGLz\/Y+eob5fC3eJI6BrGrWI648P08\/98IqalCijso97X4kBuBRrPJ\/S60j\r\nj4uRgXuhERV3W5wO3sj8zJD0ZRaP0rni3aShcw9oWcAvnSqpkVxQkIGo73sqG2Ql\r\nmU0\/G1wwzu2w1KFlBephHXyQjVvFND7DjzwrDLawoj23RdpRFqPqkAU28Ne+v0Tw\r\n3ClJ\/FyZYkC8A3IBf2c7dmQUtvys9g0xlZ5L4piiIrPrfl2Ug5tOS2P51VDECtN4\r\nuKLwerT3AgMBAAGjgcUwgcIwCQYDVR0TBAIwADARBglghkgBhvhCAQEEBAMCBaAw\r\nMwYJYIZIAYb4QgENBCYWJE9wZW5TU0wgR2VuZXJhdGVkIENsaWVudCBDZXJ0aWZp\r\nY2F0ZTAdBgNVHQ4EFgQUctR0wYmPDGgIYWBHgZ6glf2P5powHwYDVR0jBBgwFoAU\r\n483FrzKMsznxJFmAKXCjrCUm6\/MwDgYDVR0PAQH\/BAQDAgXgMB0GA1UdJQQWMBQG\r\nCCsGAQUFBwMCBggrBgEFBQcDBDANBgkqhkiG9w0BAQsFAAOCAgEACN8h7ahgFwGT\r\nY9WWN\/PZgpyxLlvDs6ULpyzL8jmCfy63+ZNREgPI8rnxGVCRAU6QStb3k2rv+QoW\r\naklQn83L5DpIPT9BYvh5RjDO2Tlz49t6L3YhnEUqNtTwG53wbOZYes11LzQnHQes\r\nGuCa9HLKP0+dD2gtNCkRtP5MnrTXxFW6soY\/mXpeqLi7BhlxDB+ceHEvxgpWmNNT\r\n7wlMD+72bI1VxHiC9uLabNrmp\/8yEXJ17u1YM97Xv\/nmvenuHIJXgrUshaiowQUX\r\njUwRmaPmf9SoimALM5TwWMO9IglFNAQeRDEgPNzjgSBIlSFikaXJhIBt7XZVKaft\r\neCqimjY4VfWb\/4co33Vo7aOmmZTb5xqFd9lji15CAikIrGakbR\/7+Gm1Bm6VLHBL\r\nGiFfUhPP5sxNMTJ\/GjZ+p+elIcOEyd17I65Izjc\/mPpDLJl06RigdbiV+bWBdCqD\r\nhHaZB0gevtQa\/S3+4tqQIjXI8V\/mj1ZPE6Tym7F+EvD4MaMjQFk+fnsZoQsttCR8\r\nEt3z0wL8eFtR3W4GoSN\/\/OlzpQ7p\/AE+yZXnL02bN9kOEuAcgRZsbvYNWEhhLZXf\r\nLLu8\/hNpsUxElUar4kjd9qEPW17KSP19EJWPom6YGyMso5JLgR+VumV6ZcGuOiwk\r\nK8nuMweU8f2lAfFK4Y0tX1nGr7VCzi4=\r\n-----END CERTIFICATE-----\r\n",
    "partnerDomain": "DEVICE",
    "partnerId": "slmds"
  },
  "requesttime": "2018-12-10T06:12:52.994Z",
  "version": "string"
}
```

7. In the response body of the above request you will get a signedCertificateData. Save the ceretificate data as “mosip-signed.crt” in the same directory.

8. If in linux or Mac. next run the “create-device-keystore.sh” within the CA_CERT_UTILITY folder.

9. If in Windows open C:\Program Files\Git\usr\bin\openssl.exe and execute the commands in the create-device-keystore.sh file, remember to change the file paths of the input files (openssl.conf, mosip-signet.crt and Client.key), remember the export password that you enter in this step.

10. Device.p12 and signed-device.crt will be created in the openssl directory.

#### Mock MDS build

1. Download the latest mock MDS .zip from https://github.com/mosip/mosip-mock-services/tree/master

2. Add the Device.p12 and signed-device.crt files to MockMDS/Biometric Devices/Face/Keys, MockMDS/Biometric Devices/Iris/Double/Keys, MockMDS/Biometric Devices/Finger/Slap/Keys

3. Update the application.property file as below after placing the certificates in the above paths.

```
mosip.mock.sbi.file.face.keys.keystorefilename=/Biometric Devices/Face/Keys/Device.p12
mosip.mock.sbi.file.face.keys.keyalias=device
mosip.mock.sbi.file.face.keys.keystorepwd=mosipface
mosip.mock.sbi.file.face.keys.encryption=/Biometric Devices/Face/Keys/signed-Device.crt

mosip.mock.sbi.file.finger.slap.keys.keystorefilename=/Biometric Devices/Finger/Slap/Keys/Device.p12
mosip.mock.sbi.file.finger.slap.keys.keyalias=device
mosip.mock.sbi.file.finger.slap.keys.keystorepwd=mosipface
mosip.mock.sbi.file.finger.slap.keys.encryption=/Biometric Devices/Finger/Slap/Keys/signed-Device.crt

mosip.mock.sbi.file.iris.double.keys.keystorefilename=/Biometric Devices/Iris/Double/Keys/Device.p12
mosip.mock.sbi.file.iris.double.keys.keyalias=device
mosip.mock.sbi.file.iris.double.keys.keystorepwd=mosipface
mosip.mock.sbi.file.iris.double.keys.encryption=/Biometric Devices/Iris/Double/Keys/signed-Device.crt
```

4. Run mvn clean install in MockMDS directory

5. Run the run.bat file inside the target folder to run the MockMDS

6. Restart the reg client as well (delete db and .mosipkeys)
