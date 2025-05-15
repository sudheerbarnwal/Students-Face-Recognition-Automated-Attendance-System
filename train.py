from tkinter import* #it is used to create powerpul GUI Based system
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np 


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.iconbitmap("face.ico")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1370,height=45)

        img_top=Image.open(r'Image\face.png')
        img_top=img_top.resize((1400,300),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1400,height=300)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=345,width=1500,height=60)

        img_buttom=Image.open(r'Image\People.jpg')
        img_buttom=img_buttom.resize((1400,300),Image.LANCZOS)
        self.photoimg_buttom=ImageTk.PhotoImage(img_buttom)

        f_lbl=Label(self.root,image=self.photoimg_buttom)
        f_lbl.place(x=0,y=407,width=1400,height=300)


    def train_classifier(self):
        data_dir = ("Data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Convert to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])  # e.g., file name = User.1.1.jpg

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)

        # ============= Train the classifier and save ================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.save("classifier.xml")  # Use .save(), not .write()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed successfully")




        

if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()