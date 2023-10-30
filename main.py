#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket as sock
import tkinter as tk
from datetime import datetime

DATE = datetime.now().strftime('%H:%M - %d/%m/%Y')
SEGOE = 'Segoe 11'

class PortScannerApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.config(background='#273238')
        self.master.iconbitmap(r'/home/rodrigo/pirate.ico')
        self.master.title('PortScanner')
        self.master.geometry('400x540+450+20')
        self.master.resizable(False, False)
        self.master.eval('tk::PlaceWindow . center')

        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.create_textbox()

    def create_labels(self):
        labels = [
            ("Port Scanner", 'Segoe 20 bold'),
            ("URL:", SEGOE),
            ("Porta Inicial:", SEGOE),
            ("Porta Final:", SEGOE)
        ]

        for i, (text, font) in enumerate(labels):
            label = tk.Label(text=text, font=font, bg='#273238', fg='white')
            label.place(x=10, y=70 + i * 30)

    def create_entries(self):
        entry_params = [
            ("URL:", 30, 'entry_text'),
            ("Porta Inicial:", 8, 'entry_text1'),
            ("Porta Final:", 8, 'entry_text2')
        ]

        self.entries = {}
        for i, (label_text, width, var_name) in enumerate(entry_params):
            entry_var = tk.StringVar()
            entry = tk.Entry(font=SEGOE, bg='#696969', fg='white', width=width, textvariable=entry_var)
            entry.insert(0, " site.com.br" if i == 0 else " 0" if i == 1 else " 0000")
            entry.place(x=110, y=100 + i * 30)
            self.entries[var_name] = entry_var

    def create_buttons(self):
        self.scan_button = tk.Button(text='SCAN', width=15, font='Arial 11 bold', bg='#FF8C00', fg='white',
                                     command=self.scan_ports)
        self.scan_button.place(x=243, y=500)

    def create_textbox(self):
        self.textbox = tk.Text(font=('Segoe 12 bold'), bg='#696969', fg='white', width=42, height=15,
                              selectbackground='green2', selectforeground='gray10')
        self.textbox.place(x=8, y=180)
        self.textbox.insert(tk.INSERT, '\n\n  Preencha os campos do SCAN!')
        self.textbox.insert(tk.INSERT, '\n\n  Quanto mais alto o valor das portas')
        self.textbox.insert(tk.INSERT, '\n\n  Maior será a demora.')
        self.textbox.insert(tk.INSERT, '\n\n  O escaneamento vai levar tempo.')

    def scan_ports(self):
        url = self.entries['entry_text'].get()
        ip_address = self.get_ip_address(url)

        if not ip_address:
            self.display_message("Hostname Could Not Be Resolved !!!!")
            return

        port_initial = int(self.entries['entry_text1'].get())
        port_final = int(self.entries['entry_text2'].get())

        for port in range(port_initial, port_final + 1):
            if self.is_port_open(ip_address, port):
                self.display_message(f'\n\n  Open port: {port}')

    def get_ip_address(self, url):
        try:
            return sock.gethostbyname(url)
        except sock.gaierror:
            return None

    def is_port_open(self, ip_address, port):
        try:
            with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((ip_address, port))
                return result == 0
        except sock.error:
            return False

    def display_message(self, message):
        self.textbox.delete(1.0, tk.END)
        self.textbox.insert(tk.INSERT, '\n  Resultado do scan:')
        self.textbox.insert(tk.INSERT, '\n\n  O scan começou em: ' + str(DATE))
        self.textbox.insert(tk.INSERT, message)

if __name__ == "__main__":
    root = tk.Tk()
    PortScanner = PortScannerApp(master=root)
    PortScanner.mainloop()

PortScanner.master.title('PortScanner')
PortScanner.master.geometry('400x540+450+20')
PortScanner.master.resizable(False, False)
PortScanner.master.eval('tk::PlaceWindow . center')
PortScanner.mainloop()
