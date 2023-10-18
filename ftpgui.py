import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ftplib import FTP
#define functions for the FTP actions
def connect_to_server():
    global ftp
    try:
        server_address = server_entry.get()
        port_enter = int(port_entry.get())
        username = username_entry.get()
        password = password_entry.get()
        ftp = FTP()
        ftp.connect(server_address, port=port_enter)
        ftp.login(user=username, passwd=password)
        status_text.set(f'connected to server {server_address} sucessfully')
    except Exception as e:
        print(e)
        status_text.set(f'Error: {e}')
    
def close_server():
    ftp.close()
    status_text.set('disconnected gracefully')

def list_files():
    try:
        files = ftp.nlst()
        status_text.set('list of files in current directory')
        file_list.delete(1.0, tk.END) #clears previous content
        for file in files:
            file_list.insert(tk.END, file + '\n')
    except Exception as e:
        status_text.set(f'Error: {e}')
def upload_file():
    file_path = filedialog.askstring('Input', 'Enter file name:')

def download_file():
    pass

#create the main window
root = tk.Tk()
root.geometry("640x600")
root.title("FTPy")
#add entry fields
server_label = ttk.Label(root, text="server address")
server_label.pack(pady=5)
server_entry = ttk.Entry(root)
server_entry.pack(pady=5)

port_label = ttk.Label(root, text="port")
port_label.pack(pady=5)
port_entry = ttk.Entry(root)
port_entry.pack(pady=5)

username_label = ttk.Label(root, text='username')
username_label.pack(pady=5)
username_entry = ttk.Entry(root)
username_entry.pack(pady=5)

password_label = ttk.Label(root, text='password')
password_label.pack(pady=5)
password_entry = ttk.Entry(root, show='*')
password_entry.pack(pady=5)
#adding label for status
status_text = tk.StringVar()
status_label = ttk.Label(root, textvariable=status_text, font=('Arial', 10, 'bold'), foreground='green')
status_label.pack(pady=10, padx=10)

file_list = tk.Text(root, height=10, width=50)
file_list.pack(pady=10)

#add our buttons
connect_button = tk.Button(root, text="connect", command=connect_to_server)
disconnect_button = tk.Button(root, text='disconnect', command=close_server)
list_button = tk.Button(root, text="list files", command=list_files)
upload_button = tk.Button(root, text="upload file", command=upload_file)
download_button = tk.Button(root, text="download file", command=download_file)


#pack the buttons into the window
connect_button.pack(pady=10)
disconnect_button.pack(pady=10)
list_button.pack(pady=10)
upload_button.pack(pady=10)
download_button.pack(pady=10)


#start the main loop
root.mainloop()