#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import socket as sock
from datetime import datetime

DATE = datetime.now().strftime('%H:%M - %d/%m/%Y')

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.create_inserts()
            
    def create_labels(self):
        self.label = tk.Label(text="Port Scanner", font="Segoe 20 bold", bg="#273238", fg="white")
        self.label.place(x="10", y="10")

        self.label1 = tk.Label(text="URL:", font="Segoe 11", bg="#273238", fg="white")
        self.label1.place(x="10", y="70")
        
        self.label2 = tk.Label(text="Porta Inicial:", font="Segoe 11", bg="#273238", fg="white")
        self.label2.place(x="10", y="100")
        
        self.label3 = tk.Label(text="Porta Final:", font="Segoe 11", bg="#273238", fg="white")
        self.label3.place(x="10", y="130")
        
    def create_entries(self):
        self.entry_text = tk.StringVar()
        self.ini = tk.Entry(font="Segoe 11", bg="#696969", fg="white", width="30", 
                            textvariable="entry_text")
        self.ini.place(x="110", y="70")
              
        self.entry_text1 = tk.IntVar()
        self.portInitial = tk.Entry(font="Segoe 11", bg="#696969", fg="white", width="8", 
                                     textvariable="entry_text1")
        self.portInitial.place(x="110", y="100")
        
        self.entry_text2 = tk.IntVar()
        self.portFinal = tk.Entry(font="Segoe 11", bg="#696969", fg="white", width="8", 
                                   textvariable="entry_text2")
        self.portFinal.place(x="110", y="130")
        
        self.textbox = tk.Text(font=("Segoe 12 bold"), bg="#696969", fg="white", width="42", height="15",
                             selectbackground="green2", selectforeground="gray10")
        self.textbox.place(x="8", y="180")
    
    def create_inserts(self):
        text0 = " uol.com.br"
        text1 = " 0"
        text2 = " 0000"
        self.ini.insert(0, text0)
        self.portInitial.insert(0, text1)
        self.portFinal.insert(0, text2)
        self.textbox.insert(tk.INSERT, "\n\n  Preencha os campos do SCAN!")
        self.textbox.insert(tk.INSERT, "\n\n  Quanto mais alto o valor das portas")
        self.textbox.insert(tk.INSERT, "\n\n  Maior será a demora.")
        self.textbox.insert(tk.INSERT, "\n\n  O escaneamento vair levar tempo.")
    
    def create_buttons(self):
        self.button1 = tk.Button(text="SCAN", width="15", font="Arial 11 bold", bg="#FF8C00", 
                                 fg="white", command=self.write_on_square)
        self.button1.place(x="243", y="500")

    def write_on_square(self):
        self.name_solved = self.ini.get()
        self.resposta = sock.gethostbyname(self.name_solved)
        self.textbox.delete(1.0, tk.END)
        self.textbox.insert(tk.INSERT, "\n  Resultado do scan:")
        self.textbox.insert(tk.INSERT, "\n\n  O scan começou em: " + str(DATE))
        self.textbox.insert(tk.INSERT, "\n\n  Alvo encontrado: " + self.name_solved + " conectado.")
        self.textbox.insert(tk.INSERT, "\n\n  Feito o scan de: " + self.resposta)
        self.scanner()
        
    def scanner(self):
        self.portI = int(self.portInitial.get())
        self.portF = int(self.portFinal.get())
        
        try:
            for port in range(self.portI, self.portF): 
                attach = sock.socket(sock.AF_INET, sock.SOCK_STREAM) 
                sock.setdefaulttimeout(1) 
                result = attach.connect_ex((self.resposta, port))
                self.port = str(port)
                if result == 0:
                    self.textbox.insert(tk.INSERT, "\n\n  Open ports: " + self.port)
                attach.close()   
        except KeyboardInterrupt: 
            print("\n Exitting Program !!!!") 
            quit 
        except sock.gaierror: 
            print("\n Hostname Could Not Be Resolved !!!!") 
            quit 
        except sock.error: 
            print("\n Server isn't responding !!!!") 
            quit 

root = tk.Tk()
PortScanner = App(master=root)
PortScanner.master.config(background="#273238")
PortScanner.master.title("PortScanner")
PortScanner.master.geometry("400x540+450+20")
PortScanner.master.resizable(False, False)
PortScanner.mainloop()
