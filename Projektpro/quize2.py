import tkinter as tk
from tkinter import messagebox
import os

class frågor:
    """A class to represent a quiz question."""
    def __init__(self, text, alternativ, rätt):
        self.text = text
        self.alternativ = alternativ
        self.rätt = rätt

def spara_frågor(svar, fönster):
    """Saves the question to the file."""
    frågor_text = svar[0].get()
    val = [e.get() for e in svar[1:5]]
    rätt__text = svar[5].get()

    if not all([frågor_text] + val + [rätt__text]):
        messagebox.showwarning("Varning!", "Fyll i alla fält")
        return
    
    if rätt__text not in val:
        messagebox.showwarning("Varning!", "Ett av alternativen måste väljas som rätt svar")
        return
    
    with open("quiz_frågor.txt", "a", encoding="utf-8") as fil:
        fil.write(f"{frågor_text}\n")
        for i, option in enumerate(val):
            fil.write(f"val {i}: {option}\n")
        fil.write(f"rätt svar: {rätt__text}\n")

    messagebox.showinfo("Sparat!", "Frågan har sparats.")
    fönster.destroy()

def frågor_add():
    """Creates a new window to add questions."""
    add_fönster = tk.Toplevel()
    add_fönster.title("Lägg till nya frågor")
    add_fönster.geometry("500x500")

    svar = []
    labels_text = ["Fråga:", "Alternativ 1:", "Alternativ 2:", "Alternativ 3:", "Alternativ 4:", "Rätt svar:"]
    for text in labels_text:
        tk.Label(add_fönster, text=text).pack(pady=10)
        entry = tk.Entry(add_fönster, width=100)
        entry.pack()
        svar.append(entry)
    tk.Button(add_fönster, text="spara frågan", command=lambda: spara_frågor(svar, add_fönster)).pack(pady=10)

if __name__ == "__main__":
    # Corrected indentation for the main application block
    if not os.path.exists("quiz_frågor.txt"):
        with open("quiz_frågor.txt", "w", encoding="utf-8"):
            pass
    huvud_fönster = tk.Tk()
    huvud_fönster.title("huvudmeny")
    huvud_fönster.geometry("500x500")
    tk.Button(huvud_fönster, text="Starta Quiz").pack(pady=10)
    tk.Button(huvud_fönster, text="Lägg till frågor", command=frågor_add).pack(pady=10)
    huvud_fönster.mainloop()