from tkinter import *

root = Tk()
root.title("File System Management")
canvas1 = Canvas(root, width=400, height=300, relief='raised')

canvas1.pack()
# label1
label1 = Label(root, text='File System Management')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

# label2
label2 = Label(root, text='Enter File Name')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

# File Name Text Filed
entry1 = Entry(root)
canvas1.create_window(200, 140, window=entry1)
# Text Area
S = Scrollbar(root)
T = Text(root, height=20, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

# buttons
download_btn = Button(text='Download', bg='brown', fg='white', font=('helvetica', 9, 'bold'))
upload_btn = Button(text='Upload', bg='brown', fg='white', font=('helvetica', 9, 'bold'))
list_btn = Button(text='List server files', bg='brown', fg='white', font=('helvetica', 9, 'bold'))
clear_screen_btn = Button(text='Clear screen', bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=download_btn)
canvas1.create_window(200, 210, window=upload_btn)
canvas1.create_window(200, 240, window=list_btn)
canvas1.create_window(200, 270, window=clear_screen_btn)