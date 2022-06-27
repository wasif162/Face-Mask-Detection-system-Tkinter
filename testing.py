from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import time
import webbrowser
import sys
import random
import PySimpleGUI as sg

def camera_scanning():
    import ImgRecongnizer
def local():
    import local
    local.main()
def alg():
    webbrowser.open_new("https://colab.research.google.com/drive/1FQeCEIlEngnltd8KeiXyOQC1PNSUdIFf#scrollTo=45x3Cr81Mnt_")
def fb():
    webbrowser.open_new("https://www.facebook.com/")
def gmail():
    webbrowser.open_new("https://mail.google.com/mail/")
root=Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry("990x550")
root.title("Masked Facial Recognition")
#root.attributes('-fullscreen', True)
color = "Silver"
color2 = "#0a2f49"
color3 = "#196f90"
color4 = '#11517c'
root.configure(bg=color3)
total_cost=0
frame = Frame(root, width=200, height=100)
#frame.place(x=560,y=500)
frame.pack()
frame.place( relx=0.5, rely=0.5,x=-210,y=-217)
img = ImageTk.PhotoImage(Image.open("www.jpg"))

label = Label(frame, image = img)

label.pack()
##scanned Items settings


# ==========================FRAMES=========================
# ======================menu-options on the left frame=============================

Email_k_btn_btm_frame = Button(root, text="SIGN IN AS GMAIL", width=17,height=2,bg=color4,bd=7,relief=RAISED,font=("Candra", 8,"bold") ,fg=color, command=lambda:gmail())
Email_k_btn_btm_frame.place(x=560, y=330)
Facebook_k_btn_btm_frame = Button(root, text="SIGN IN AS FACEBOOK", width=17,height=2,bg=color4,bd=7,relief=RAISED,font=("Candra", 8,"bold") ,fg=color, command=lambda:fb())
Facebook_k_btn_btm_frame.place(x=320, y=330)

camera_k_btn_btm_frame = Button(root, text="Camera Scanning", width=17,height=2,bg=color4,bd=7,relief=RAISED,font=("Candra", 8,"bold") ,fg=color, command=lambda:camera_scanning())
camera_k_btn_btm_frame.place(x=560, y=400)
alg_k_btn_btm_frame = Button(root, text="Attached file via Gdrive", width=17,height=2,bg=color4,bd=7,relief=RAISED,font=("Candra", 8,"bold") ,fg=color, command=lambda:alg())
alg_k_btn_btm_frame.place(x=320, y=400)
file_k_btn_btm_frame = Button(root, text="Attached File", width=17,height=2,bg=color4,bd=7,relief=RAISED,font=("Candra", 8,"bold") ,fg=color, command=lambda:local())
file_k_btn_btm_frame.place(x=430, y=480)

# ============================TITLE on top FRAME=======================
label_show = Label(root, text="Masked Facial Recongnition", bd=7, relief=RIDGE, width=35, height=2,
                   font=("Times", 12, "bold", "italic"), bg=color4, fg=color).place(x=360, y=0)


root.mainloop()

