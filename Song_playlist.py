import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
import os

music_player = Tk()
music_player.geometry("500x500")

directory = askdirectory()
os.chdir(directory)

song_list = os.listdir()

play_list = Listbox(music_player,selectmode=SINGLE)

for i in song_list:
    count = 0
    play_list.insert(count,i)
    count+=1
pygame.init()
pygame.mixer.init()


var=StringVar()
song_title=Label(music_player,textvariable=var)

def play():
    pygame.mixer.music.load(play_list.get(ACTIVE))
    var.set(play_list.get(ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()


b1 = Button(music_player,text="PLAY",command=play)
b1.place(x=150,y=250)

b2 = Button(music_player,text="STOP",command=stop)
b2.place(x=250,y=250)

b3 = Button(music_player,text="PAUSE",command=pause)
b3.place(x=250,y=350)

b4 = Button(music_player,text="RESUME",command=resume)
b4.place(x=150,y=350)


play_list.place(x=150,y=5)
song_title.pack()


music_player.mainloop()