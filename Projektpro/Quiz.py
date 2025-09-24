import tkinter as tk
from tkinter import messagebox
import os

class frågor:
    def __init__(self,text, alternativ, rätt):
        self.text=text
        self.alternativ=alternativ
        self.rätt=rätt

def spara_frågor(svar, fönster):
    frågor_text = svar[0].get()
    val = [e.get() for e in svar[1:5]]
    rätt__text = svar[5].get()

    if not all([frågor_text] + val + [rätt__text]):
        messagebox.showwarning("!","Fyll i alla fält")
        return
    
    if rätt__text not in val:
        messagebox.showwarning("!", "ett alternativ måste väljas")
        return
    
    with open("quiz_frågor.txt", "a", encoding="utf-8") as fil:
        fil.write(f"{frågor_text}\n")
        for i, val in enumerate(val):
            fil.write(f"val {i}: {val}\n")
        fil.write(f"rätt svar: {rätt__text}\n")

    messagebox.showinfo("frågan har sparats.")
    fönster.destroy()


    
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
    tk.Button(add_fönster, text="spara frågan", command=lambda:spara_frågor(svar, add_fönster)).pack(pady=10)


        

    if __name__ == "__main__":
        if not os.path.exists("quiz_frågor.txt"):
            with open("quiz_frågor.txt", "w", encoding="utf-8"):
                pass
        huvud_fönster = tk.Tk()
        huvud_fönster.title("huvudmeny")
        huvud_fönster.geometry("500x500")
        tk.Button(huvud_fönster, text="Starta Quiz").pack(pady=10)
        tk.Button(huvud_fönster, text="Lägg till frågor", command=frågor_add).pack(pady=10)
        huvud_fönster.mainloop()