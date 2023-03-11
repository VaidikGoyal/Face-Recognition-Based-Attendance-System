from tkinter import *
from tkinter import ttk
import types
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x1080+0+0")
        self.root.title("Student Detail")

        #variable Declaration
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()
        self.var_radio2=StringVar()




        # # Mits Logo
        # img=Image.open(r"C:\Users\yashj\Desktop\minor\logo.jpg")
        # img=img.resize((150,150),Image.ANTIALIAS)
        # self.photoimg = ImageTk.PhotoImage(img)

        # f_label = Label(self.root, image=self.photoimg)
        # f_label.place(x=0,y=0,width=150, height=150)

        # #Topic
        # img1=Image.open(r"C:\Users\yashj\OneDrive\Pictures\Saved Pictures\01.jpg")
        # img1=img1.resize((1500,150),Image.ANTIALIAS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)

        # f_label1 = Label(self.root, image=self.photoimg1)
        # f_label1.place(x=150,y=0,width=1500, height=150)

        # #Submitted by
        # img2=Image.open(r"C:\Users\yashj\OneDrive\Pictures\Saved Pictures\345330.jpg")
        # img2=img2.resize((200,200),Image.ANTIALIAS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)

        # f_label2 = Label(self.root, image=self.photoimg2)
        # f_label2.place(x=1700,y=0,width=200, height=150)
        
        title_label1 = Label(self.root, text="Student Details",font=("times new roman",32,"bold"),bg="darkseagreen",fg="white")
        title_label1.place(x=0,y=0,width=1536,height=45)

        go_back=Image.open(r"C:\Users\yashj\Desktop\minor\back.png")
        go_back=go_back.resize((50,50),Image.ANTIALIAS)
        self.photoback = ImageTk.PhotoImage(go_back)

        back_sample_btn = Button(title_label1,command=self.goback,image=self.photoback,width=32, font=("time new roman",13,"bold"),bg="darkseagreen")
        back_sample_btn.place(x=0,y=0, width=45,height=45)

        
        bck=Image.open(r"C:\Users\yashj\OneDrive\Pictures\Saved Pictures\01.png")
        bck=bck.resize((1900,1080),Image.ANTIALIAS)
        self.photobck = ImageTk.PhotoImage(bck)

        f_label3 = Label(self.root, image=self.photobck)
        f_label3.place(x=0,y=45,width=1536, height=850)

        
        #frame
        main_frame = Frame(f_label3, bd=2,bg="white" )
        main_frame.place(x=18,y=75,width=1500, height=600)

        #left label frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730, height=580)

        # img4=Image.open(r"C:\Users\yashj\Pictures\Saved Pictures\345330.jpg")
        # img4=img4.resize((1900,1080),Image.ANTIALIAS)
        # self.photoimg4 = ImageTk.PhotoImage(img4)

        # f_label3 = Label(left_frame, image=self.photoimg3)
        # f_label3.place(x=5,y=0,width=720, height=130)

        #current course Frame
        current_c = LabelFrame(left_frame,bd=2,bg="white", relief=RIDGE, text="Current Course", font=("times new roman",12,"bold"))
        current_c.place(x=10,y=10,width=700, height=120)

        #department
        dep_label=Label(current_c, text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0, padx=5, pady=10)

        dep_combo=ttk.Combobox(current_c, textvariable=self.var_dep, font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department", "Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=10)

        #course
        course_label=Label(current_c, text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2, padx=5, pady=10)

        course_combo=ttk.Combobox(current_c,textvariable=self.var_course, font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","B.Tech.","M.Tech.","Phd","MS")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        #year
        year_label=Label(current_c, text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0, padx=5, pady=10)

        year_combo=ttk.Combobox(current_c,textvariable=self.var_year, font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year", "2019-20","2020-21","2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=10, sticky=W)
        
        #Semester
        semester_label=Label(current_c, text="Semester",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2, padx=5, pady=10, sticky=W)

        semester_combo=ttk.Combobox(current_c,textvariable=self.var_semester, font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester", "Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=5, pady=10, sticky=W)



        #Current student Information Frame
        current_s = LabelFrame(left_frame,bd=2,bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman",12,"bold"))
        current_s.place(x=10,y=140,width=700, height=400)
        #student id
        student_id=Label(current_s, text="Student Id",font=("times new roman",12,"bold"))
        student_id.grid(row=0,column=0, padx=5, pady=10, sticky=W)
        
        student_id_entry=ttk.Entry(current_s,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        student_id_entry.grid(row=0, column=1, pady=10, sticky=W )

        #student name
        student_name=Label(current_s, text="Student Name",font=("times new roman",12,"bold"))
        student_name.grid(row=0,column=2, padx=5, pady=10, sticky=W)
        
        student_name_entry=ttk.Entry(current_s,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0, column=3, pady=10, sticky=W )

        #class_div_label
        class_div_label=Label(current_s, text="Class Division",font=("times new roman",12,"bold"))
        class_div_label.grid(row=1,column=0, padx=5, pady=10, sticky=W)
        
        # class_div_label_entry=ttk.Entry(current_s,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # class_div_label_entry.grid(row=1, column=1, pady=10, sticky=W )

        class_div_combo=ttk.Combobox(current_s,textvariable=self.var_div, font=("times new roman",12,"bold"),state="readonly")
        class_div_combo["values"]=("Select Division","A","B")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1,  pady=10, sticky=W)


        #roll_no
        roll_no=Label(current_s, text="Roll no",font=("times new roman",12,"bold"))
        roll_no.grid(row=1,column=2, padx=10, pady=5, sticky=W)
        
        roll_no_entry=ttk.Entry(current_s,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W )

        #gender_label
        gender_label=Label(current_s, text="Gender",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0, padx=5, pady=5, sticky=W)
        
        # gender_label_entry=ttk.Entry(current_s,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # gender_label_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W )
        gender_combo=ttk.Combobox(current_s,textvariable=self.var_gender, font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)


        #Dob
        dob_label=Label(current_s, text="DOB",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column=2, padx=5, pady=5, sticky=W)
        
        dob_label_entry=ttk.Entry(current_s,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_label_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W )

        #Email
        Email=Label(current_s, text="Email",font=("times new roman",12,"bold"))
        Email.grid(row=3,column=0, padx=5, pady=5, sticky=W)
        
        Email_entry=ttk.Entry(current_s,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W )

        #phone_no
        phone_no=Label(current_s, text="Phone no.",font=("times new roman",12,"bold"))
        phone_no.grid(row=3,column=2, padx=5, pady=5, sticky=W)
        
        phone_no_entry=ttk.Entry(current_s,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W )
        
        #Address
        address=Label(current_s, text="Address",font=("times new roman",12,"bold"))
        address.grid(row=4,column=0, padx=10, pady=5, sticky=W)
        
        address_entry=ttk.Entry(current_s,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W )
        
        #teacher_name
        teacher_name=Label(current_s, text="Teacher Name",font=("times new roman",12,"bold"))
        teacher_name.grid(row=4,column=2, padx=5, pady=5, sticky=W)
        
        teacher_name_entry=ttk.Entry(current_s,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_name_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W )

        #radio button
        radiobtn1=ttk.Radiobutton(current_s,variable=self.var_radio1, text="Take Photo Sample", value="yes")
        radiobtn1.grid(row=5, column=0, padx=5, pady=10)

        radiobtn2=ttk.Radiobutton(current_s,variable=self.var_radio1, text="No Photo Sample", value="no")
        radiobtn2.grid(row=5, column=1, padx=5, pady=10)

        #Button frames
        #1
        btn_frame=Frame(current_s, bd=2, relief=RIDGE)
        btn_frame.place(x=5,y=250, width=685, height=50)

        save_btn = Button(btn_frame,command=self.add_data,text="Save",width=15, font=("time new roman",13,"bold"),bg="white")
        save_btn.grid(row=0,column=0,pady=7,padx=2)
        delete_btn = Button(btn_frame,command=self.delete_data,text="Delete",width=16, font=("time new roman",13,"bold"),bg="white")
        delete_btn.grid(row=0,column=1, pady=7,padx=2)
        update_btn = Button(btn_frame,command=self.update_data,text="Update",width=16, font=("time new roman",13,"bold"),bg="white")
        update_btn.grid(row=0,column=2,pady=7,padx=2)
        reset_btn = Button(btn_frame,command=self.reset_data,text="Reset",width=15, font=("time new roman",13,"bold"),bg="white")
        reset_btn.grid(row=0,column=3,pady=7,padx=2)
        #2
        btn_frame1=Frame(current_s, bd=2, relief=RIDGE)
        btn_frame1.place(x=5,y=310, width=685, height=50)
        take_sample_btn = Button(btn_frame1,command=self.generate_dataset,text="Take a photo sample",width=32, font=("time new roman",13,"bold"),bg="white")
        take_sample_btn.grid(row=0,column=0,pady=7,padx=2)
        update_photo_btn = Button(btn_frame1,text="Update photo sample",width=33, font=("time new roman",13,"bold"),bg="white")
        update_photo_btn.grid(row=0,column=1,pady=7,padx=2)



        #right label frame
        right_frame = LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        right_frame.place(x=760,y=10,width=720, height=580)

        # #search System
        # search_frame = LabelFrame(right_frame,bd=2,bg="white", relief=RIDGE, text="Search System", font=("times new roman",12,"bold"))
        # search_frame.place(x=10,y=20,width=720, height=100)

        # Search_label=Label(search_frame, text="Search by:",font=("times new roman",12,"bold"))
        # Search_label.grid(row=0,column=0, padx=10, pady=5, sticky=W)

        # search_combo=ttk.Combobox(search_frame,width=15, font=("times new roman",12,"bold"),state="readonly")
        # search_combo["values"]=("Select", "Roll_no","Phone_no")
        # search_combo.current(0)
        # search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # search_entry=ttk.Entry(search_frame,width=17,font=("times new roman",12,"bold"))
        # search_entry.grid(row=0,column=2, padx=10, pady=5, sticky=W)

        # search_btn = Button(search_frame,text="Search",width=13, font=("time new roman",13,"bold"),bg="white")
        # search_btn.grid(row=0,column=3,pady=10,padx=2)
        # showall_btn = Button(search_frame,text="Show All",width=13, font=("time new roman",13,"bold"),bg="white")
        # showall_btn.grid(row=0,column=4, pady=10,padx=2)

        #label Frame
        table_frame = Frame(right_frame,bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=10,y=20,width=700, height=500)

        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("dep","year","sem","id","course","roll","name","div","phone","address","teacher","photo","email", "gender","dob"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        
        self.student_table["show"]="headings"

        
        self.student_table.column("dep",width=120,)
        self.student_table.column("course",width=120)
        self.student_table.column("year",width=120)
        self.student_table.column("sem",width=120)
        self.student_table.column("id",width=120)
        self.student_table.column("name",width=120)
        self.student_table.column("roll",width=120)
        self.student_table.column("gender",width=120)
        self.student_table.column("div",width=120)
        self.student_table.column("dob",width=120)
        self.student_table.column("email",width=120)
        self.student_table.column("phone",width=120)
        self.student_table.column("address",width=120)
        self.student_table.column("teacher",width=120)
        self.student_table.column("photo",width=120)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    def goback(self):
        self.root.destroy()


    #function declaration

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
                my_cursor= conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                
                                                                                                                
             
                                                                                                                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student details added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)


    #fetch data from sql
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
        my_cursor= conn.cursor()

        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #get cursor
    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_year.set(data[1])
        self.var_semester.set(data[2])
        self.var_std_id.set(data[3])
        self.var_course.set(data[4])
        self.var_roll.set(data[5])
        self.var_std_name.set(data[6])
        self.var_div.set(data[7])
        self.var_phone.set(data[8])
        self.var_address.set(data[9])
        self.var_teacher.set(data[10])
        self.var_radio1.set(data[11])
        self.var_email.set(data[12])
        self.var_gender.set(data[13])
        self.var_dob.set(data[14])


    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you wnat to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
                    my_cursor= conn.cursor()
                    my_cursor.execute("update student set Dep=%s, Year=%s, semester=%s, course=%s, Roll=%s,name=%s, Division=%s, phone=%s, Address=%s, teacher=%s,photosample=%s, email=%s,gender=%s,dob=%s where Student_id=%s",(
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_std_id.get(),
                                                                                                                                                                                                             ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details suceesfully Updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}", parent= self.root)
        
    
    #delete details
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete= messagebox.askyesno("Delete","Do you want to permanently delete the student detail",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
                    my_cursor= conn.cursor()
                    sql_query = "delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql_query,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Delete","Student record successfully deleted",parent=self.root)

            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)          
    

    #Reset
    def reset_data(self):

        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_course.set("Select Course")
        self.var_roll.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        self.var_email.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")


    #Take photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
                my_cursor= conn.cursor()
                my_cursor.execute("select * from student")
                result = my_cursor.fetchall()
                
                id=self.var_std_id.get()
                # print(id)
                # # for x in result:
                # #     id+=1
                # #     print(id)
                   
                my_cursor.execute("update student set Dep=%s, Year=%s, semester=%s, course=%s, Roll=%s,name=%s, Division=%s, phone=%s, Address=%s, teacher=%s,photosample=%s, email=%s,gender=%s,dob=%s where Student_id=%s",(
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_std_id.get()

                                                                                                                                                                                                             ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined data from face frontal from open cv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def cropface(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    # Minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                capture= cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=capture.read()
                    if cropface(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(cropface(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="FaceData/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Data set generated successfully",parent=self.root)
            

            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)



if __name__ == "__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()