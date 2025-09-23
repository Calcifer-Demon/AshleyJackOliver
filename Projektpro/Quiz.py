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
    add_fönster.title("Lägg till nya frågor")
    add_fönster.geometry("500x500")

    svar = []
    labels_text= ["Fråga:", "Alternativ 1:", "Alternativ 2:", "Alternativ 3:", "Alternativ 4:", "Rätt svar:"]
    for text in labels_text:
        tk.Label(add_fönster, text=text).pack(pady=10)
        entry = tk.Entry(add_fönster, width=100)
        entry.pack()
        svar.append(entry)

def starta_quiz():
        


    if __name__ == "__main__":
        if not os.path.exists("quiz_frågor.txt"):
            with open("quiz_frågor.txt", "w", encoding="utf-8"):
                pass

    huvud_fönster = tk.Tk()
    huvud_fönster.title("huvudmeny")
    huvud_fönster.geometry("500x500")

    tk.Button(huvud_fönster, text="Starta Quiz", command=starta_quiz).pack(pady=10)
    tk.Button(huvud_fönster, text="Lägg till frågor", command=frågor_add).pack(pady=10)
    huvud_fönster.mainloop()