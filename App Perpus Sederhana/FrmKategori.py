import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Kategori import *
class FrmKategori:
    
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
        Label(mainFrame, text='KODE_KATEGORI:',bg="#6666FF",fg="Snow").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_KATEGORI:',bg="#6666FF",fg="Snow").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        mainFrame.config(bg="#6666FF")
        # Textbox
        self.txtKode_kategori = Entry(mainFrame) 
        self.txtKode_kategori.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_kategori.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama_kategori = Entry(mainFrame) 
        self.txtNama_kategori.grid(row=1, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id','kode_kategori','nama_kategori')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kode_kategori', text='KODE KATEGORI')
        self.tree.column('kode_kategori', width="100")
        self.tree.heading('nama_kategori', text='NAMA KATEGORI')
        self.tree.column('nama_kategori', width="110")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_kategori.delete(0,END)
        self.txtKode_kategori.insert(END,"")
        self.txtNama_kategori.delete(0,END)
        self.txtNama_kategori.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data kategori
        obj = Kategori()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["kode_kategori"],d["nama_kategori"]))
    def onCari(self, event=None):
        kode_kategori = self.txtKode_kategori.get()
        obj = Kategori()
        a = obj.get_by_kode_kategori(kode_kategori)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_kategori = self.txtKode_kategori.get()
        obj = Kategori()
        res = obj.get_by_kode_kategori(kode_kategori)
        self.txtKode_kategori.delete(0,END)
        self.txtKode_kategori.insert(END,obj.kode_kategori)
        self.txtNama_kategori.delete(0,END)
        self.txtNama_kategori.insert(END,obj.nama_kategori)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_kategori = self.txtKode_kategori.get()
        nama_kategori = self.txtNama_kategori.get()
        # create new Object
        obj = Kategori()
        obj.kode_kategori = kode_kategori
        obj.nama_kategori = nama_kategori
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_kategori(kode_kategori)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_kategori = self.txtKode_kategori.get()
        obj = Kategori()
        obj.kode_kategori = kode_kategori
        if(self.ditemukan==True):
            res = obj.delete_by_kode_kategori(kode_kategori)
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
    aplikasi = FrmKategori(root2, "Aplikasi Data Kategori")
    root2.mainloop()