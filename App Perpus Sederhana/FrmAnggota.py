import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Anggota import *
from PIL import Image, ImageTk

class FrmAnggota:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODEANGGOTA:',bg="#6666FF",fg="Snow").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:',bg="#6666FF",fg="Snow").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JENIS KELAMIN:',bg="#6666FF",fg="Snow").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:',bg="#6666FF",fg="Snow").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        mainFrame.configure(bg="#6666FF")

        # Textbox
        self.txtKodeanggota = Entry(mainFrame) 
        self.txtKodeanggota.grid(row=0, column=1, padx=5, pady=5)
        self.txtKodeanggota.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtJk = Entry(mainFrame) 
        self.txtJk.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=3, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('idanggota','kodeanggota','nama','jk','alamat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idanggota', text='ID')
        self.tree.column('idanggota', width="30")
        self.tree.heading('kodeanggota', text='KODE ANGGOTA')
        self.tree.column('kodeanggota', width="100")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="120")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="30")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="120")
        # set tree position
        self.tree.place(x=0, y=200)

    def onClear(self, event=None):
        self.txtKodeanggota.delete(0,END)
        self.txtKodeanggota.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtJk.delete(0,END)
        self.txtJk.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data anggota
        obj = Anggota()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["idanggota"],d["kodeanggota"],d["nama"],d["jk"],d["alamat"]))
    def onCari(self, event=None):
        kodeanggota = self.txtKodeanggota.get()
        obj = Anggota()
        a = obj.get_by_kodeanggota(kodeanggota)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kodeanggota = self.txtKodeanggota.get()
        obj = Anggota()
        res = obj.get_by_kodeanggota(kodeanggota)
        self.txtKodeanggota.delete(0,END)
        self.txtKodeanggota.insert(END,obj.kodeanggota)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtJk.delete(0,END)
        self.txtJk.insert(END,obj.jk)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kodeanggota = self.txtKodeanggota.get()
        nama = self.txtNama.get()
        jk = self.txtJk.get()
        alamat = self.txtAlamat.get()
        # create new Object
        obj = Anggota()
        obj.kodeanggota = kodeanggota
        obj.nama = nama
        obj.jk = jk
        obj.alamat = alamat
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kodeanggota(kodeanggota)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kodeanggota = self.txtKodeanggota.get()
        obj = Anggota()
        obj.kodeanggota = kodeanggota
        if(self.ditemukan==True):
            res = obj.delete_by_kodeanggota(kodeanggota)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmAnggota(root2, "Aplikasi Data Anggota")
    root2.mainloop()