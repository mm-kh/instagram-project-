from tkinter import *
import instaloader
import urllib
from urllib.request import urlopen
from PIL import Image , ImageTk
import io


def show_image():
    l=instaloader.Instaloader()
    profile=instaloader.Profile.from_username(l.context , f"{username.get()}")
    a=urlopen(profile.get_profile_pic_url())
    data=a.read()
    a.close()
    image=Image.open(io.BytesIO(data))
    pic=ImageTk.PhotoImage(image)
    label.config(image=pic)
    label.image=pic
    label.pack()



window=Tk()
window.title("profile picture downloader")
window.geometry("600x600")

Label(window , text="enter instagram username" ,fg="blue").pack()


username=Entry(window , width=50)
username.pack()

Button(window , text="start download" , fg="black" , bg="gray" , command=show_image).pack()

label=Label(window)
Label(window , text="written by mm_khani" , fg="blue").place(x=250 , y=550)
window.mainloop()