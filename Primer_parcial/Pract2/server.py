import socket
from common import *
import common
from automata import is_even


def process_conn(conn):
    odds = []
    even = []
    # Tenemos que enviar un montón de peticiones por cada conexión
    while True:
        # Podemos obtener lo que el cliente nos está enviando
        request_str = str(conn.recv(BUFFER_SIZE), encoding=ENCODING)

        code = request_str[0]

        match code:

            case common.CODE_RECV_RM_STR_END:
                print(even)
                print(odds)
                code_resp = None
                for e in even:
                    conn.send(bytes(f"{CODE_SEND_RESP_PROCESSED}e{e}", encoding=ENCODING))
                    resp = str(conn.recv(BUFFER_SIZE), encoding=ENCODING)
                    code_resp = resp[0]
                    if code_resp == CODE_SEND_RESP_PROCESSED:
                        continue
                    else:
                        print(f"Error: código no esperado {code_resp}")
                        break

                for o in odds:
                    conn.send(bytes(f"{CODE_SEND_RESP_PROCESSED}o{o}", encoding=ENCODING))
                    resp = str(conn.recv(BUFFER_SIZE), encoding=ENCODING)
                    code_resp = resp[0]
                    if code_resp == CODE_SEND_RESP_PROCESSED:
                        continue
                    else:
                        print(f"Error: código no esperado {code_resp}")
                        break

                conn.send(bytes(CODE_SEND_RESP_PROCESSED_END, encoding=ENCODING))   

            case '3':
                s = request_str[1:]
                if is_even(s):
                    even.append(s)
                else:
                    odds.append(s)
                conn.send(bytes(CODE_RECV_RM_STR, encoding=ENCODING))

            case '6':
                # Ahora cerramos la conexión con el cliente
                conn.close()
                break


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
 


if __name__ == "__main__":
    main()