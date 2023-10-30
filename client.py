import socket
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():
    window = Tk()
    window.title('Share Music')
    window.geometry('300x300')
    window.configure(bg='#93a9cc')

    selectSong = Label(window, text='Select Song', bg='#93a9cc', font=('Ink Free', 10))
    selectSong.place(x=10, y=1)

    listBox= Listbox(window, height=10, width=39, activestyle='dotbox', font=('Ink Free', 10))
    listBox.place(x=10, y=25)

    scrollbar = Scrollbar(listBox)
    scrollbar.place(relheight=1, relx=1)
    scrollbar.config(command=listBox.yview)

    playButton = Button(window, text='Play', width=10, bd=1, bg='#eadeff', font=('Ink Free', 10))
    playButton.place(x=30, y=220)

    stop = Button(window, text='Stop', bd=1, width=10, bg='#eadeff', font=('Ink Free', 10))
    stop.place(x=200, y=220)

    upload = Button(window, text='Upload', bd=1, width=10, bg='#eadeff', font=('Ink Free', 10))
    upload.place(x=30, y=260)

    download = Button(window, text='Download', bd=1, width=10, bg='#eadeff', font=('Ink Free', 10))
    download.place(x=200, y=260)

    infoLabel = Label(window, text='', fg='blue', font=('Ink Free', 10))
    infoLabel.place(x=10, y=280)

    #available_fonts = font.families()
    #print(available_fonts)

    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    musicWindow()

setup()