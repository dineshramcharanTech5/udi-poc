from certs import readRawCertificate
from OpenSSL import crypto
import rsa
import base64

certFile="certificates\\ABCBank\\abc_bank.p12"
encdata=b"O-m-ofm2VDspFHgkB9I1_QfN1nXXIF5-Mea7puUILm74pNRqdyuSLqg3-ErvE63CX3sDKByeKGEagEkDSao6c7NBK3iJ0odRPqEFds32mD59tbYzNM6Or3911ZctXB-dlJAD6RriMUVRml1MZ2VXBU7T58j_6tVLUfi5iUjHzF5r7luQixAStSvvPglXYzUvsxvA9vpr-4QjYjCjOdzD7_xfP8xBZFc2pVztrJDITZcljWJowqpau0wlHvFWHQImDEHfm86ifiUog9czZcQY36zCPiLUR65_K_0Sw_qfPMpAOAL_TrQK25oNgSw8jfn-j8o-yHyRA9Cl2JKBF6XarSNLRVlfU1BMSVRURVIjW9jFqeFx5LHzndn_WZRtLsgA7d28217BFbJW7F_8ijZ7ShhRF3JQCuwr4_CrrgEPXXI4k_a4F9jPA3A7p13KQzh0yN77J7xCT_Xaocy_G5CuXzdOoszLPbAPDpyOBc0kupbzaEf_nIIJqNuifAINnUZIqSBzjE7gQiJcN84V4AFVswR29Q8rgUqmpvbtI1AJe9tv1-OMcCKEnDvNOAD-MSmDxiFahHYx-R5CYPiQ4stxnI13Y_p8KvMMwdWvJ4P1xRGvHl-ccAJw1eNISyLqcixc8Rsgv6cm4rNMrYQ_d_4BCRUf33xu4jHM3ujrlAeaMHJYTscDGjrnmeZEBeqeODP7p_WN4B4TmfQCS_isGrTGEHLT0wlebf-v88ZSMw9D3ANvQ0SWgKGw7dIo13Uu7yHRlWn8qutPbCWH5C0of3kiB_trrSk7nYETTIM7OMOqfLsUsh2kk8TXM30B5wNZTw46Mkyf6ObahtAjwrqc2hyFsgghWYtXtbTojBPsSjPegsOUnYjRU9aHoV3vDMqhAu4LQS1HO0LhHlOHxtLqsg"
decdata = base64.urlsafe_b64decode(encdata +  b'==' )
print(decdata)
keysplitter = bytes("#KEY_SPLITTER#","utf-8")

pos = decdata.find(keysplitter)
print(pos)
symkey = decdata[0:pos-1]
data  = decdata[ pos+ len(keysplitter)]
splitterkey = decdata[ pos: (pos + len(keysplitter))]
print(splitterkey)
certKeys = readRawCertificate(certFile)
p12 = crypto.load_pkcs12(certKeys,b"123456")
privateKey = p12.get_privatekey()
print(privateKey)
pemKey = crypto.dump_privatekey(crypto.FILETYPE_PEM,privateKey)

#key = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDAabKiCdP8UCgP\n4oWJ0HQrA/8WeixzvP+G8ifuHGEWtlaRp9RJX5pmylP8vM2XeiPcDfOpbwpWxVl6\nqFXqN/Mi1J8BafL7lzSIcg5qX2MPB7f2wDxa4tCFbMFqW67xoA7dsocvvCqfiuKr\nTjAAd5YsvhpfEBWyd3LgqM+s5RCBekYn5tIji2n+aNybFINFkPUF498AQpXxZJVB\nMz4LgtkoW+/CaPMxNEYfIIHumGpoblX6sz6Rnna65On6irDKgB68m2fs4uOWepA+\nbRAAcU9aLJeG5h6a+nrsyEfNgLOy77BEZS/BOOfCoE9wAos7znTKQKZT3oyiFgks\ndIYY0uj7AgMBAAECggEAE8JG79DmjgCFPKxcXjyj0U8FwP8m1XPRIcB4TUFozvZG\niYqciDRjHK8mVMvmqOmICS79mKaofySg/bGPsQ+xzh/bfD+vDhsG8AQWauIEwCRg\nxdwT1pl4JFt4uT1VB8cR/743l7VRAzU19bV/xGyDZXDYMG7sa3lMuLldKjoTqdgA\n6cuOomsbDxGbV90OmTPAUIq0dUdSANoi8+dzMyb1nSFAfxChrcbxatsxabR2UQHH\n9J7CcYy+KVrjmDuWUP+6LhqifIVqGJw5UvUAoOTIzK6NhFBBs6DlRMSdbhbl2cqk\nitk1twWZYnt6hPrpUinWzCrWd1t12RCn+WDksDZWEQKBgQDvWq1uJo+1NbpVBZQS\neWB0ibUWb3N2TLwdbWwsOsbvg9Xnz+U2drkTjNyWtUdaW0eYUcA8XnV5d2F5pFwy\nmg5/qvv3Cqc74lN09nZhwKeQ6hhaI00Bm97kRLVZ6vLUMHuMv2VpfhIRZGD+vE/j\nJjxMpS4m+o3N6l2pEQuw/boxtwKBgQDNy03qQ/kjsquMBEFHZtdbk5NlSROe1nu9\n+A0YQk+zn9mT/lb5uhPDWqEt6NTnXsdNqLGeJX9FnAcEMCyR8nBvc21cEhbi5BG7\nOgdu9PNLM3hZlK0ydGVs5yV8C+2BJcXVQWA4EKmZRmb9TcanSFiukral6aMDxpy4\nR4BWeKHy3QKBgQDSDIiQVuTciMb5oAie4cek3ch+ZNY15gdb58/7TKWSQebxJP+o\n+S1YG9DlrTZt9BbzdCK4l8iODRcMshF7ErlQjpPJ655xLiBBT5z6EiC7SsSOLdaB\nZ/GF70obG9V4Iwf5r2lm140xmB6KzmVpGP/n3zmOWWkiYN9K5DuXWkMRJwKBgDoE\nUtb0isxRlqNGn9CtYZFjrW4kh++DsCcCQ07PgwC00/YxAfwtRV0Rs9bpiPwhcDao\nlEptb9AECMZZfnc2zhPdirsmLmWQvp714Rqa2+wbepZmn91VizKEh8DM7Aw4xek1\nIRctO2MGwgovXw3SC45LtkpX76kk2RHqtneqUp3RAoGBALyUyawTiILFqAf3vCpR\nNhLNyHymVnRb8M71GMp0Q8U6H8D/kI/XiZha8HyDMixx8etwqRm6L0wYJXF2Y89/\naZ14kD1FmfgjNzBfXOtzqTWyiU6Bbb+HNLwYKeRYbQcoAWLgRURZjqB++FWxe52R\nuXGqOynKSrvpTSAsZZYGRoSm"
    #byteData = bytes(encrypedData, 'utf-8')
    #byteData =base64.b64decode(encrypedData)
    #fernet = Fernet()
#pemKey = str(pemKey)
#pemKey = pemKey.replace("PRIVATE","RSA PRIVATE")
#pemKey = bytes(pemKey, 'utf-8')
#pemKey =  base64.b64decode(pemKey)
#pem_prefix = '-----BEGIN RSA PRIVATE KEY-----\n'
#pem_suffix = '\n-----END RSA PRIVATE KEY-----'

#pemKey = '{}{}{}'.format(pem_prefix, key, pem_suffix)
#pemKey=bytes(pemKey,'utf-8')
#print(pemKey)
#pvtKey = rsa.PrivateKey.load_pkcs1(str(pemKey))    
    #decodedData = fernet.decrypt(encrypedData).decode()
print(symkey)
decodedData = rsa.decrypt(symkey, pemKey ).decode()
print( decodedData)
