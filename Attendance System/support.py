from tkinter import *
from tkinter import ttk
import types
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Support:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x1080+0+0")
        self.root.title("Student Detail")

        
        title_label1 = Label(self.root, text="Support",font=("times new roman",30,"bold"),bg="darkseagreen",fg="white")
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

        current_c = LabelFrame(f_label3,bd=2,bg="white", relief=RIDGE, font=("times new roman",12,"bold"))
        current_c.place(x=508,y=250,width=520, height=330)

        ##############yash
        current = LabelFrame(current_c,bd=2,bg="white", relief=RIDGE,  font=("times new roman",12,"bold"))
        current.place(x=10,y=10,width=500, height=150)
        
        img=Image.open(r"C:\Users\yashj\Desktop\minor\yash.jpg")
        img=img.resize((140,140),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_label = Label(current, image=self.photoimg)
        f_label.place(x=5,y=5,width=140, height=140)

        current_name = LabelFrame(current,bd=2,bg="white", relief=RIDGE,  font=("times new roman",12,"bold"))
        current_name.place(x=160,y=10,width=330, height=130)

        yash_label=Label(current_name, text="Yash Jain",font=("times new roman",12,"bold"))
        yash_label.place(x=10,y=10,width=310, height=55)
        yash_email_label=Label(current_name, text="yashjainyj1304200@gmail.com",font=("times new roman",12,"bold"))
        yash_email_label.place(x=10,y=65,width=310, height=55)
        


        ##########vaidik
        current1 = LabelFrame(current_c,bd=2,bg="white", relief=RIDGE,  font=("times new roman",12,"bold"))
        current1.place(x=10,y=170,width=500, height=150)

        img1=Image.open(r"C:\Users\yashj\Desktop\minor\vaidik.jpg")
        img1=img1.resize((140,140),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_label1 = Label(current1, image=self.photoimg1)
        f_label1.place(x=5,y=5,width=140, height=140)

        current_name1 = LabelFrame(current1,bd=2,bg="white", relief=RIDGE,  font=("times new roman",12,"bold"))
        current_name1.place(x=160,y=10,width=330, height=130)

        vaidik_label=Label(current_name1, text="Vaidik Goyal",font=("times new roman",12,"bold"))
        vaidik_label.place(x=10,y=10,width=310, height=55)
        vaidik_email_label=Label(current_name1, text="vaidik@gmail.com",font=("times new roman",12,"bold"))
        vaidik_email_label.place(x=10,y=65,width=310, height=55)

    def goback(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj = Support(root)
    root.mainloop()