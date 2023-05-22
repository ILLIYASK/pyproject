from tkinter import *
from tkinter import messagebox

from mysql_functions import MysqlFunction

class CreateNewAccount(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("1280x650+40+20")
        self.config(bg="light blue")

    def create_new_account(self):

        def varify(usr_name,password):
            try:
                obj=MysqlFunction()
                obj.create_account(usr_name,password)
            except Exception as e:
                messagebox.showinfo("info",e)



        def shwpsd(var,entry):

            if var.get()==1:
                entry.config(show='')
            else:
                entry.config(show='*')


        self.create_new_account_frame=Frame(self,bg="light blue"
                                            ,width=400,height=300)
        self.create_new_account_frame.place(x=250,y=100)


        self.heading=Label(self.create_new_account_frame,text="Create New Account !!!",
                           font=("Comic Sans MS", 30,),width=20,height=2,bg="light blue",
                           fg="blue")

        self.username_label=Label(self.create_new_account_frame,text="Enter username : ",
                                  width=21,font=("Comic Sans MS", 15,),anchor="nw",bg='light blue')

        self.username_entry=Entry(self.create_new_account_frame,width=20,
                                  font=("Comic Sans MS", 14,))

        self.password_label=Label(self.create_new_account_frame,text="Enter password : ",
                                  font=("Comic Sans MS", 15,),width=21,anchor="nw",bg='light blue')

        self.password_entry=Entry(self.create_new_account_frame,width=20,
                                  font=("Comic Sans MS", 14,),show="*")

        self.conform_password_label=Label(self.create_new_account_frame,text="Conform Password :",
                                          font=("Comic Sans MS", 15,),width=21,anchor="nw",bg='light blue')

        self.conform_password_entry=Entry(self.create_new_account_frame,width=20,
                                          font=("Comic Sans MS", 14,),show='*')

        self.var=IntVar(value=0)
        self.checkbutton=Checkbutton(self.create_new_account_frame,variable=self.var,offvalue=0,
                                     onvalue=1,command=lambda :shwpsd(self.var,self.password_entry),
                                     bg="light blue",width=1)

        self.sumbit_button=Button(self.create_new_account_frame,text="Create",font=("Comic Sans MS", 14,),
                                  command=lambda :varify(self.username_entry.get(),self.password_entry.get()))


        self.heading.grid(row=0, column=0,pady=20)
        self.username_label.grid(row=1, column=0)
        self.username_entry.grid(row=2, column=0)
        self.password_label.grid(row=3, column=0)
        self.password_entry.grid(row=4, column=0)
        self.checkbutton.grid(row=4,column=0,sticky='ne',padx=85)
        self.conform_password_label.grid(row=5,column=0)
        self.conform_password_entry.grid(row=6,column=0)
        self.sumbit_button.grid(row=7,column=0,pady=20)


if __name__ =="__main__":
    window=CreateNewAccount()
    window.create_new_account()
    window.mainloop()
