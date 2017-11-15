import io
from tkinter.filedialog import *
from PIL import Image


class Paint(Frame):

    result_image_size = 28, 28

    def __init__(self, parent, neuron_net):
        Frame.__init__(self, parent)
        self.neuron_net = neuron_net
        self.parent = parent
        self.digit_label = None
        self.canvas = None
        self.color = "black"
        self.brush_size = 10
        self.set_ui()

    def set_ui(self):
        self.parent.title("Нейронная сеть Кохонена")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        self.canvas = Canvas(self, bg="white")
        self.canvas.grid(row=2, column=0, columnspan=7,
                         padx=5, pady=5, sticky=E + W + S + N)

        clear_label = Label(self, text="Очистить холст: ")
        clear_label.grid(row=0, column=0, padx=6)

        clear_btn = Button(self, text="очистка", width=20,
                           command=lambda: self.clear(),
                           bg="red", fg="black")
        clear_btn.grid(row=0, column=2, sticky=W)

        check_label = Label(self, text="Проверь результат: ")
        check_label.grid(row=1, column=0, padx=5)

        check_btn = Button(self, text="проверка", width=20,
                           command=lambda: self.check_digit(),
                           bg="green", fg="black")
        check_btn.grid(row=1, column=2)

        self.digit_label = Label(self, text="?",
                                 font=("Helvetica", 28), fg="blue")
        self.digit_label.grid(row=0, column=4,
                              columnspan=8, rowspan=2)

        self.canvas.bind("<B1-Motion>", self.draw)

    def draw(self, event):
        self.canvas.create_oval(event.x - self.brush_size,
                                event.y - self.brush_size,
                                event.x + self.brush_size,
                                event.y + self.brush_size,
                                fill=self.color,
                                outline=self.color)

    def clear(self):
        self.canvas.delete("all")
        self.digit_label['text'] = "?"

    def check_digit(self):
        img = Image.open(io.BytesIO(self.canvas
                                    .postscript(colormode='color')
                                    .encode('utf-8')))
        img = img.resize(self.result_image_size,
                         Image.ANTIALIAS)
        result_image = list(map(lambda x: abs((255 - x[0])/255),
                                list(img.getdata())))

        img.save('./images/digit.jpg')
        self.digit_label['text'] = self.neuron_net.recognize(result_image)
