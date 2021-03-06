from tkinter import *
from PIL import Image, ImageTk 
import re
import os
from pytube import YouTube
root = Tk()
root.geometry('1000x500')
root.resizable(0,0)
tgt_folder = "Videos"
load = Image.open("Utilities\download_mp4_button.png")
load = load.resize((150, 50), Image.ANTIALIAS)
mp4image = ImageTk.PhotoImage(load)
load = Image.open("Utilities\downloadmp3.png")
load = load.resize((150, 50), Image.ANTIALIAS)
mp3image = ImageTk.PhotoImage(load)
load = Image.open("Utilities\Logo_Thing.png")
load = load.resize((796, 112), Image.ANTIALIAS)
logoting = ImageTk.PhotoImage(load)
load = Image.open("Utilities\Search_Bar.png")
load = load.resize((700, 50), Image.ANTIALIAS)
searchbar = ImageTk.PhotoImage(load)
search = Label(root, image=searchbar, bg = "SteelBlue4")
search.image = searchbar


#text

root.title("YouTube Downloader")
root.configure(bg= "SteelBlue4")
Label(root,image = logoting, font ='arial 10 bold', bg = "SteelBlue4").pack()

#download video function 

def downloadvideo ():
    
    url = YouTube(str(link.get()))
    w = url.streams.first()
    w.download(output_path="Videos")
    Label(root, text = 'Video Downloaded! Check the folder where you installed this exe. ', font = 'arial 10', bg = "SteelBlue4").place(x= 300, y = 310)  
def downloadaudio ():
    url = YouTube(str(link.get()))
    v= url.streams.filter(only_audio=True).all()
    v[0].download(output_path="Videos")
    Label(root, text = 'Audio Downloaded! Check the folder where you installed this exe. ', font = 'arial 10', bg = "SteelBlue4").place(x= 300, y = 310)  

#button and entry box
Button(root,image = mp4image, font = 'arial 15 bold' ,bg = 'SteelBlue4', activebackground = "SteelBlue4", padx = 2, borderwidth=0, command = downloadvideo).place(x=411 ,y = 200)
Button(root,image=mp3image, font = 'arial 15 bold' ,bg = 'SteelBlue4', padx = 2, activebackground="SteelBlue4",  borderwidth = 0,command = downloadaudio).place(x=415 ,y = 250)


link = StringVar()
search.place(x = 140, y = 142.5)
link_enter = Entry(root, borderwidth = 0, width = 70,textvariable = link).place(x = 280, y = 160)



root.mainloop()
