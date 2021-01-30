from pytube import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
from tkinter import *
# total file size container
file_size=0

# for updating percentage
def progress(stream=None,chunk=None,file_handle=None,remaining=None):
    file_downloaded=(file_size-file_handle)
    per=float((file_downloaded/file_size)*100)
    dbtn.config(text="{:00.0f}% downloaded".format(per))



def startDownload():
    global file_size

    url=urlField.get()
    print(url)
    dbtn.config(text="Loading...")
    dbtn.config(state=DISABLED)
        # url = "https://www.youtube.com/watch?v=CbPGkNPYt6w"
        # path_to_save_vid = "C:\\Users\\nikit\\Downloads"
    path_to_save_vid = askdirectory()
    print(path_to_save_vid)
        # if path_to_save_vid is None:
        #     return

        # creating youtube obj wid url
    ob = YouTube(url)
    ob = YouTube(url,on_progress_callback=progress)


        # to fetch the all streams
        # strms=ob.streams.all()
        # for s in strms:
        #     print(s)

        # to extract data of that vid
    strm = ob.streams.first()
    file_size=strm.filesize
    # print(file_size)
    # print(int(file_size))
    # vTitle.config(text=strm.title)
    # vTitle.pack(side=TOP)
        # print(strm.filesize)
        # print(strm.title)
        # print(ob.description)

        # to download vid
    strm.download(path_to_save_vid)
    print("done....")
    dbtn.config(text="Download")
    print("Successfully Downloaded....")
    dbtn.config(state=NORMAL)
    showinfo("Finished downloading","Successfully Downloaded")
    urlField.delete(0,END)
    # vTitle.pack_forget()


    # except Exception as e:
    #     print(e)
    #     print("Sorry error!")

# create a thread
def startDownloadThread():
    thread=Thread(target=startDownload)
    thread.start()

# building GUI
root=Tk()
root.config(bg="#BA5C7D")
root.title("My YouTube Downloader")
root.iconbitmap("gui/pikachu.ico")
root.geometry("500x600")

# heading icon
obj=PhotoImage(file='gui/pikachu.png')
headingIcon=Label(root,image=obj)
headingIcon.pack(side=TOP)
# url textfield
urlField=Entry(root,font=("verdana 15"),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)
# download button
dbtn = Button(root,text="Download",font=("Verdana,18"),relief='ridge',command=startDownloadThread)
dbtn.config(bg="#701334")
dbtn.config(fg="white")
dbtn.pack(side=TOP,pady=10)

# video title
# vTitle=Label(root,text="video title")


root.mainloop()
# https://www.youtube.com/watch?v=scZD2Fx_nBo
