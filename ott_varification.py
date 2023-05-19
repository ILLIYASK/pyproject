from tkinter import *
from twilio.rest import Client
from tkinter import messagebox
import time

account_sid = "ACfc6ea1c9a9fb8ccb1512129f0817a3bb"
auth_token = "f629238878fc0de07c3af46918456af8"
verify_sid = "VAdead5e0e7181efeaec2f1711f1193de5"
verified_number = "+918606913836"


class OtpVarifier(Tk):
    def  __init__(self):
        super().__init__()
        self.geometry('1000x580+200+80')
        self.config(bg="white")
        self.resizable(0,0)
        self.client=Client(account_sid,auth_token)
        self.time=120


    def send(self):
        self.verification = self.client.verify.v2.services(verify_sid) \
            .verifications \
            .create(to=verified_number, channel="sms")
    def update(self):
        self.time=self.time-1
        print(self.time)
        if self.time>=-1:
            self.timer_label()
        else:
            messagebox.showinfo("showinfo","time out ")
            window.destroy()

    def Labels(self):
        self.c=Canvas(self,bg="light blue",width=400,height=280)
        self.c.place(x=290,y=120)
        self.upper=Frame(self,bg="gray",width=1500,height=130)
        self.upper.place(x=0,y=0)

    def timer_label(self):
        self.time-=1
        if self.time>=0:
            self.timer=Label(self,bg="black",fg="white",width=44,height=3,text=f" 00 : {self.time//60:>02}: {self.time%60:>02}")
            self.timer.place(x=300,y=450)
            self.timer.after(1000,self.timer_label)
        else:
            window.destroy()


    def entry(self):
        self.e=Entry(self,bg="white",width=20)
        self.e.place(x=400,y=200)
    def varify(self):
        verification_check = self.client.verify.v2.services(verify_sid) \
            .verification_checks \
            .create(to=verified_number, code=self.e.get())
        return messagebox.showinfo("showinfo",f"{verification_check.status}")

    def resend(self):
        return self.send()
    def buuton(self):
        self.re=Button(self,text="resend",command=lambda :self.resend())
        self.su=Button(self,text="submit",command=lambda :self.varify())
        self.se=Button(self,text="otp",command=lambda :self.send())
        self.se.place(x=400,y=300)
        self.su.place(x=440,y=300)
        self.re.place(x=480,y=300)

if __name__== "__main__" :
    window=OtpVarifier()
    window.Labels()
    window.entry()
    window.buuton()
    window.timer_label()
    window.mainloop()