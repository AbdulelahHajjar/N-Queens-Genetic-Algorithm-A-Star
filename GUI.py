from tkinter import *
from PIL import ImageTk, Image

windowWidth = 800
windowHeight = 600
sideBarWidth = 200
numQueens = 8

queenIconSize = int((windowWidth - sideBarWidth) / numQueens)


def drawBoard():
    canvas = Canvas(window, width=600, height=600)
    canvas.pack()
    for i in range(numQueens):
        for j in range(numQueens):
            image = Image.open('example.png')
            image = image.resize(
                (queenIconSize, queenIconSize), Image.ANTIALIAS)
            my_img = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, image=my_img, anchor="nw")

            a = canvas.create_rectangle(50, 0, 50, 0, fill='red')
    canvas.move(a, sideBarWidth, 0)


window = Tk()

window.title('Hello Python')
window.geometry(str(windowWidth)+"x"+str(windowHeight))

window.mainloop()
