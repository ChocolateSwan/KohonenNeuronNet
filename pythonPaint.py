from tkinter import *
from tkinter.filedialog import *
import io
from PIL import Image


class Paint(Frame):
    def __init__(self, parent,kn):
        Frame.__init__(self, parent)
        self.network = kn
        self.parent = parent
        self.digit_label = None
        self.color = "black"
        self.setUI()
        self.brush_size = 18
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

        self.digit_label = Label(self, text= "?" , font=("Helvetica", 28), fg="blue")
        self.digit_label.grid(row=0, column=4, columnspan=8,rowspan = 2 )


        self.canv.bind("<B1-Motion>", self.draw)

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)
    def clear (self):
        self.canv.delete("all")
        self.digit_label['text'] = "?"
        self.pixelMatrix = [[0] * 28 for i in range(28)]



    def listener (self):
        size = 28,28
        ps = self.canv.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        img = img.resize(size, Image.ANTIALIAS)
        result_image = list(img.getdata())

        result_image = list(map(lambda x: abs((255 - x[0])/255), result_image))
        img.save('./digit_image.jpg')

        list_t = []
        for i in self.pixelMatrix:
            list_t.extend(i)
        qq = self.network.Handle(result_image)
        self.digit_label['text'] = str(qq)

