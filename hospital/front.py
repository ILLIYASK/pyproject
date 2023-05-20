from tkinter import *
from PIL import Image,ImageTk


class Front(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x650+40+20")
        self.config(bg='blue',borderwidth=1)
        self.title("front")

    def MainLabels(self):

        self.hospital_img= Image.open("C:\\Users\\ADMIN\\Desktop\\pyproject\\hospital\\resources\\main.webp")
        self.hospital_img= ImageTk.PhotoImage(self.hospital_img)
        self.main_label= Label(self,image=self.hospital_img)
        self.name= Label(
            self.main_label,text="Hospital Management System", bg="#d7f5f7",
            fg="#eb0918",font=("Helvetica", "46"),
            highlightthickness=4,highlightbackground="#065e53",
        )

        self.main_label.place(x=0,y=0)
        self.name.place(x=250,y=80)

    def LoginFrame(self):

        def shwpsd(var,entry):
            if self.var.get()==0:
                self.password_entry.config(show='')
            else:
                self.password_entry.config(show='*')



        self.login_frame=Frame(self.main_label,bg="white",highlightbackground="#085099",
                               highlightthickness=3,width=400,height=300,)
        self.login_frame.place(x=340,y=240)


        self.username_label=Label(self.login_frame,text="Enter username :",
                                  font=("Comic Sans MS", 15, "bold"),width=15,)

        self.username_entry=Entry(self.login_frame,font=("Comic Sans MS", 14,),
                                  width=20)

        self.password_label=Label(self.login_frame,text="Enter password :",
                                  font=("Comic Sans MS", 15, "bold"),width=15,)

        self.password_entry=Entry(self.login_frame,font=("Comic Sans MS", 14, ),width=20)

        self.var=IntVar(value=0)
        self.password_checkbutton=Checkbutton(self.login_frame,offvalue=0, onvalue=1,
                                              variable=self.var,command=lambda :shwpsd(self.var,self.password_entry))

        self.login_button=Button(self.login_frame,text="Log-in",font=("Comic Sans MS",15, "bold"),
                                 width=8,bg="blue",fg="white",activeforeground="blue",
                                 activebackground="white")

        self.forget_password_button=Button(self.login_frame,text="Forgot Password",fg="red")

        self.create_user_button=Button(self.login_frame,text="create an account",fg="blue")


        self.username_label.grid(row=0,column=0,pady=10,padx=20)
        self.username_entry.grid(row=0,column=1,padx=5)
        self.password_label.grid(row=1,column=0,pady=10)
        self.password_entry.grid(row=1,column=1)
        self.password_checkbutton.grid(row=1,column=2,sticky="nw",pady=10,padx=10)
        self.login_button.grid(row=3,column=1,pady=10)
        self.forget_password_button.grid(row=2,column=2,sticky="ne",padx=20)
        self.create_user_button.grid(row=3,column=2)



window=Front()
window.MainLabels()
window.LoginFrame()
window.mainloop()
