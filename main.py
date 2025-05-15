from tkinter import* #it is used to create powerpul GUI Based system
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
from Students import student
import os
from train import Train
from face_recognition import Face_Recognition
from Attandace import Attandance_data
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.iconbitmap("face.ico")

        #First image
        img=Image.open(r'E:\Face Recognization Attandance System\Image\School.jpeg')
        img=img.resize((480,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=480,height=130)

        #Second Image
        img1=Image.open(r'E:\Face Recognization Attandance System\Image\Face recognition.png')
        img1=img1.resize((480,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=480,y=0,width=480,height=130)

        #Third Image
        img2=Image.open(r'E:\Face Recognization Attandance System\Image\Right.png')
        img2=img2.resize((480,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=960,y=0,width=400,height=130)
        
        #background imag3
        img3=Image.open(r'E:\Face Recognization Attandance System\Image\Background.jpg')
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENTS FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1370,height=45)

        #============Time ==================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #students button
        img4=Image.open(r'E:\Face Recognization Attandance System\Image\students photo.jpg')
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=80,width=220,height=220)

        b1_1=Button(bg_img,text="Students details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=280,width=220,height=40)

        #Detect Face button
        img5=Image.open(r'E:\Face Recognization Attandance System\Image\Face Detector.jpg')
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=80,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=280,width=220,height=40)

         #Attendance
        img6=Image.open(r'E:\Face Recognization Attandance System\Image\Attendance.jpeg')
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attandance_data)
        b1.place(x=700,y=80,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attandance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=280,width=220,height=40)

        #Help Desk
        img7=Image.open(r'E:\Face Recognization Attandance System\Image\Help desk.jpeg')
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=80,width=220,height=220)

        b1_1=Button(bg_img,text="Helf Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=280,width=220,height=40)

          #Train Data
        img8=Image.open(r'E:\Face Recognization Attandance System\Image\Train Data.jpg')
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=330,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=530,width=220,height=40)


       #Photo
        img9=Image.open(r'E:\Face Recognization Attandance System\Image\Photo.jpg')
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=330,width=220,height=220)

        b1_1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=530,width=220,height=40) 

        #Developer
        img10=Image.open(r'E:\Face Recognization Attandance System\Image\Developer.jpg')
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=330,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=530,width=220,height=40)  

         #Exit
        img11=Image.open(r'E:\Face Recognization Attandance System\Image\exit.jpeg')
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=330,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=530,width=220,height=40)  

    def open_img(self):
        os.startfile("Data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    # =============Fuction buttons===============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attandance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attandance_data(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()