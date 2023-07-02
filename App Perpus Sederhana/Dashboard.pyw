import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox, Menu
from Users import *
from FrmBuku import *
from FrmPeminjaman import *
from FrmAnggota import*
from FrmKategori import*
from PIL import Image, ImageTk

class Dashboard:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("750x500")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.my_w_child = None
        self.aturKomponen()
        root.resizable(0,0)
        
    def new_window( self, number, _class):
        new = tk.Toplevel()
        new.transient()
        new.grab_set()
        _class(new, number)
       
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        mainmenu = Menu(self.parent)
        self.parent.config(menu=mainmenu)
        file_menu1 = Menu(mainmenu, tearoff= False)
        
        # Menu Awal
        file_menu1.add_command(
            label='Login', command=self.show_login
        )
        file_menu1.add_command(
            label='Exit', command=root.destroy
        )
        
        # Tampilkan menu ke layar
        mainmenu.add_cascade(
            label="Menu", menu=file_menu1,
        )
        mainFrame.configure(bg="#000066")
        judul=Label(root,text="APLIKASI",font=('Cooper Black',30, "bold"),bg='#000066', fg='snow')
        judul.place(x=220, y=10)
        judul=Label(root,text="PERPUSTAKAAN",font=('Cooper Black',30),bg='#000066', fg='snow')
        judul.place(x=220,y=80)
                              
        Label(root,text="@2023, Arya Ghiffari",font=('cambria',12),bg='#000066', fg='snow').place(x=500,y=358)
        Label(root,text="Nim    : 210511004",font=('cambria',12),bg='#000066', fg='snow').place(x=500,y=380)
        Label(root,text="Teknik Informatika",font=('cambria',12),bg='#000066', fg='snow').place(x=500,y=400)

        image1 = Image.open("umc.png")
        resize = image1.resize((120,120),Image.ANTIALIAS)
        new_photo = ImageTk.PhotoImage(resize)
        label= Label(image= new_photo, bg = '#000066')
        label.image = new_photo
        label.pack()
        label.place(x=50,y=10)
        
    def menuAdmin(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar, tearoff= False)
        admin_menu = Menu(menubar, tearoff= False)
      
        # Menu File
       
        file_menu.add_command(
            label='Log out', command=self.onLogout
        )
        file_menu.add_command(
            label='Exit', command=root.destroy
        )

      
        # Menu Admin
        admin_menu.add_command(
            label='Daftar Buku', command= lambda: self.new_window("Buku", FrmBuku)
        )
        admin_menu.add_command(
            label='Data Peminjaman', command= lambda: self.new_window("Peminjaman", FrmPeminjaman)
        )
        admin_menu.add_command(
            label='Data Anggota', command= lambda: self.new_window("Anggota", FrmAnggota)
        )
        admin_menu.add_command(
            label='Kategori Buku', command= lambda: self.new_window("Kategori", FrmKategori)
        )
        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="File", menu=file_menu
        )
        
        menubar.add_cascade(
            label="Menu Petugas", menu=admin_menu
        )       
        
    def show_login(self):
        self.my_w_child=tk.Toplevel(root,bg="#000066")
        self.my_w_child.geometry("250x100") 
        
                # pasang Label
        Label(self.my_w_child, text='Username:',bg="#000066",fg="Snow").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(self.my_w_child, text="Password:",bg="#000066",fg="Snow").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        

        # pasang textbox
        self.txtUsername = Entry(self.my_w_child) 
        self.txtUsername.grid(row=0, column=1, padx=5, pady=5)
        
        self.txtPassword = Entry(self.my_w_child) 
        self.txtPassword.grid(row=1, column=1, padx=5, pady=5)  
        self.txtPassword.config(show='*')
                
        # Pasang Button
        self.btnLogin = tk.Button(self.my_w_child, text='Login',command=self.onLogin,bg="#CC0000",fg="snow")
        self.btnLogin.grid(row=2, column=1, padx=5, pady=5)
    
    def onLogin(self, event=None):
        u = self.txtUsername.get()
        p = self.txtPassword.get()
        A = Users()
        B =[]
        A.username = u
        A.passwd = p
        res = A.Login()
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        #messagebox.showinfo("showinfo", "status:"+status+"message:"+msg) 
        if(status=="success"):
            self.my_w_child.destroy()
            if(msg=="petugas"):
                self.menuAdmin()
           
            else:
                messagebox.showinfo("showinfo", "User Tidak Dikenal")
            
        else:
            messagebox.showinfo("showinfo", "Login Not Valid") 
        
    def onLogout(self):
        self.aturKomponen()
                    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    root = tk.Tk()
    my_str = tk.StringVar()
    aplikasi = Dashboard(root, "Aplikasi Perpustakaan")
    root.mainloop() 