import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Buku import *
class FrmBuku:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("900x500")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODEBUKU:',bg="#6666FF",fg="Snow").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JUDUL:',bg="#6666FF",fg="Snow").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENGARANG:',bg="#6666FF",fg="Snow").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENERBIT:',bg="#6666FF",fg="Snow").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TAHUN:',bg="#6666FF",fg="Snow").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEKATEGORI:',bg="#6666FF",fg="Snow").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        mainFrame.config(bg="#6666FF")
        # Textbox
        self.txtKodebuku = Entry(mainFrame) 
        self.txtKodebuku.grid(row=0, column=1, padx=5, pady=5)
        self.txtKodebuku.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtJudul = Entry(mainFrame) 
        self.txtJudul.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtPengarang = Entry(mainFrame) 
        self.txtPengarang.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtPenerbit = Entry(mainFrame) 
        self.txtPenerbit.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtTahun = Entry(mainFrame) 
        self.txtTahun.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtKodekategori = Entry(mainFrame) 
        self.txtKodekategori.grid(row=5, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('idbuku','kodebuku','judul','pengarang','penerbit','tahun','kodekategori')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idbuku', text='ID')
        self.tree.column('idbuku', width="30")
        self.tree.heading('kodebuku', text='KODEBUKU')
        self.tree.column('kodebuku', width="90")
        self.tree.heading('judul', text='JUDUL')
        self.tree.column('judul', width="250")
        self.tree.heading('pengarang', text='PENGARANG')
        self.tree.column('pengarang', width="160")
        self.tree.heading('penerbit', text='PENERBIT')
        self.tree.column('penerbit', width="150")
        self.tree.heading('tahun', text='TAHUN')
        self.tree.column('tahun', width="70")
        self.tree.heading('kodekategori', text='KODEKATEGORI')
        self.tree.column('kodekategori', width="100")
        # set tree position
        self.tree.place(x=0, y=210)
        
    def onClear(self, event=None):
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,"")
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,"")
        self.txtPengarang.delete(0,END)
        self.txtPengarang.insert(END,"")
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,"")
        self.txtTahun.delete(0,END)
        self.txtTahun.insert(END,"")
        self.txtKodekategori.delete(0,END)
        self.txtKodekategori.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data buku
        obj = Buku()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["idbuku"],d["kodebuku"],d["judul"],d["pengarang"],d["penerbit"],d["tahun"],d["kodekategori"]))
    def onCari(self, event=None):
        kodebuku = self.txtKodebuku.get()
        obj = Buku()
        a = obj.get_by_kodebuku(kodebuku)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kodebuku = self.txtKodebuku.get()
        obj = Buku()
        res = obj.get_by_kodebuku(kodebuku)
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,obj.kodebuku)
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,obj.judul)
        self.txtPengarang.delete(0,END)
        self.txtPengarang.insert(END,obj.pengarang)
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,obj.penerbit)
        self.txtTahun.delete(0,END)
        self.txtTahun.insert(END,obj.tahun)
        self.txtKodekategori.delete(0,END)
        self.txtKodekategori.insert(END,obj.kodekategori)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kodebuku = self.txtKodebuku.get()
        judul = self.txtJudul.get()
        pengarang = self.txtPengarang.get()
        penerbit = self.txtPenerbit.get()
        tahun = self.txtTahun.get()
        kodekategori = self.txtKodekategori.get()
        # create new Object
        obj = Buku()
        obj.kodebuku = kodebuku
        obj.judul = judul
        obj.pengarang = pengarang
        obj.penerbit = penerbit
        obj.tahun = tahun
        obj.kodekategori = kodekategori
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kodebuku(kodebuku)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kodebuku = self.txtKodebuku.get()
        obj = Buku()
        obj.kodebuku = kodebuku
        if(self.ditemukan==True):
            res = obj.delete_by_kodebuku(kodebuku)
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
    aplikasi = FrmBuku(root2, "Aplikasi Data Buku")
    root2.mainloop()