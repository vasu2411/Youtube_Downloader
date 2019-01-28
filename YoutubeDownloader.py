import tkinter.filedialog
from tkinter import *
from pytube import YouTube
from tkinter import messagebox

class Application(Frame):
    downloadPath = "E:/"
    downloadURL = ""
    downloadTitle = ""
    t2 = ""
    t1 = ""
    li1 = ""
    loop_active = True

    # initialization
    def __init__(self, master=None):
        Frame.__init__(self, master)
        root.title("Youtube Downloader")
        root.wm_iconbitmap("icon.ico")
        self.grid()
        self.addWidgets()

    # add widgets to the window
    def addWidgets(self):
        # label for enter video url
        l1 = Label(root, text="Video URL")
        l1.grid(row=0, column=0)

        # text box to enter video url
        global t1
        t1 = Entry(root, width="76")
        t1.grid(row=0, column=1, columnspan=10)

        # label to enter download path
        l2 = Label(root, text="Download Path")
        l2.grid(row=3, column=0)

        # text box to enter download path
        global t2
        t2 = Entry(root, width="59")
        t2.grid(row=3, column=1, columnspan=9)
        t2.insert(0, self.downloadPath)

        # button to change download path
        b1 = Button(root, text="Change", width="11", command=self.changeDirectory)
        b1.grid(row=3, column=10)

        # button to download best quality
        b2 = Button(root, text="Download Best", command=lambda: self.download("video", "best"))
        b2.grid(row=6, column=0)

        # button to download 144p quality
        b3 = Button(root, text="Download 144p", command=lambda: self.download("video", "144p"))
        b3.grid(row=6, column=2)

        # button to download 240p quality
        b4 = Button(root, text="Download 240p", command=lambda: self.download("video", "240p"))
        b4.grid(row=6, column=4)

        # button to download 360p quality
        b5 = Button(root, text="Download 360p", command=lambda: self.download("video", "360p"))
        b5.grid(row=6, column=6)

        # button to download 720p quality
        b6 = Button(root, text="Download 720p", command=lambda: self.download("video", "720p"))
        b6.grid(row=6, column=8)

        # button to download audio only
        b7 = Button(root, text="Download Audio", command=lambda: self.download("audio", ""))
        b7.grid(row=6, column=10)

        # label for logs
        l3 = Label(root, text="Logs:")
        l3.grid(row=8, column=0)

        # listbox for logs
        global li1
        li1 = Listbox(root, width=92, height=12)
        li1.grid(row=9, column=0, columnspan=11, rowspan=2)

        # button to exit
        b8 = Button(root, text="Exit", width=11, command=exit)
        b8.grid(row=12, column=10)

    # let user to change download path
    def changeDirectory(self):
        global downloadPath
        downloadPath = tkinter.filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')
        t2.delete(0, END)
        t2.insert(0, downloadPath)

    # close application
    def exit(self):
        root.destroy()

    # download function
    def download(self, type, quality):
        global li1, downloadURL, downloadPath

        def callback():
            if (type == "audio"):
                self.downloadURL = t1.get()
                if not t1.get():
                    li1.insert(END, "You entered an invalid URL")
                    messagebox.showinfo("Error", "Please enter valid youtube video URL")
                else:
                    try:
                        yt = YouTube(self.downloadURL)
                        global downloadTitle
                        downloadTitle = yt.title
                        yt.register_on_complete_callback(convert_to_aac)
                        stream = yt.streams.filter(only_audio=True).all()
                        stream[0].download(self.downloadPath)
                    except Exception as e:
                        li1.insert(END,str(e))

            else:
                if not t1.get():
                    li1.insert(END, "You entered an invalid URL")
                    messagebox.showinfo("Error", "Please enter valid youtube video URL")
                else:
                    try:
                        self.downloadURL = t1.get()
                        yt = YouTube(self.downloadURL)
                        downloadTitle = yt.title
                        yt.register_on_complete_callback(convert_to_aac)
                        stream = yt.streams.all()

                        if quality == "144p":
                            for item in stream:
                               if item.resolution == '144p':
                                   item.download(self.downloadPath)
                                   break

                        elif quality == "240p":
                           for item in stream:
                              if item.resolution == '240p':
                                   item.download(self.downloadPath)
                                   break

                        elif quality == "360p":
                            for item in stream:
                                if item.resolution == '360p':
                                    item.download(self.downloadPath)
                                    break

                        elif quality == "720p":
                            for item in stream:
                                if item.resolution == '720p':
                                    item.download(self.downloadPath)
                                    break

                        else:
                            stream = yt.streams.first()
                            stream.download(self.downloadPath)

                    except Exception as e:
                        li1.insert(END,str(e))

        # function to be called on completion of download
        def convert_to_aac(stream, file_handle):
            li1.insert(END, downloadTitle + " downloaded to: " + self.downloadPath)

        if t1.get():
            li1.insert(END, "Downloading " + t1.get())
        root.after_idle(callback)


root = Tk()
app = Application(master=root)
app.mainloop()