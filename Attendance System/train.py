from tkinter import *
from tkinter import ttk
import types
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x1080+0+0")
        self.root.title("Train Data")

        title_label1 = Label(self.root, text="Train Data Set",font=("times new roman",30,"bold"),bg="darkseagreen",fg="white")
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

        train_btn = Button(f_label3,command=self.train_data_classifier,cursor="hand2",text="Train Data",width=100, font=("time new roman",25,"bold"),bg="azure")
        train_btn.place(x=618,y=385,width=300,height=50)
        
    def train_data_classifier(self):
        data_dir=("FaceData")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        # print(path)
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray Scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            # print(id)
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        ############train the classifier############
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("faceclassifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!",parent=self.root)
        
    def goback(self):
        self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()