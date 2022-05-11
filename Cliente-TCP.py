import os
import socket
from nacl.signing import SigningKey

HOST = 'localhost'
PORT =  5789


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    f = "nuevo.txt"
    size = os.path.getsize(f)



    print("Enviando...")

    with open(f,"rb") as arc :
        cnt = arc.read(1024)
        llave_firma = SigningKey.generate()
        signed = llave_firma.sign(cnt)
        verify_key = llave_firma.verify_key
        verify_key_hex = verify_key.encode()
        s.send(verify_key_hex)
        s.send(signed.signature)
        s.send(cnt)



    print("Terminado de enviar")
    #print(s.recv(1024))
    s.close()
