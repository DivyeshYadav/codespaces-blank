from tkinter import*
from PIL import ImageTk, Image
window = Tk()
window.geometry("400x400")
window.title("Image ")
image = Image.open("Codingal\Giraffe.jpg")
picture = ImageTk.PhotoImage(image)
label = Label(window, image=picture)
label.place(x=30,y = 0)
window.mainloop()
