from tkinter import* #it is used to create powerpul GUI Based system
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 


class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.iconbitmap("face.ico")

        #variable
        self.var_class=StringVar()
        self.var_section=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_adm_no=StringVar()
        self.var_name=StringVar()
        self.var_F_name=StringVar()
        self.var_M_name=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone_no=StringVar()
        self.var_address=StringVar()
       

        #First image
        img=Image.open(r'E:\Face Recognization Attandance System\Image\student1.jpg')
        img=img.resize((480,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=480,height=130)

        #Second Image
        img1=Image.open(r'E:\Face Recognization Attandance System\Image\student2.jpg')
        img1=img1.resize((480,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=480,y=0,width=480,height=130)

        #Third Image
        img2=Image.open(r'E:\Face Recognization Attandance System\Image\student3.jpg')
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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1370,height=45)

        main_frame=Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=10,y=60,width=1340, height=540)

        #left side label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=525)

        #left side image
        img_left=Image.open(r'E:\Face Recognization Attandance System\Image\Students.png')
        img_left=img_left.resize((630,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=630,height=130)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg='white',relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=630,height=100)

        #class
        class_label=Label(current_course_frame,text="Class",font=("times new roman",12,"bold"),bg="white")
        class_label.grid(row=0,column=0,padx=10,sticky=W)

        class_combo=ttk.Combobox(current_course_frame,textvariable=self.var_class,font=("times new roman",12,"bold"),state="readonly",width=20)
        class_combo["values"]=("Select Class","First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Nineth","Tenth")
        class_combo.current(0)
        class_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #Section
        Section_label=Label(current_course_frame,text="Section",font=("times new roman",12,"bold"),bg="white")
        Section_label.grid(row=0,column=2,padx=10,sticky=W)

        Section_combo=ttk.Combobox(current_course_frame,textvariable=self.var_section,font=("times new roman",12,"bold"),state="readonly",width=20)
        Section_combo["values"]=("Select Section","A","B","C")
        Section_combo.current(0)
        Section_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Session",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Session","2024-2025","2025-2026","2026-2027")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=20)
        Semester_combo["values"]=("Select Class","First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Nineth","Tenth")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W) 

         #Class Students Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg='white',relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=240,width=630,height=260)

        #Adm No.
        StudentID_label=Label(class_student_frame,text="Admission No.",font=("times new roman",12,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_adm_no,width=20,font=("times new roman",11,"bold"))
        studentID_entry.grid(row=0,column=1,padx=4,pady=5,sticky=W)

         #Student_Name
        Stdent_Name_label=Label(class_student_frame,text="Student_Name",font=("times new roman",12,"bold"),bg="white")
        Stdent_Name_label.grid(row=0,column=2,padx=4,sticky=W)

        Stdent_Name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=22,font=("times new roman",11,"bold"))
        Stdent_Name_entry.grid(row=0,column=3,padx=4,pady=5,sticky=W)

         #Father's Name
        Father_name_label=Label(class_student_frame,text="Father's Name",font=("times new roman",12,"bold"),bg="white")
        Father_name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Father_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_F_name,width=20,font=("times new roman",11,"bold"))
        Father_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

         #Mother's Name
        Mother_Name_label=Label(class_student_frame,text="Mother's Name",font=("times new roman",12,"bold"),bg="white")
        Mother_Name_label.grid(row=1,column=2,padx=10,sticky=W)

        Mother_Name_entry=ttk.Entry(class_student_frame,textvariable=self.var_M_name,width=22,font=("times new roman",11,"bold"))
        Mother_Name_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

         #Roll No.
        Roll_No_label=Label(class_student_frame,text="Roll No.",font=("times new roman",12,"bold"),bg="white")
        Roll_No_label.grid(row=2,column=0,padx=5,sticky=W)

        Roll_No_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll_no,width=20,font=("times new roman",11,"bold"))
        Roll_No_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

         #Gender
        Gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=2,padx=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=3,padx=5,pady=4,sticky=W)

         #DOB
        DOB_label=Label(class_student_frame,text="Date_Of_Birth",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=3,column=0,padx=5,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",11,"bold"))
        DOB_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

         #Email
        Email_label=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=3,column=2,padx=5,sticky=W)

        Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=22,font=("times new roman",11,"bold"))
        Email_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

         #Phone No
        Phone_No_label=Label(class_student_frame,text="Phone No.",font=("times new roman",12,"bold"),bg="white")
        Phone_No_label.grid(row=4,column=0,padx=5,sticky=W)

        Phone_No_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone_no,width=20,font=("times new roman",11,"bold"))
        Phone_No_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

         #Adress
        Adress_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        Adress_label.grid(row=4,column=2,padx=5,sticky=W)

        Adress_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=22,font=("times new roman",11,"bold"))
        Adress_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

       
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=185,width=620,height=25)
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=210,width=620,height=25)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=43,font=("times new roman",10,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=43,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)

        #Right side label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=670,y=10,width=650,height=525)

        img_right=Image.open(r'E:\Face Recognization Attandance System\Image\Right.png')
        img_right=img_right.resize((630,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=630,height=130)

        #search system
        Search_frame=LabelFrame(Right_frame,bd=2,bg='white',relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=630,height=70)

        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
        Search_label.grid(row=0,column=0,padx=5,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        Search_combo["values"]=("Select","Roll No","Name","Father's Name","Phone No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        Search_btn=Button(Search_frame,text="Search",width=15,font=("times new roman",10,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=3)

        ShowAll_btn=Button(Search_frame,text="ShowAll",width=15,font=("times new roman",10,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=3)

        #Table frame Search
        table_frame=Frame(Right_frame,bd=2,bg='white',relief=RIDGE)
        table_frame.place(x=5,y=210,width=630,height=290)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("class","section","year","sem","Adm No.","name","Father's name","Mother's name","roll no","gender","DOB","email","Phone No","Address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("class",text="Class")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("year",text="Session")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("Adm No.",text="Admission No")
        self.student_table.heading("name",text="Student's Name")
        self.student_table.heading("Father's name",text="Father's Name")
        self.student_table.heading("Mother's name",text="Mother's Name")
        self.student_table.heading("roll no",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("DOB",text="Date Of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("Phone No",text="Phone No.")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("class",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("Adm No.",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("Father's name",width=100)
        self.student_table.column("Mother's name",width=100)
        self.student_table.column("roll no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("Phone No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("photo",width=100)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    # ================Function decration =======================
    def add_data(self):
        if self.var_class.get() == "Select Class" or self.var_name.get() == "" or self.var_adm_no.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Sudhir@123",
                        database="face_recognizer",use_pure=True
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                                                            self.var_class.get(),
                                                            self.var_section.get(),
                                                            self.var_year.get(),
                                                            self.var_sem.get(),
                                                            self.var_adm_no.get(),
                                                            self.var_name.get(),
                                                            self.var_F_name.get(),
                                                            self.var_M_name.get(),
                                                            self.var_roll_no.get(),
                                                            self.var_gender.get(),
                                                            self.var_dob.get(),
                                                            self.var_email.get(),
                                                            self.var_phone_no.get(),
                                                            self.var_address.get(),
                                                            self.var_radio1.get()
                )
                )
                conn.commit()
                self.fetch_data()  # Refresh the table after saving
                conn.close()
                messagebox.showinfo("Success", "Data saved successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #============== fatch data ==============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sudhir@123",database="face_recognizer",use_pure=True)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #    #==============get cursor ==============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_class.set(data[0]),
        self.var_section.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_adm_no.set(data[4]),
        self.var_name.set(data[5]),
        self.var_F_name.set(data[6]),
        self.var_M_name.set(data[7]),
        self.var_roll_no.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_email.set(data[11]),
        self.var_phone_no.set(data[12]),
        self.var_address.set(data[13]),
        self.var_radio1.set(data[14])

        # =======update funtions ==============
    def update_data(self):
        if self.var_class.get() == "Select Class" or self.var_name.get() == "" or self.var_adm_no.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sudhir@123",database="face_recognizer",use_pure=True)
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Class=%s,Section=%s,Year=%s, Semester=%s,Name=%s,Father_Name=%s,Mother_Name=%s,Roll_No=%s,Gender=%s,Date_Of_Birth=%s,Email_address=%s,phone_no=%s,address=%s,PhotoSample=%s where Admission_No=%s",(
                                                                                                                                self.var_class.get(),
                                                                                                                                self.var_section.get(),
                                                                                                                                self.var_year.get(),
                                                                                                                                self.var_sem.get(),
                                                                                                                                self.var_name.get(),
                                                                                                                                self.var_F_name.get(),
                                                                                                                                self.var_M_name.get(),
                                                                                                                                self.var_roll_no.get(),
                                                                                                                                self.var_gender.get(),
                                                                                                                                self.var_dob.get(),
                                                                                                                                self.var_email.get(),
                                                                                                                                self.var_phone_no.get(),
                                                                                                                                self.var_address.get(),
                                                                                                                                self.var_radio1.get(),
                                                                                                                                self.var_adm_no.get()                   
                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Sucess","Student details sucessfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
#delete fuction
    def delete_data(self):
        if self.var_adm_no.get()=="":
            messagebox.showerror("Error","Admission No must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sudhir@123",database="face_recognizer",use_pure=True)
                    my_cursor=conn.cursor()
                    sql="delete from student where Admission_No=%s"
                    val=(self.var_adm_no.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showinfo("Delete","Sucessfully deleted student details",parent=self.root)

    #reset 
    def reset_data(self):
        self.var_class.set("Select Class")
        self.var_section.set("Select Section")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_adm_no.set("")
        self.var_name.set("")
        self.var_F_name.set("")
        self.var_M_name.set("")
        self.var_roll_no.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone_no.set("")
        self.var_address.set("")
        self.var_radio1.set("")

# ========= Generate data set or Take photo Samples ====================
    def generate_dataset(self):
        if self.var_class.get() == "Select Class" or self.var_name.get() == "" or self.var_adm_no.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sudhir@123",database="face_recognizer",use_pure=True)
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Class=%s,Section=%s,Year=%s, Semester=%s,Name=%s,Father_Name=%s,Mother_Name=%s,Roll_No=%s,Gender=%s,Date_Of_Birth=%s,Email_address=%s,phone_no=%s,address=%s,PhotoSample=%s where Admission_No=%s",(
                                                                                                                                self.var_class.get(),
                                                                                                                                self.var_section.get(),
                                                                                                                                self.var_year.get(),
                                                                                                                                self.var_sem.get(),
                                                                                                                                self.var_name.get(),
                                                                                                                                self.var_F_name.get(),
                                                                                                                                self.var_M_name.get(),
                                                                                                                                self.var_roll_no.get(),
                                                                                                                                self.var_gender.get(),
                                                                                                                                self.var_dob.get(),
                                                                                                                                self.var_email.get(),
                                                                                                                                self.var_phone_no.get(),
                                                                                                                                self.var_address.get(),
                                                                                                                                self.var_radio1.get(),
                                                                                                                                self.var_adm_no.get()==id+1                   
                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ================= Load predifiend data on face frontals from opencv =================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    # Minimum Neighbor=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                     
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGRA2GRAY)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croopeed Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed !!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()