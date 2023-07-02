import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Peminjaman import *
class FrmPeminjaman:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("900x600")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='NOMORBUKTI:',bg="#6666FF",fg="Snow").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGL_PINJAM:',bg="#6666FF",fg="Snow").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEANGGOTA:',bg="#6666FF",fg="Snow").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEBUKU1:',bg="#6666FF",fg="Snow").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEBUKU2:',bg="#6666FF",fg="Snow").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGLHRSKEMBALI:',bg="#6666FF",fg="Snow").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGL_DIKEMBALIKAN:',bg="#6666FF",fg="Snow").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='STATUS_PINJAM:',bg="#6666FF",fg="Snow").grid(row=7, column=0,
            sticky=W, padx=5, pady=5)
        mainFrame.config(bg="#6666FF")
        # Textbox
        self.txtNomorbukti = Entry(mainFrame) 
        self.txtNomorbukti.grid(row=0, column=1, padx=5, pady=5)
        self.txtNomorbukti.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtKodeanggota = Entry(mainFrame) 
        self.txtKodeanggota.grid(row=2, column=1, padx=5, pady=5)
        #Textbox
        self.txtTgl_pinjam = Entry(mainFrame) 
        self.txtTgl_pinjam.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtKodebuku1 = Entry(mainFrame) 
        self.txtKodebuku1.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtKodebuku2 = Entry(mainFrame) 
        self.txtKodebuku2.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtStatus_pinjam = Entry(mainFrame) 
        self.txtStatus_pinjam.grid(row=7, column=1, padx=5, pady=5)
        # Textbox
        self.txtTglhrskembali = Entry(mainFrame) 
        self.txtTglhrskembali.grid(row=5, column=1, padx=5, pady=5)
        # Textbox
        self.txtTgl_dikembalikan = Entry(mainFrame) 
        self.txtTgl_dikembalikan.grid(row=6, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('idpeminjaman','nomorbukti','tgl_pinjam','kodeanggota','kodebuku1','kodebuku2','tglhrskembali','tgl_dikembalikan','status_pinjam')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idpeminjaman', text='ID')
        self.tree.column('idpeminjaman', width="30")
        self.tree.heading('nomorbukti', text='NO BUKTI')
        self.tree.column('nomorbukti', width="70")
        self.tree.heading('tgl_pinjam', text='TGL PINJAM')
        self.tree.column('tgl_pinjam', width="100")
        self.tree.heading('kodeanggota', text='KODE ANGGOTA')
        self.tree.column('kodeanggota', width="110")
        self.tree.heading('kodebuku1', text='KODE BUKU1')
        self.tree.column('kodebuku1', width="100")
        self.tree.heading('kodebuku2', text='KODE BUKU2')
        self.tree.column('kodebuku2', width="100")
        self.tree.heading('tglhrskembali', text='TGL HRS KEMBALI')
        self.tree.column('tglhrskembali', width="120")
        self.tree.heading('tgl_dikembalikan', text='TGL DIKEMBALIKAN')
        self.tree.column('tgl_dikembalikan', width="120")
        self.tree.heading('status_pinjam', text='STATUS PINJAM')
        self.tree.column('status_pinjam', width="120")
        # set tree position
        self.tree.place(x=0, y=300)
        
    def onClear(self, event=None):
        self.txtNomorbukti.delete(0,END)
        self.txtNomorbukti.insert(END,"")
        self.txtTgl_pinjam.delete(0,END)
        self.txtTgl_pinjam.insert(END,"")
        self.txtKodeanggota.delete(0,END)
        self.txtKodeanggota.insert(END,"")
        self.txtKodebuku1.delete(0,END)
        self.txtKodebuku1.insert(END,"")
        self.txtKodebuku2.delete(0,END)
        self.txtKodebuku2.insert(END,"")
        self.txtStatus_pinjam.delete(0,END)
        self.txtStatus_pinjam.insert(END,"")
        self.txtTglhrskembali.delete(0,END)
        self.txtTglhrskembali.insert(END,"")
        self.txtTgl_dikembalikan.delete(0,END)
        self.txtTgl_dikembalikan.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data peminjaman
        obj = Peminjaman()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["idpeminjaman"],d["nomorbukti"],d["tgl_pinjam"],d["kodeanggota"],d["kodebuku1"],d["kodebuku2"],d["tglhrskembali"],d["tgl_dikembalikan"],d["status_pinjam"]))
    def onCari(self, event=None):
        nomorbukti = self.txtNomorbukti.get()
        obj = Peminjaman()
        a = obj.get_by_nomorbukti(nomorbukti)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        nomorbukti = self.txtNomorbukti.get()
        obj = Peminjaman()
        res = obj.get_by_nomorbukti(nomorbukti)
        self.txtNomorbukti.delete(0,END)
        self.txtNomorbukti.insert(END,obj.nomorbukti)
        self.txtTgl_pinjam.delete(0,END)
        self.txtTgl_pinjam.insert(END,obj.tgl_pinjam)
        self.txtKodeanggota.delete(0,END)
        self.txtKodeanggota.insert(END,obj.kodeanggota)
        self.txtKodebuku1.delete(0,END)
        self.txtKodebuku1.insert(END,obj.kodebuku1)
        self.txtKodebuku2.delete(0,END)
        self.txtKodebuku2.insert(END,obj.kodebuku2)
        self.txtStatus_pinjam.delete(0,END)
        self.txtStatus_pinjam.insert(END,obj.status_pinjam)
        self.txtTglhrskembali.delete(0,END)
        self.txtTglhrskembali.insert(END,obj.tglhrskembali)
        self.txtTgl_dikembalikan.delete(0,END)
        self.txtTgl_dikembalikan.insert(END,obj.tgl_dikembalikan)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        nomorbukti = self.txtNomorbukti.get()
        tgl_pinjam = self.txtTgl_pinjam.get()
        kodeanggota = self.txtKodeanggota.get()
        kodebuku1 = self.txtKodebuku1.get()
        kodebuku2 = self.txtKodebuku2.get()
        tglhrskembali = self.txtTglhrskembali.get()
        tgl_dikembalikan = self.txtTgl_dikembalikan.get()
        status_pinjam = self.txtStatus_pinjam.get()
        # create new Object
        obj = Peminjaman()
        obj.nomorbukti = nomorbukti
        obj.tgl_pinjam = tgl_pinjam
        obj.kodeanggota = kodeanggota
        obj.kodebuku1 = kodebuku1
        obj.kodebuku2 = kodebuku2
        obj.tglhrskembali = tglhrskembali
        obj.tgl_dikembalikan = tgl_dikembalikan
        obj.status_pinjam = status_pinjam
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_nomorbukti(nomorbukti)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        nomorbukti = self.txtNomorbukti.get()
        obj = Peminjaman()
        obj.nomorbukti = nomorbukti
        if(self.ditemukan==True):
            res = obj.delete_by_nomorbukti(nomorbukti)
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
    aplikasi = FrmPeminjaman(root2, "Aplikasi Data Peminjaman")
    root2.mainloop()