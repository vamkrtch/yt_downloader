from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

screen = Tk()
title = screen.title("Youtube Download")
canvas = Canvas(screen, width=500,height=500)
canvas.pack()

def path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def __download__():
    get_lnk = link_space.get()
    user_path = path_label.cget("text")
    mp4_v = YouTube(get_lnk).streams.get_highest_resolution().download()
    result = VideoFileClip(mp4_v)
    result.close()


logo = PhotoImage(file="YT.png")
logo_resize = logo.subsample(10,10)
canvas.create_image(250,80,image=logo_resize)

link_space = Entry(screen,width=50)
link_text = Label(screen, text="Enter Download link ")

canvas.create_window(250, 200, window=link_space)
canvas.create_window(250, 170, window=link_text)

path_label = Label(screen, text="Select Folder for saving space")
path_select_button = Button(screen, text="Save As",command=path)

canvas.create_window(250, 250, window=path_label)
canvas.create_window(250, 300, window=path_select_button)

download_butt = Button(screen, text="Download Video",command=__download__)
canvas.create_window(250, 350, window=download_butt)

screen.mainloop()
