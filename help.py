from tkinter import* #it is used to create powerpul GUI Based system
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.iconbitmap("face.ico")

        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1370,height=55)

        img_top=Image.open(r'Image\dev1.jpg')
        img_top=img_top.resize((1400,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1400,height=700)

        dev_label=Label(f_lbl,text="Email: sudheerbarnwal470@gmail.com",font=("times new roman",25,"bold"),bg="white",fg="blue")
        dev_label.place(x=430,y=50)


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()