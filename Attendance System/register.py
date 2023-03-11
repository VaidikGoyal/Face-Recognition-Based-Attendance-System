from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("New User Register")
        self.root.geometry("1536x850+0+0")

        ##############variable#################
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=StringVar()
        self.var_radio1=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\yashj\Desktop\minor\01.png")

        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame= Frame(self.root,bg="white") 
        frame.place(x=418,y=125,width=700,height=550)   
        
        register_lb1=Label(frame,text="Register Here",font=("time new roman",24,"bold"),fg="steelblue")
        register_lb1.place(x=20,y=20)

        

        ############label and entry

        fname=Label(frame,text="First Name",font=("time new roman",16,"bold"),bg="white")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("time new roman",16,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("time new roman",16,"bold"),bg="white")
        lname.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("time new roman",16,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Student ID",font=("time new roman",16,"bold"),bg="white")
        contact.place(x=50,y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("time new roman",16,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("time new roman",16,"bold"),bg="white")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("time new roman",16,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        sec=Label(frame,text="Select Security Question",font=("time new roman",16,"bold"),bg="white")
        sec.place(x=50,y=240)
        self.combo_sec=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("time new roman",15,"bold"),state="readonly")
        self.combo_sec["values"]=("Select","Your Birth Place","Your Pet Name","Favourite Sport")
        self.combo_sec.place(x=50,y=270,width=250)
        self.combo_sec.current(0)

        
        sec_an=Label(frame,text="Security Answer",font=("time new roman",16,"bold"),bg="white")
        sec_an.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("time new roman",16,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        password=Label(frame,text="Password",font=("time new roman",16,"bold"),bg="white")
        password.place(x=50,y=310)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_pass,font=("time new roman",16,"bold"))
        self.txt_contact.place(x=50,y=340,width=250)

        cnf_pas=Label(frame,text="Confirm Password",font=("time new roman",16,"bold"),bg="white")
        cnf_pas.place(x=370,y=310)
        self.txt_pass=ttk.Entry(frame,textvariable=self.var_confpass,font=("time new roman",16,"bold"))
        self.txt_pass.place(x=370,y=340,width=250)

        radiobtn1=ttk.Radiobutton(frame,variable=self.var_radio1, text="Register as Admin", value="yes")
        radiobtn1.place(x=50,y=380,width=150)

        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("time new roman",16,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=410)


        
        registerbtn=Button(frame,command=self.register_data,text="Register",font=("time new roman",16,"bold"),bd=3,relief=RIDGE,bg="steelblue",cursor="hand2",fg="white")
        registerbtn.place(x=100,y=470,width=200,height=50)

        loginbtn=Button(frame,command=self.loginBtn,text="Login",font=("time new roman",16,"bold"),bd=3,relief=RIDGE,bg="springgreen",cursor="hand2",fg="white")
        loginbtn.place(x=375,y=470,width=200,height=50)


    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_securityA.get()=="" or self.var_securityQ.get()=="Select" or self.var_contact.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
            my_cursor= conn.cursor()
            query=("select * from register where email=%s or Student_id=%s")
            value=(self.var_email.get(),self.var_contact.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email id or Student id is already register",parent=self.root)
            else:
                my_cursor.execute("Insert into register value(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_contact.get(),
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_pass.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_radio1.get()
                                                                                                          ))
                conn.commit()
                conn.close()
                
                messagebox.showinfo("Success","Register Successfully")
                self.root.destroy()
                
    def loginBtn(self):
        self.root.destroy()










if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()