
import socket
from os import path, mkdir

from client_transceiver import *
from tkinter import filedialog
from threading import Thread
from gui import *


def connect():
    s = socket.socket()
    try:
        s.connect((host, port))
    except socket.error:
        print("server down")
        s = False
        T.insert(END, "Can't connect, perhaps server is down!")
        T.insert(END, "\n____________________________________\n")
    return s


def upload(file_path):
    s = connect()
    if s:
        s.sendall("3".encode())
        T.insert(END, "uploading: " + file_path)
        T.insert(END, "\n____________________________________\n")
        send_file(s, file_path)
        T.insert(END, "done uploading: " + file_path)
        T.insert(END, "\n____________________________________\n")
    return


def download(file_name):
    s = connect()
    if s:
        s.sendall("2".encode())
        T.insert(END, "downloading: " + file_name + " to: " + os.getcwd() + "/local storage")
        T.insert(END, "\n____________________________________\n")
        s.sendall(file_name.encode())
        recv_file(s)
        T.insert(END, "done downloading: " + file_name)
        T.insert(END, "\n____________________________________\n")
    return


files_list = ""


def list_files():
    s = connect()
    global files_list
    if s:
        s.sendall("1".encode())
        files_list = str(s.recv(BUFFER_SIZE).decode())
        T.insert(END, "Server available files:")
        T.insert(END, "\n----------------------\n")
        T.insert(END, files_list)
        T.insert(END, "\n____________________________________\n")


def u_thread():
    file_path = filedialog.askopenfilename()
    if file_path != "":
        Thread(target=upload, args=(file_path,)).start()
    return


def d_thread():
    filename = str(entry1.get()).strip()
    if filename == "":
        T.insert(END, "Please type the file name to download")
        T.insert(END, "\n____________________________________\n")
    elif not files_list.__contains__(filename):
        print(files_list)
        T.insert(END, "File doesn't exist! please refresh files list")
        T.insert(END, "\n____________________________________\n")
    else:
        Thread(target=download, args=(filename,)).start()
    return


def l_thread():
    Thread(target=list_files, args=()).start()
    return


def clear_txt_area():
    T.delete('1.0', END)
    return


if __name__ == "__main__":
    if not path.isdir("local storage"):
        mkdir("local storage")

    download_btn['command'] = d_thread
    upload_btn['command'] = u_thread
    list_btn['command'] = l_thread
    clear_screen_btn['command'] = clear_txt_area
    list_files()

    print(files_list)

    root.mainloop()
