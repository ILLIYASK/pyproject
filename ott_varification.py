from tkinter import *
from twilio.rest import Client
import random

class OtpVarifier(Tk):
    def  __init__(self):
        super().__init__()
        self.geometry('1000x580+200+80')
        self.config(bg="white")
        self.resizable(0,0)
if __name__== "__main__" :
    window=OtpVarifier()
    window.mainloop()
