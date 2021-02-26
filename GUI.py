from tkinter import *
windowWidth = 800
windowHeight = 600

window = Tk()

# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()

window.title('Hello Python')
window.geometry(str(windowWidth)+"x"+str(windowHeight))

lbl = Label(window, text="This is Label widget",
            fg='red', font=("Helvetica", 16))
lbl.place(x=200, y=50)

window.mainloop()


def emptyBoard():
    for i in range(8):
        for j in range(8):
            print("test")
