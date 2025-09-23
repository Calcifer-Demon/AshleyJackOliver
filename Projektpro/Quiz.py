import tkinter as tk
from tkinter import messagebox
import os

class frågor:
    def __init__(self,text, alternativ, rätt):
        self.text=text
        self.alternativ=alternativ
        self.rätt=rätt




    
def frågor_add():
    add_fönster = tk.Toplevel()



def starta_quiz():
        


if __name__ == "__main__":
    if not os.path.exists("quiz_frågor.txt"):
        with open("quiz_frågor.txt", "w", encoding="utf-8"):
            pass

    huvud_fönster = tk.Tk()
    huvud_fönster.title("huvudmeny")
    huvud_fönster.geometry("250x150")

    tk.Button(huvud_fönster, text="Starta Quiz", command=starta_quiz)
    tk.Button(huvud_fönster, text="Lägg till frågor", command=frågor_add)