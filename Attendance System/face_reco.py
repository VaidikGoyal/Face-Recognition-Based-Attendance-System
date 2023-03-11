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



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x1080+0+0")
        self.root.title("Face Recognition System")

        title_label1 = Label(self.root, text="Face Recognition",font=("times new roman",30,"bold"),bg="darkseagreen",fg="white")
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

        img=Image.open(r"C:\Users\yashj\Desktop\minor\face.png")
        img=img.resize((500,500),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_label = Label(f_label3, image=self.photoimg)
        f_label.place(x=568,y=100,width=400, height=400)


        detect_btn = Button(f_label3,command=self.face_recog,cursor="hand2",text="Face Recognition",width=100, font=("time new roman",25,"bold"),bg="azure")
        detect_btn.place(x=618,y=550,width=300,height=50)


    ############Attendance###############
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
                # print(name_list)
                
            if((i not in name_list)):
                p="Present"
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},{p}")

                conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
                my_cursor= conn.cursor()
                my_cursor.execute("insert into attendance values(%s,%s,%s,%s,%s,%s,%s)",(i,n,r,d,d1,dtString,p ))
                conn.commit()
                conn.close()

 



        #face recognition

    def face_recog(self):

        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost", username="root", password="yashjain", database="facerecognizer")
                my_cursor= conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                

                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord 

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
            
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("faceclassifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Recognition your face",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

    def goback(self):
        self.root.destroy()




if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition(root)
    root.mainloop()