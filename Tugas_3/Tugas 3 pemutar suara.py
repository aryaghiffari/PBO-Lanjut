from tkinter import*
import tkinter as tk
from tkinter import filedialog
from pygame import mixer


class Music:
    def __init__(self,win) -> None:
        win.geometry ('200x200')
        win.title ('Pemutar Suara')
        
        mainmenu = Menu()
        win.config(menu=mainmenu)
        load_menu=Menu(mainmenu)
        
        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')

        load_menu = Menu(mainmenu,tearoff=False)
        load_menu.add_command(label='Pilih Folder', command=self.load)
        mainmenu.add_cascade(label='Menu',menu=load_menu)
        play_button = Button(win,textvariable=self.play_restart, width=10, font=('Arial,20'),command=self.play)
        play_button.place(x=100, y=80,anchor='center')
        pause_button = Button(win,textvariable=self.pause_resume, width=10, font=('Arial,20'),command=self.pause)
        pause_button.place(x=100, y=120,anchor='center')

        self.music = False
        self.playing_state = False
        
    def load(self):
        self.music_file = filedialog.askopenfilename()
        print('loaded :',self.music_file)
        self.play_restart.set('play')

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(str(self.music_file))
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('restart')
            self.pause_resume.set('Pause')

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('resume')
        else:
            mixer.music.unpause()
            self.playing_state= False
            self.pause_resume.set('pause')
     
root=Tk()
Music(root)
root.mainloop()