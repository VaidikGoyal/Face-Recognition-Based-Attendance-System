from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_reco import Face_Recognition
from Attendance import Attendance 
from support import Support
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x1080+0+0")
        self.root.title("Face Recognition Attendance System (Admin)")

        # Mits Logo
        img=Image.open(r"C:\Users\yashj\Desktop\minor\logo.jpg")
        img=img.resize((150,150),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_label = Label(self.root, image=self.photoimg)
        f_label.place(x=0,y=0,width=150, height=150)

        # #Topic
        # img1=Image.open(r"C:\Users\yashj\OneDrive\Pictures\Saved Pictures\345330.jpg")
        # img1=img1.resize((1500,150),Image.ANTIALIAS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)

        # f_label1 = Label(self.root, image=self.photoimg1)
        # f_label1.place(x=150,y=0,width=1500, height=150)

        # #Submitted by
        # img2=Image.open(r"C:\Users\yashj\OneDrive\Pictures\Saved Pictures\345330.jpg")
        # img2=img2.resize((200,200),Image.ANTIALIAS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)

        f_label2 = Label(self.root, text="Madhav Institute of Technology & Science, Gwalior(M.P.)",font=("times new roman",35,"bold"),fg="darkblue",bg="azure")
        f_label2.place(x=150,y=0,width=1386, height=75)

        f_label1 = Label(self.root, text="Batch:- 2019-23",font=("times new roman",25,"bold"),fg="darkcyan",bg="azure")
        f_label1.place(x=150,y=75,width=1380, height=75)
        

        #background Image
        img3=Image.open(r"C:\Users\yashj\OneDrive\Pictures\Saved Pictures\01.png")
        img3=img3.resize((1900,1080),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_label3 = Label(self.root, image=self.photoimg3)
        f_label3.place(x=0,y=150,width=1536, height=700)


        #Topic Name
        title_label1 = Label(f_label3, text="Face Recognition Attendance System",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_label1.place(x=0,y=0,width=1536,height=45)

    ############################time##################

        def time():
            string = strftime('%H:%M:%S %p')
            lb1.config(text = string)
            lb1.after(1000,time)

        lb1 = Label(title_label1, font=('time new roman',14,'bold'),background='white', foreground="blue")
        lb1.place(x=0,y=0,width=150,height=45)
        time()

        #student button
        img4=Image.open(r"C:\Users\yashj\Desktop\minor\student.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(f_label3, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=320, y=100, width=200 , height=200)
        b1_1 = Button(f_label3, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman",18,"bold"),bg="white",fg="red")
        b1_1.place(x=320, y=300, width=200 , height=40)

        #Attendance
        img5=Image.open(r"C:\Users\yashj\Desktop\minor\Attendance.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(f_label3,command=self.attend, image=self.photoimg5, cursor="hand2")
        b2.place(x=667, y=100, width=200 , height=200)
        b2_2 = Button(f_label3,command=self.attend, text="Attendance", cursor="hand2", font=("times new roman",18,"bold"),bg="white",fg="red")
        b2_2.place(x=667, y=300, width=200 , height=40)

        #Face Finder
        img6=Image.open(r"C:\Users\yashj\Desktop\minor\FaceDetection.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(f_label3, image=self.photoimg6,command=self.face_reco, cursor="hand2")
        b3.place(x=1014, y=100, width=200 , height=200)
        b3_3 = Button(f_label3, text="Face Detector",command=self.face_reco, cursor="hand2", font=("times new roman",18,"bold"),bg="white",fg="red")
        b3_3.place(x=1014, y=300, width=200 , height=40)

        #Traindata
        img7=Image.open(r"C:\Users\yashj\Desktop\minor\train.png")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(f_label3, image=self.photoimg7,command=self.train_data, cursor="hand2")
        b4.place(x=147, y=350, width=200 , height=200)
        b4_4 = Button(f_label3, text="Train Data",command=self.train_data, cursor="hand2", font=("times new roman",18,"bold"),bg="white",fg="red")
        b4_4.place(x=147, y=550, width=200 , height=40)

        #Support
        img8=Image.open(r"C:\Users\yashj\Desktop\minor\support.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(f_label3,command=self.support, image=self.photoimg8, cursor="hand2")
        b5.place(x=494, y=350, width=200 , height=200)
        b5_5 = Button(f_label3,command=self.support, text="Support", cursor="hand2", font=("times new roman",18,"bold"),bg="white",fg="red")
        b5_5.place(x=494, y=550, width=200 , height=40)

        #Photos
        img9=Image.open(r"C:\Users\yashj\Desktop\minor\photo.png")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(f_label3, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b6.place(x=841, y=350, width=200 , height=200)
        b6_6 = Button(f_label3, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman",18,"bold"),bg="white",fg="red")
        b6_6.place(x=841, y=550, width=200 , height=40)

        #Exit
        img10=Image.open(r"C:\Users\yashj\Desktop\minor\Exit.png")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(f_label3, image=self.photoimg10, cursor="hand2",command=self.iExit)
        b7.place(x=1188, y=350, width=200 , height=200)
        b7_7 = Button(f_label3, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman",18,"bold"),bg="white",fg="red")
        b7_7.place(x=1188, y=550, width=200 , height=40)

    #function of button

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

    #photo button
    def open_img(self):
        os.startfile("FaceData")


    #function of train button

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)

    #function of face reco

    def face_reco(self):
        self.new_window = Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    #function of Attendance

    def attend(self):
        self.new_window = Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
     #function of Support

    def support(self):
        self.new_window = Toplevel(self.root)
        self.app=Support(self.new_window)

     #function of Exit

    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
        


if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

