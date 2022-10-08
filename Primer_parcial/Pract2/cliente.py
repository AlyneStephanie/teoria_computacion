# Importamos socket al igual que con el servidor; sin embargo, su configuración será diferente
import socket
import random


def main():
    # Generamos un nuevo objeto
    mi_socket = socket.socket()

    # Hacemos la conexión
    # connect() va a recibir una tupla, y esta tupla va a contener dos valores: 1.- la dirección a la que nos tenemos que conectar, 2.- el puerto al que nos vamos a conectar. En el servidor establecimos el 8000
    mi_socket.connect(('localhost', 8000))

    # lista = 

    # Ahora enviaremos un mensaje
    for s in make_list():
        print(s)
        mi_socket.send(bytes('3' + s, encoding='utf-8'))
        respuesta = str(mi_socket.recv(1024), encoding='utf-8')
        print(respuesta)

    mi_socket.send(bytes("2", encoding='utf-8'))

    # Ahora vamos a recibir lo que el servidor nos responda. Para esto vamos a utilizar el método recv, y vamos a colocar 1024, lo cual hace referencia al bufer; es decir, 1024 bytes
    

    # lists = respuesta.split("-")
    # even = lists[0].split(",")
    # odd = lists[1].split(",")
    
    # even = [x for x in even if x != '']
    # odd = [x for x in odd if x != '']

    # print(even)
    # print(odd)

    # print(respuesta)
    

    # Cerramos la conexión
    mi_socket.close()


def make_list():

    lista_str = ""
    # Deben ser 64 caracteres
    largo_cadena = 4
    # Deben ser 1_000_000 de cadenas
    num_cadenas = 10

    for i in range(num_cadenas):
       s = bin(random.randint(0, (2**largo_cadena) - 1))[2:].zfill(largo_cadena)
       yield str(s)

    # print(lista_str)

    # return lista_str


if __name__ == "__main__":
    main()