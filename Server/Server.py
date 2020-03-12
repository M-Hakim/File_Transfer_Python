import socket
from os import path, mkdir
from threading import Thread
from server_transceiver import *


def handle_client(sc, add):
    print(f"[+] {add} is connected.")
    received_msg = sc.recv(1).decode()
    if received_msg == "1":  # list
        files_list = str(os.listdir("cloud"))
        sc.sendall(files_list.encode())

    elif received_msg == "2":  # download
        filename = "cloud/" + sc.recv(32).decode()
        print(filename)
        send_file(sc, filename)

    elif received_msg == "3":  # upload
        recv_file(sc)

    sc.close()


if __name__ == "__main__":

    if not path.isdir("cloud"):
        mkdir("cloud")

    while True:
        with socket.socket() as s:
            s.bind((SERVER_HOST, SERVER_PORT))
            s.listen(5)
            print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
            client_socket, address = s.accept()
            Thread(target=handle_client, args=(client_socket, address)).start()
