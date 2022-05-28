import tkinter
import grpc
import hello_pb2_grpc
import hello_pb2


class Area:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Area")
        self.result = tkinter.StringVar()
        self.entry = tkinter.Entry(self.main_window)
        self.entry.grid(row=0, column=0)
        self.entry1 = tkinter.Entry(self.main_window)
        self.entry1.grid(row=0, column=1)
        button1 = tkinter.Button(self.main_window, text="Calculate", command=self.calculate)
        button1.grid(row=0, column=2)
        self.label1 = tkinter.Label(self.main_window, textvariable=self.result, width=3, height=2)
        self.label1.grid(row=0, column=3)

    def run(self):
        self.main_window.mainloop()

    def calculate(self):
        width = int(self.entry.get())
        length = int(self.entry1.get())
        self.result.set(self.send_area(width, length))

    def send_area(self, width, length):
        with grpc.insecure_channel('localhost:12346') as channel:
            stub1 = hello_pb2_grpc.GreeterStub(channel)
            response1 = stub1.CalculateArea(hello_pb2.GiveSide(side1=width, side2=length))
            return response1.area


login = Area()
login.run()