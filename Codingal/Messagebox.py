from tkinter import*
from tkinter import messagebox
window = Tk()
window.geometry("200x200")
window.title("Message Box")
def message():
    messagebox.showinfo("Alert","Virus Detected!")
btn = Button(window, text = "Scan for Virus", command=message)
btn.pack()
window.mainloop()