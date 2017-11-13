from tkinter import *
from tkinter.filedialog import *


class Paint(Frame):
    def __init__(self, parent,kn):
        Frame.__init__(self, parent)
        self.network = kn
        self.parent = parent
        self.setUI()
        self.brush_size = 18
        self.color = "black"
        self.pixelMatrix = [[0] * 28 for i in range(28)]


    def setUI(self):
        self.parent.title("The best Neuron Net from me!")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6,weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5,
                       sticky=E + W + S + N)

        color_lab = Label(self, text="Очистить экран: ")
        color_lab.grid(row=0, column=0, padx=6)
        red_btn = Button(self, text="очистить",width=20, command=lambda: self.clear(), bg="red",fg="black")
        red_btn.grid(row=0, column=2, sticky=W)

        check_label = Label(self, text="Проверь нейронку: ")  # Создаем метку для кнопок изменения размера кисти
        check_label.grid(row=1, column=0, padx=5 )
        check_btn = Button(self, text="Check", width=20, command = lambda : self.listener(), bg="green",fg="black")
        check_btn.grid(row=1, column=2)


        self.canv.bind("<B1-Motion>", self.draw)
        # print (self.canv)

    def draw(self, event=0):
        self.pixelMatrix[round(event.y/18)][round(event.x/18)] = 1

        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)
    def clear (self):
        self.canv.delete("all")
        self.pixelMatrix = [[0] * 28 for i in range(28)]



    def listener (self):
        for i in self.pixelMatrix:
            print (i,"\n")
        # print(self.pixelMatrix)
        # print (self.canv.find_all())
        # print (self.canv.coords(1))
        print("Press button")

