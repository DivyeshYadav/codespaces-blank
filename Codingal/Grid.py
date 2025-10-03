from tkinter import *
window = Tk()
window.title("Grid")
for i in range(3):
    for j in range(3):
        frame = Frame(
            master=window,
            relief=RAISED,
            borderwidth=10
        )
        frame.grid(row=i, column=j,padx=5,pady=5)
        label = Label(master = frame ,text = f"Row{i} column{j}")
        label.pack()
window.mainloop()