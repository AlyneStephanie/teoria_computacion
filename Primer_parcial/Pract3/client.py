# Importamos socket al igual que con el servidor; sin embargo, su configuración será diferente
import socket
import random
from common import *
import gui
import time


def make_list():

    for i in range(NUM_STRS):
       s = bin(random.randint(0, (2**STR_SIZE) - 1))[2:].zfill(STR_SIZE)
       yield str(s)

def sorting(s):
    even = []
    odds = []
    for i in range(len(s)):
        if s[i][0] == 'e':
            even.append(s[i][1:])
        else:
            odds.append(s[i][1:])
    return even, odds

curr = [CODE_RECV_RM_STR]

def main():

    # Generamos un nuevo objeto socket
    client = socket.socket()

    # Hacemos la conexión
    # connect() va a recibir una tupla, y esta tupla va a contener dos valores: 1.- la dirección a la que nos tenemos que conectar, 2.- el puerto al que nos vamos a conectar. En el servidor establecimos el 8000
    client.connect(('localhost', 8000))
    

    strings = []

    tries = 1
    with open("./strings.txt", "wt+") as f:
        even_file = open("./strings_even.txt", "wt+")
        odds_file = open("./strings_odd.txt", "wt+")
        while tries:
            # Ahora enviaremos un mensaje
            for s in make_list():
                client.send(bytes(CODE_RECV_RM_STR + s, encoding=ENCODING))
                curr[0] = CODE_RECV_RM_STR

                # Ahora vamos a recibir lo que el servidor nos responda. Para esto vamos a utilizar el método recv, y vamos a colocar 1024, lo cual hace referencia al bufer; es decir, 1024 bytes
                response_serv = str(client.recv(BUFFER_SIZE), encoding=ENCODING)
                
                print(response_serv)

            client.send(bytes(CODE_RECV_RM_STR_END, encoding=ENCODING))
            curr[0] = CODE_RECV_RM_STR_END
            gui.pause(DELAY_SECONDS)


            while True:
                resp = str(client.recv(BUFFER_SIZE), encoding=ENCODING)
                gui.pause(DELAY_SECONDS)
                
                if len(resp) > 0:
                    code = resp[0]
                    curr[0] = code
                    if code == CODE_SEND_RESP_PROCESSED:
                        s = resp[1:]
                        strings.append(s)
                        print(resp)
                        client.send(bytes(CODE_SEND_RESP_PROCESSED, encoding=ENCODING))

                    if code == CODE_SEND_RESP_PROCESSED_END:
                        tries = random.randint(0, 1)
                        print(tries)
                        break
        
        even, odds = sorting(strings)
        # print(strings[0])
        f.write("Even: \n")
        for i in even:
            even_file.write(f"{i},")
            f.write(f"{i},")
        f.write("\nOdds\n")
        for i in odds:
            odds_file.write(f"{i},")
            f.write(f"{i},")
        

        print("Cliente Cerrando")
        # Cerramos la conexión

        client.send(bytes(CODE_END, encoding=ENCODING))
        curr[0] = CODE_END

        client.close()
        even_file.close()
        odds_file.close()

        input("Press [enter] to quit.")
        gui.close()
         



if __name__ == "__main__":
    # Genero el grafo
    gui.start_animation(curr)
    input("Press [enter] to continue.")
    main()