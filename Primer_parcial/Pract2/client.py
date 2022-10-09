# Importamos socket al igual que con el servidor; sin embargo, su configuración será diferente
import socket
import random


def main():
    # Generamos un nuevo objeto
    my_socket = socket.socket()

    # Hacemos la conexión
    # connect() va a recibir una tupla, y esta tupla va a contener dos valores: 1.- la dirección a la que nos tenemos que conectar, 2.- el puerto al que nos vamos a conectar. En el servidor establecimos el 8000
    my_socket.connect(('localhost', 8000))

    # lista = 

    # Ahora enviaremos un mensaje
    for s in make_list():
        my_socket.send(bytes('3' + s, encoding='utf-8'))
        # Ahora vamos a recibir lo que el servidor nos responda. Para esto vamos a utilizar el método recv, y vamos a colocar 1024, lo cual hace referencia al bufer; es decir, 1024 bytes
        response_serv = str(my_socket.recv(1024), encoding='utf-8')

    my_socket.send(bytes('2', encoding='utf-8'))

    while True:
        resp = str(my_socket.recv(1024), encoding='utf-8')
        if len(resp) > 0:
            code = resp[0]

            if code == '4':
                s = resp[1:]
                my_socket.send(bytes("4", encoding='utf-8'))

            if code == '5':
                # Cerramos la conexión
                my_socket.close()
                break

    

    # lists = response_serv.split("-")
    # even = lists[0].split(",")
    # odd = lists[1].split(",")
    
    # even = [x for x in even if x != '']
    # odd = [x for x in odd if x != '']

    # print(even)
    # print(odd)

    # print(response_serv)
    



def make_list():

    # Deben ser 64 caracteres
    largo_cadena = 4
    # Deben ser 1_000_000 de cadenas
    num_cadenas = 10

    for i in range(num_cadenas):
       s = bin(random.randint(0, (2**largo_cadena) - 1))[2:].zfill(largo_cadena)
       yield str(s)



if __name__ == "__main__":
    main()