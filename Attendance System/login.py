from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from main import Face_Recognition_System
from student_access import Student_Access

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("login")
        self.root.geometry("1536x850+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\yashj\Desktop\minor\01.png")

        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = LabelFrame(self.root,bd=2,bg="white", relief=RIDGE)
        frame.place(x=598,y=175,width=340, height=450)

        img1= Image.open(r"C:\Users\yashj\Desktop\minor\log.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        lbImage1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbImage1.place(x=720,y=175,width=100, height=100)

        Get_str= Label(frame,text="Get Started",font=("time new roman",18,"bold"))
        Get_str.place(x=100,y=100)

        #label username
        username = lb1 = Label(frame,text="Username",font=("time new roman",12,"bold"),bg="white")
        username.place(x=25,y=155)

        self.txtuser=ttk.Entry(frame,font=("time new roman",14,"bold"))
        self.txtuser.place(x=20,y=180,width=295)

        password = lb1 = Label(frame,text="Password",font=("time new roman",12,"bold"),bg="white")
        password.place(x=25,y=225)

        self.txtpass=ttk.Entry(frame,font=("time new roman",14,"bold"))
        self.txtpass.place(x=20,y=250,width=295)

        #login

        loginbtn=Button(frame,command=self.login,text="Login",font=("time new roman",16,"bold"),bd=3,relief=RIDGE,bg="steelblue",cursor="hand2",fg="white")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register
        registerbtn=Button(frame,command=self.register_window,text="Register",borderwidth=0,font=("time new roman",11,"bold"),relief=RIDGE,bg="white",fg="black",cursor="hand2",activebackground="white")
        registerbtn.place(x=10,y=350,width=120)

        #forget 
        forgetbtn=Button(frame,command=self.forget_password_window,text="Forget Password",borderwidth=0,font=("time new roman",10,"bold"),relief=RIDGE,bg="white",fg="black",cursor="hand2",activebackground="white")
        forgetbtn.place(x=10,y=375,width=160)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
            if(self.txtuser.get()=="" or self.txtpass.get()==""):
                messagebox.showerror("Error","All fields are Required")
            else:
                conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
                my_cursor= conn.cursor()
                my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get()
                                                                                            ))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid username and password")
                else:
                    
                    if "yes" in row:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                    else:
                        
                        self.new_window=Toplevel(self.root)
                        self.app=Student_Access(self.new_window)
    

    def resetpassword(self):
        if self.combo_sec.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter Secutity Answer",parent=self.root2)
        elif self.txt_pass()=="":
            messagebox.showerror("Error","Please Enter new Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
            my_cursor= conn.cursor()
            qry=("select * from register where email=%s and securityQ=%s and securityA=%s")
            val=(self.txtuser.get(), self.combo_sec.get(),self.txt_security.get())
            my_cursor.execute(qry,val)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter Correct Security Answer",parent=self.root2)
            else:
                query=("update register set password =%s where email=%s")
                value=(self.txt_pass.get(),self.get.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been reset Successfully", parent=self.root2)
                self.root2.destroy()


        


    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
            my_cursor= conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")    
                self.root2.geometry("340x450+598+175")

                l=Label(self.root2,text="Forget Password",font=("time new roman",18,"bold"))
                l.place(x=0,y=10,relwidth=1)

                sec=Label(self.root2,text="Select Security Question",font=("time new roman",16,"bold"),bg="white")
                sec.place(x=50,y=80)
                self.combo_sec=ttk.Combobox(self.root2,font=("time new roman",15,"bold"),state="readonly")
                self.combo_sec["values"]=("Select","Your Birth Place","Your Pet Name","Favourite Sport")
                self.combo_sec.place(x=50,y=110,width=250)
                self.combo_sec.current(0)

                
                sec_an=Label(self.root2,text="Security Answer",font=("time new roman",16,"bold"),bg="white")
                sec_an.place(x=50,y=150)
                self.txt_security=ttk.Entry(self.root2,font=("time new roman",16,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                password=Label(self.root2,text="New Password",font=("time new roman",16,"bold"),bg="white")
                password.place(x=50,y=220)
                self.txt_pass=ttk.Entry(self.root2,font=("time new roman",16,"bold"))
                self.txt_pass.place(x=50,y=250,width=250)

                resetbtn=Button(self.root2,command=self.resetpassword,text="Reset",font=("time new roman",16,"bold"),bd=3,relief=RIDGE,bg="steelblue",cursor="hand2",fg="white")
                resetbtn.place(x=50,y=300,width=250,height=50)



if __name__ == "__main__":
    main()