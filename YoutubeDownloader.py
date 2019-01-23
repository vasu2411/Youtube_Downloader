from tkinter import *
from pytube import YouTube

window=Tk()

#label for enter video url
l1 = Label(window, text="Video URL")
l1.grid(row=0,column=0)

#text box to enter video url
t1 = Entry(window,width="76")
t1.grid(row=0,column=1,columnspan=10)

#label to enter download path
l2 = Label(window, text="Download Path")
l2.grid(row=3,column=0)

#text box to enter download path
t2 = Entry(window,width="59")
t2.grid(row=3,column=1,columnspan=9)

#button to change download path
b1 = Button(window,text="Change",width="11")
b1.grid(row=3,column=10)

#button to download best quality
b2 = Button(window,text="Download Best")
b2.grid(row=6,column=0)

#button to download 144p quality
b3 = Button(window,text="Download 144p")
b3.grid(row=6,column=2)

#button to download 240p quality
b4 = Button(window,text="Download 240p")
b4.grid(row=6,column=4)

#button to download 360p quality
b5 = Button(window,text="Download 360p")
b5.grid(row=6,column=6)

#button to download 720p quality
b6 = Button(window,text="Download 720p")
b6.grid(row=6,column=8)

#button to download audio only
b7 = Button(window,text="Download Audio")
b7.grid(row=6,column=10)

#label for logs
l3 = Label(window,text="Logs:")
l3.grid(row=8,column=0)

#listbox for logs
li1 = Listbox(window,width=92,height=12)
li1.grid(row=9,column=0,columnspan=11,rowspan=2)

#button to exit
b8 = Button(window,text="Exit",width=11)
b8.grid(row=12,column=10)

window.mainloop()