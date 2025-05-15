from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
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
        img3=Image.open(r'Image\Login.png')
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENTS FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1370,height=45)

        frame=Frame(bg_img,bg="black")
        frame.place(x=550,y=100,width=300,height=400)

        img4=Image.open(r"Image\Get.png")
        img4=img4.resize((90,90),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img4)
        lblimg4=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg4.place(x=650,y=235,width=90,height=90)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=78,y=90)

        # Label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=145)

        self.texuser=ttk.Entry(frame,font=("times new roman",14,"bold"))
        self.texuser.place(x=40,y=175,width=220)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=215)

        self.passuser=ttk.Entry(frame,font=("times new roman",14,"bold"))
        self.passuser.place(x=40,y=245,width=220)

        #============ Icond Images =================
        img5=Image.open(r"Image\Get.png")
        img5=img5.resize((25,25),Image.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        lblimg5=Label(image=self.photoimage5,bg="black",borderwidth=0)
        lblimg5.place(x=595,y=380,width=25,height=25)

        img6=Image.open(r"Image\Lock.png")
        img6=img6.resize((25,25),Image.LANCZOS)
        self.photoimage6=ImageTk.PhotoImage(img6)
        lblimg6=Label(image=self.photoimage6,bg="black",borderwidth=0)
        lblimg6.place(x=595,y=450,width=25,height=25)

        #===========LoginButton ==============
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=95,y=290,width=120,height=35)

        #registerbutton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=17,y=330,width=150)

        #forgot password btn
        forgetbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=10,y=360,width=150)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.texuser.get()=="" or self.passuser.get()=="":
            messagebox.showerror("Error","all field requred")
        elif self.texuser.get()=="sudheer" and self.passuser.get()=="ashu":
            messagebox.showinfo("Success","Welcome to Students face recognize System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sudhir@123",database="face_recognizer",use_pure=True)
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where Email=%s and Password=%s",(
                                                                                        self.texuser.get(),
                                                                                        self.passuser.get()
                                                                            
                                                                                    ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ================= reset password =================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sudhir@123",database="face_recognizer",use_pure=True)
            my_cursor=conn.cursor()
            qery=("select * from register where Email=%s and SecurityQ=%s and SecurityA=%s")
            vlue=(self.texuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qery,vlue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the correct answer",parent=self.root2)
            else:
                query=("update register set Password=%s where Email=%s")
                value=(self.txt_newpass.get(),self.texuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, Please login with new password",parent=self.root2)
                self.root2.destroy()

    #forgot password windows
    def forgot_password_window(self):
        if self.texuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sudhir@123",database="face_recognizer",use_pure=True)
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.texuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please Enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["value"]=("Select","Your Birth Place","Your First School Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=220)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)
                
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=220)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
                
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=220)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",20,"bold"),fg="white",bg="green")
                btn.place(x=120,y=290)


# Registration Code
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #===========variables ============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #=========Background Image ================
        self.bg=ImageTk.PhotoImage(file=r"Image\1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file=r"Image\nature.jpg")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=50,y=100,width=485,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=535,y=100,width=700,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #===============label entry =======================
        #--------------- row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=220)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=220)

        #---------------- row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=220)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=220)

        #----------------row3
        security_Q=Label(frame,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["value"]=("Select","Your Birth Place","Your First School Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=220)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Select Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=220)

        #----------------- row4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=220)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=220)

        #=============== checkbutton==============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #===============buttons==============
        img=Image.open(r"Image\Register.png")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=50,y=420,width=200)

        img1=Image.open(r"Image\LogIn Now.jpeg")
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white")
        b2.place(x=370,y=420,width=200)

    #===============Function declaration ====================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & confirm Password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sudhir@123",database="face_recognizer",use_pure=True)
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row !=None:
                messagebox.showerror("Error","Your have already Registered & Try another Email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully",parent=self.root)
            self.root.destroy()

    def return_login(self):
        self.root.destroy()





if __name__ == "__main__":
    main()
