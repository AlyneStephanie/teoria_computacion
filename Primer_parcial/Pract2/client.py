# Importamos socket al igual que con el servidor; sin embargo, su configuración será diferente
import socket
import random
from common import *


def make_list():

    # Deben ser 64 caracteres
    largo_cadena = 4
    # Deben ser 1_000_000 de cadenas
    num_cadenas = 10

    for i in range(num_cadenas):
       s = bin(random.randint(0, (2**largo_cadena) - 1))[2:].zfill(largo_cadena)
       yield str(s)


def main():
    # Generamos un nuevo objeto
    client = socket.socket()

    # Hacemos la conexión
    # connect() va a recibir una tupla, y esta tupla va a contener dos valores: 1.- la dirección a la que nos tenemos que conectar, 2.- el puerto al que nos vamos a conectar. En el servidor establecimos el 8000
    client.connect(('localhost', 8000))


    # Ahora enviaremos un mensaje
    for s in make_list():
        client.send(bytes(CODE_RECV_RM_STR + s, encoding=ENCODING))
        # Ahora vamos a recibir lo que el servidor nos responda. Para esto vamos a utilizar el método recv, y vamos a colocar 1024, lo cual hace referencia al bufer; es decir, 1024 bytes
        response_serv = str(client.recv(BUFFER_SIZE), encoding=ENCODING)
        print(response_serv)

    client.send(bytes(CODE_RECV_RM_STR_END, encoding=ENCODING))

    while True:
        resp = str(client.recv(BUFFER_SIZE), encoding=ENCODING)
        if len(resp) > 0:
            code = resp[0]

            if code == CODE_SEND_RESP_PROCESSED:
                s = resp[1:]
                print(resp)
                client.send(bytes(CODE_SEND_RESP_PROCESSED, encoding=ENCODING))

            if code == CODE_SEND_RESP_PROCESSED_END:
                print("Cliente Cerrando")
                # Cerramos la conexión
                client.close()
                break

    

    # lists = response_serv.split("-")
    # even = lists[0].split(",")
    # odd = lists[1].split(",")
    
    # even = [x for x in even if x != '']
    # odd = [x for x in odd if x != '']

    # print(even)
    # print(odd)

    # print(response_serv)
    




if __name__ == "__main__":
    main()