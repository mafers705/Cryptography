import socket
import Aleatorios
from Crypto.Cipher import AES
from nacl.signing import VerifyKey


HOST = "127.0.0.1"
PORT = 5789
r = open("nuevo.txt",'rb')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Está conectado {addr}")
        key_bytes = conn.recv(32)
        sign = conn.recv(64)
        verifykey = VerifyKey(key_bytes)
        data = conn.recv(1024)
        while (data):
            print("Recibiendo...")
            verifykey.verify(r.read(),sign)
            data = conn.recv(1024)

        #with open("hola.txt",'rb') as file:
        #    verifykey.verify(file.read(),sign)

        with open("./enviados/"+"nuevo.txt","wb") as arc :
            filecont = conn.recv(1024)
            key = Aleatorios.aleatorio()
            cifrado = AES.new(key, AES.MODE_EAX)
            textocifrado, tag = cifrado.encrypt_and_digest(filecont)
            arc.write(textocifrado)

        r.close()
        print("Terminado")
        conn.close()
