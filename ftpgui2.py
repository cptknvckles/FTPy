from tkinter import *
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
import ttkbootstrap as tbk
from ftplib import FTP

#define our functions 
def connect_to_server():
    pass
    
#define our window
root = tbk.Window(themename='superhero')
root.title('PyTransfer Pro')
root.geometry('1200x680')
root.resizable('FALSE', 'FALSE')

#creating an entry frame
enter_info_frame = tbk.LabelFrame(root, text='Enter server information:', bootstyle='success')
enter_info_frame.pack(padx=10, pady=10, fill='both', expand=False)
#labels Entries and Packs for entrer_info_frame
server_label = tbk.Label(enter_info_frame, text='Server Address:')
server_label.pack(side='left', padx=(0, 10), anchor='w')
server_entry = tbk.Entry(enter_info_frame, bootstyle='success', width=10)
server_entry.pack(side='left', pady=5, padx=5, anchor='w')

port_label = tbk.Label(enter_info_frame, text='Port Number:')
port_label.pack(side='left', padx=(0,10), anchor='w')
port_entry = tbk.Entry(enter_info_frame, bootstyle='success', width=4)
port_entry.pack(side='left', padx=5, pady=5)

username_label = tbk.Label(enter_info_frame, text='username:')
username_label.pack(side='left', padx=(0,10), anchor='w')
username_entry = tbk.Entry(enter_info_frame, bootstyle='success', width=10)
username_entry.pack(side='left', padx=5, pady=5)

password_label = tbk.Label(enter_info_frame, text='password:')
password_label.pack(side='left', padx=(0,10), anchor='w')
password_entry = tbk.Entry(enter_info_frame, bootstyle='success', width=15, show='*')
password_entry.pack(side='left', padx=5, pady=5)

#buttons
connect_button = tbk.Button(enter_info_frame, text='Connect!', bootstyle='success')
connect_button.pack(side='right', padx=(0,10))



#prePacks


#grids
#toast notification

root.mainloop()