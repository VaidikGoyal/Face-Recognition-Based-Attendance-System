from tkinter import *
from tkinter import ttk
import types
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x1080+0+0")
        self.root.title("Attendance Management System")

        #############variable#####################
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()
        
        title_label1 = Label(self.root, text="Attendance Management System",font=("times new roman",30,"bold"),bg="darkseagreen",fg="white")
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
        main_frame.place(x=68,y=50,width=1405, height=630)

        #left label frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=680, height=600)

        left_inside_frame = LabelFrame(left_frame,bd=2,bg="white", relief=RIDGE, font=("times new roman",12,"bold"))
        left_inside_frame.place(x=15,y=125,width=650, height=200)


        attendance_id=Label(left_inside_frame, text="Attendance Id",font=("times new roman",12,"bold"))
        attendance_id.grid(row=0,column=0, padx=5, pady=10, sticky=W)
        
        attendance_id_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_id,width=20,font=("times new roman",12,"bold"))
        attendance_id_entry.grid(row=0, column=1, pady=10, sticky=W )

        #student name
        student_name=Label(left_inside_frame, text="Student Name",font=("times new roman",12,"bold"))
        student_name.grid(row=0,column=2, padx=5, pady=10, sticky=W)
        
        student_name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0, column=3, pady=10, sticky=W )

        #Roll_no
        Roll_no=Label(left_inside_frame, text="Roll_no",font=("times new roman",12,"bold"))
        Roll_no.grid(row=1,column=0, padx=5, pady=10, sticky=W)
        
        Roll_no_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_roll,width=20,font=("times new roman",12,"bold"))
        Roll_no_entry.grid(row=1, column=1, pady=10, sticky=W )

        #department
        department=Label(left_inside_frame, text="Department",font=("times new roman",12,"bold"))
        department.grid(row=1,column=2, padx=5, pady=10, sticky=W)
        
        department_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_dep,width=20,font=("times new roman",12,"bold"))
        department_entry.grid(row=1, column=3, pady=10, sticky=W )

        #time
        time=Label(left_inside_frame, text="Time",font=("times new roman",12,"bold"))
        time.grid(row=2,column=0, padx=5, pady=10, sticky=W)
        
        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_time,width=20,font=("times new roman",12,"bold"))
        time_entry.grid(row=2, column=1, pady=10, sticky=W )

        #date
        date=Label(left_inside_frame, text="Date",font=("times new roman",12,"bold"))
        date.grid(row=2,column=2, padx=5, pady=10, sticky=W)
        
        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_date,width=20,font=("times new roman",12,"bold"))
        date_entry.grid(row=2, column=3, pady=10, sticky=W )

        #status
        status_label=Label(left_inside_frame, text="Attendance Status",font=("times new roman",12,"bold"))
        status_label.grid(row=3,column=0, padx=5, pady=10, sticky=W)

        status_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance, font=("times new roman",12,"bold"),state="readonly")
        status_combo["values"]=("Status", "Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=3, column=1, padx=5, pady=10, sticky=W)

        #Button frames
        #1
        btn_frame=Frame(left_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=15,y=400,width=650, height=60)

        import_btn = Button(btn_frame,command=self.importcsv,text="Import csv",width=14, font=("time new roman",13,"bold"),bg="white")
        import_btn.grid(row=0,column=0,pady=10,padx=4)
        export_btn = Button(btn_frame,command=self.exportcsv,text="Export csv",width=15, font=("time new roman",13,"bold"),bg="white")
        export_btn.grid(row=0,column=1, pady=10,padx=2)
        update_btn = Button(btn_frame,command=self.update_data,text="Update",width=15, font=("time new roman",13,"bold"),bg="white")
        update_btn.grid(row=0,column=2,pady=10,padx=2)
        reset_btn = Button(btn_frame,command=self.reset_data,text="Reset",width=14, font=("time new roman",13,"bold"),bg="white")
        reset_btn.grid(row=0,column=3,pady=10,padx=2)


        right_frame = LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman",12,"bold"))
        right_frame.place(x=710,y=10,width=680, height=600)
        table_frame = LabelFrame(right_frame,bd=2,bg="white", relief=RIDGE, font=("times new roman",12,"bold"))
        table_frame.place(x=10,y=10,width=660, height=560)

        #############scroll bar################
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        self.fetchdb()
    ###################face data#######################

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def fetchdb(self):
        global mydata

        conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
        my_cursor= conn.cursor()

        my_cursor.execute("select * from attendance")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in data:
                self.AttendanceReportTable.insert("",END,values=i)
                mydata.append(i)
            conn.commit()
        conn.close()

    
    #import csv
    def importcsv(self):
        global mydata
        mydata.clear()

        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fin) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fin, mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fin)+" successfully")
         
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")

    def update_data(self):
        if self.var_attend_attendance=="Status" or self.var_attend_id.get()=="" or self.var_attend_dep.get()=="" or self.var_attend_date.get()=="" or self.var_attend_time.get()=="" or self.var_attend_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you wnat to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
                    my_cursor= conn.cursor()
                    my_cursor.execute("update attendance set name=%s,roll=%s,dep=%s,attendance=%s,time=%s,date=%s where Student_id=%s",(
                                                                                                                                        self.var_attend_name.get(),
                                                                                                                                        self.var_attend_roll.get(),
                                                                                                                                        self.var_attend_dep.get(),
                                                                                                                                        self.var_attend_attendance.get(),
                                                                                                                                        self.var_attend_time.get(),
                                                                                                                                        self.var_attend_date.get(),
                                                                                                                                        self.var_attend_id.get()
                                                                                                                                                                                                                
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Attendance suceesfully Updated", parent=self.root)
                conn.commit()
                self.fetchdb()
                conn.close()

            except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}", parent= self.root)

    def goback(self):
        self.root.destroy()
    




if __name__ == "__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()