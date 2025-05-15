from tkinter import* #it is used to create powerpul GUI Based system
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np 

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.iconbitmap("face.ico")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="yellow",fg="green")
        title_lbl.place(x=0,y=0,width=1370,height=45)

        #1st Image
        img_top=Image.open(r'Image\Face Detector.jpg')
        img_top=img_top.resize((650,650),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=48,width=650,height=650)

        #2nd Image
        img_buttom=Image.open(r'Image\face_recognition.png')
        img_buttom=img_buttom.resize((750,650),Image.LANCZOS)
        self.photoimg_buttom=ImageTk.PhotoImage(img_buttom)

        f_lbl=Label(self.root,image=self.photoimg_buttom)
        f_lbl.place(x=650,y=48,width=750,height=650)

        #button
        b1_1=Button(f_lbl,text="TRAIN DATA",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="green",fg="white")
        b1_1.place(x=272,y=575,width=200,height=40)

    # ============== attendance ====================
    def mark_attendance(self,a,r,n,c):
        with open("sudheer.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((a not in name_list) and (r not in name_list) and (n not in name_list) and (c not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{a},{r},{n},{c},{dtString},{d1},Present")



    # =============face recognition ===============
    
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))  # or 100 - predict

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Sudhir@123",
                    database="face_recognizer", use_pure=True)
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Admission_No = %s", (id,))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else ""

                my_cursor.execute("SELECT Roll_No FROM student WHERE Admission_No = %s", (id,))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else ""

                my_cursor.execute("SELECT Class FROM student WHERE Admission_No = %s", (id,))
                c = my_cursor.fetchone()
                c = "+".join(c) if c else ""

                my_cursor.execute("SELECT Admission_No FROM student WHERE Admission_No = %s", (id,))
                a = my_cursor.fetchone()
                a = "+".join(a) if a else ""

                if confidence > 77:
                    cv2.putText(img, f"ID: {a}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.putText(img, f"Class: {c}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    self.mark_attendance(a,r,n,c)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Train data first. classifier.xml not found.")
            return

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key to exit
                break

        video_cap.release()  # ✅ fixed typo here
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()