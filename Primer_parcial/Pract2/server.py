import socket

def main():
    # Genera un socket con los valores por default
    my_socket = socket.socket()

    # Ahora establezco la conexión con el método bind, el cual recibe una tupla con dos valores: 1.- host, 2.- en qué puerto estará escuchando el socket
    my_socket.bind(('localhost', 8000))

    # Ahora establezco la cantidad de peticiones que puede manejar en cola nuestro socket
    my_socket.listen(1)

    # Una vez establecida la conexión y que hayamos definido la cantidad de conexiones que puedan estar en cola, se establece un ciclo infinito
    while True:
        # Dentro de este ciclo, vamos a aceptar las peticiones de los clientes
        # Esta línea nos va a retornar dos valores: 1.- conexión, 2.- dirección
        connection_cl, addr = my_socket.accept()
        print("Nueva conexión establecida")
        # Imprimimos la dirección de la cual se ha hecho la petición
        print(addr)
        odds = []
        even = []

        # Tenemos que enviar un montón de peticiones por cada conexión
        while True:
            # Podemos obtener lo que el cliente nos está enviando
            request_str = str(connection_cl.recv(1024), encoding='utf-8')

            if request_str[0] == "2":
                print(even)
                print(odds)
                
                for e in even:
                    connection_cl.send(bytes(f"4e{e}", encoding='utf-8'))
                    resp = str(connection_cl.recv(1024), encoding='utf-8')
                    if resp[0] == "4":
                        continue
                    else:
                        print(f"Error: código no esperado {resp[0]}")
                        break

                for o in odds:
                    connection_cl.send(bytes(f"4o{o}", encoding='utf-8'))
                    resp = str(connection_cl.recv(1024), encoding='utf-8')
                    if resp[0] == "4":
                        continue
                    else:
                        print(f"Error: código no esperado {resp[0]}")
                        break

                connection_cl.send(bytes(f"5_end", encoding='utf-8'))   

                # Ahora cerramos la conexión con el cliente
                connection_cl.close()

                break

            if request_str[0] == "3":
                s = request_str[1:]
                if is_even(s):
                    even.append(s)
                else:
                    odds.append(s)

            # Una vez con la petición, enviamos un mensaje al cliente:

            connection_cl.send(bytes("3", encoding='utf-8'))

        

    # Si corremos ahora el servidor, no ocurrirá nada, lo que significa que el servidor está a la espera. Ahora, lo que debemos hacer es generar el cliente.

def is_even(s):
    return  s.count('1') % 2 == 0


if __name__ == "__main__":
    main()