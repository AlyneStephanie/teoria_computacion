import socket
from common import *


def process_conn(conn):
    odds = []
    even = []
    # Tenemos que enviar un montón de peticiones por cada conexión
    while True:
        # Podemos obtener lo que el cliente nos está enviando
        request_str = str(conn.recv(BUFFER_SIZE), encoding=ENCODING)

        if request_str[0] == CODE_RECV_RM_STR_END:
            print(even)
            print(odds)
            code = None
            for e in even:
                conn.send(bytes(f"{CODE_SEND_RESP_PROCESSED}e{e}", encoding=ENCODING))
                resp = str(conn.recv(BUFFER_SIZE), encoding=ENCODING)
                code = resp[0]
                if code == CODE_SEND_RESP_PROCESSED:
                    continue
                else:
                    print(f"Error: código no esperado {code}")
                    break

            for o in odds:
                conn.send(bytes(f"{CODE_SEND_RESP_PROCESSED}o{o}", encoding=ENCODING))
                resp = str(conn.recv(BUFFER_SIZE), encoding=ENCODING)
                code = resp[0]
                if code == CODE_SEND_RESP_PROCESSED:
                    continue
                else:
                    print(f"Error: código no esperado {code}")
                    break

            conn.send(bytes(CODE_SEND_RESP_PROCESSED_END, encoding=ENCODING))   

            # Ahora cerramos la conexión con el cliente
            conn.close()

            break

        if request_str[0] == CODE_RECV_RM_STR:
            s = request_str[1:]
            if is_even(s):
                even.append(s)
            else:
                odds.append(s)

        # Una vez con la petición, enviamos un mensaje al cliente:

        conn.send(bytes(CODE_RECV_RM_STR, encoding=ENCODING))
    

def main():
    # Genera un socket con los valores por default
    server = socket.socket()

    # Ahora establezco la conexión con el método bind, el cual recibe una tupla con dos valores: 1.- host, 2.- en qué puerto estará escuchando el socket
    server.bind(('localhost', 8000))

    # Ahora establezco la cantidad de peticiones que puede manejar en cola nuestro socket
    server.listen(1)

    # Una vez establecida la conexión y que hayamos definido la cantidad de conexiones que puedan estar en cola, se establece un ciclo infinito
    while True:
        # Dentro de este ciclo, vamos a aceptar las peticiones de los clientes
        # Esta línea nos va a retornar dos valores: 1.- conexión, 2.- dirección
        conn, addr = server.accept()
        print("Nueva conexión establecida")
        # Imprimimos la dirección de la cual se ha hecho la petición
        print(addr)
        process_conn(conn)
 

def is_even(s):
    return  s.count('1') % 2 == 0


if __name__ == "__main__":
    main()