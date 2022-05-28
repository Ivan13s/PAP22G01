import json
import time
import tkinter
from tkinter import *



import requests

# root=tkinter.Tk()
# root.attributes('-fullscreen',True)
# root.title('MyApp')
# label1=tkinter.Label(root, text='Green Text',bg='#000000',)
# label1.grid(row=0, column=0)
def request():

    for i in range(3):
        time.sleep(1)
        result=requests.get(url="https://csrng.net/csrng/csrng.php?min=0&max=255")
        lista=result.json()[0]["random"]
        Hex=hex(lista)
        print(Hex)
        return Hex



def change_color():
    pass



request()




# root.mainloop()