from tkinter import* #it is used to create powerpul GUI Based system
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1370,height=45)

        img_top=Image.open(r'Image\dev.jpg')
        img_top=img_top.resize((1400,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1400,height=700)

    

        img_top1=Image.open(r'Image\Sudheer.jpg')
        img_top1=img_top1.resize((230,200),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(f_lbl,image=self.photoimg_top1)
        f_lbl.place(x=650,y=0,width=230,height=200)

         #Developer Info
        dev_label=Label(f_lbl,text="Hello, My name is Sudheer",font=("times new roman",14,"bold"),bg="blue",fg="white")
        dev_label.place(x=0,y=150)

        dev_label=Label(f_lbl,text="I am full stack developer",font=("times new roman",14,"bold"),bg="blue",fg="white")
        dev_label.place(x=0,y=175)

       
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()