import tqdm
import os
from client_config import *

def recv_file(active_socket):
    received = active_socket.recv(BUFFER_SIZE).decode()
    print(received)
    filename, filesize = received.split(SEPARATOR)
    filename = "local storage/" + os.path.basename(filename)
    filesize = int(filesize)
    # progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    progress = range(filesize)
    with open(filename, "wb") as f:
        for _ in progress:
            bytes_read = active_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            # progress.update(len(bytes_read))
    print("download complete")
    active_socket.close()


def send_file(server_socket, filename):
    filesize = os.path.getsize(filename)
    server_socket.send(f"{filename}{SEPARATOR}{filesize}".encode())
    # progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    progress = range(filesize)
    with open(filename, "rb") as f:
        for _ in progress:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            server_socket.sendall(bytes_read)
            # progress.update(len(bytes_read))
    print("upload complete")
    server_socket.close()


