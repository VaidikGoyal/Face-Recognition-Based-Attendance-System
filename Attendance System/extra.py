go_back=Image.open(r"C:\Users\yashj\OneDrive\Pictures\Saved Pictures\01.png")
go_back=go_back.resize((1900,1080),Image.ANTIALIAS)
self.photoback = ImageTk.PhotoImage(go_back)

back_sample_btn = Button(title_label1,command=self.goback,image=self.photoback,width=32, font=("time new roman",13,"bold"),bg="white")
back_sample_btn.place(x=0,y=0, width=30,height=30)

def goback(self):
    self.root.destroy()





