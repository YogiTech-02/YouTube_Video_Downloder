from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox,filedialog
import pytube as pt
import shutil


def select_path():
    path = filedialog.askdirectory()
    lbl_path.config(text=path)

def download():
    get_link = e_link.get()
    user_path = lbl_path.cget(str("text"))
    quality = cb_qua.get()
    if(quality=="MP4 360"):
         con = pt.YouTube(get_link).streams[1].download()

    elif(quality=="MP4 144"):
         con = pt.YouTube(get_link).streams[0].download()  

    elif(quality=="MP4 720"):
         con = pt.YouTube(get_link).streams[2].download()    
    else:
        messagebox.showerror("Download","Something Went Wrong")

    shutil.move(con, user_path)
    messagebox.showinfo("Download","Downloading Complete.")


    
win=Tk()
win.state("zoomed")
win.configure(bg="lightblue")


lbl_title=Label(win,text="YouTube Video Download",bg="lightblue",font=("title",50,"bold"))
lbl_title.pack()

lbl_link=Label(win,text="Paste your video link here",bg="lightblue",font=("arial",25,"bold"))
lbl_link.place(relx=.03,rely=.3)


e_link=Entry(win,font=('arial',20),bd=3)
e_link.place(relx=.35,rely=.3,relheight=.08,relwidth=.5)
e_link.focus()

lbl_path=Label(win,text="Select Path For Download",bg="lightblue",font=("arial",25,"bold"))
lbl_path.place(relx=.03,rely=.45)

btn_path=Button(win,text="Select Path",command=select_path,font=('arial',20,'bold'),bd=3)
btn_path.place(relx=.35,rely=.45)


lbl_qua=Label(win,text="Choose your video quality",bg="lightblue",font=("arial",25,"bold"))
lbl_qua.place(relx=.03,rely=.6)


cb_qua=Combobox(win,values=['MP4 144','MP4 360','MP4 720'],font=("arial",25))
cb_qua.current(1)
cb_qua.place(relx=.35,rely=.6,relheight=.08,relwidth=.5)


btn_dw=Button(win,text="Download",command=download,font=('arial',20,'bold'),bd=3)
btn_dw.place(relx=.45,rely=.75)

win.mainloop()
