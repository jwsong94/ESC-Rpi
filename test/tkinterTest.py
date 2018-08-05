from tkinter import *

window = Tk()
window.title("Welcome to Tkinter")

canvas = Canvas(window, width=300, height=300)
canvas.pack()

img = PhotoImage(file="star.jpg")
canvas.create_image(20,20, anchor=NW, image=img)

window.mainloop()
