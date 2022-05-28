import asyncio
import json
import tkinter
import random
from tkinter import Toplevel

import aiohttp
import requests

from c6_asynio.app3 import zone_data



async def time_zone_getter():
    async with aiohttp.ClientSession() as client:
        result = await client.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/Europe')
        return json.loads(await result.text())



async def time_getter():
    async with aiohttp.ClientSession() as client:
        while not zone_data:
            await asyncio.sleep(1)
        else:
            city = zone_data.pop()
            result = await client.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/{city}')
            print(json.loads(await result.text()))


class Exam():
    title = 'Main Menu'
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Exam")
        self.add_menu()
        lista_timezone=asyncio.run(time_zone_getter())
        print(lista_timezone)
        for i in range(9):
            for j in range(5):
                self.__setattr__(f'label{i, j}',
                                 tkinter.Label(self.main_window, text=self.is_bomb(), width=10, height=2))
                self.__setattr__(f'button{i, j}', tkinter.Button(self.main_window, text=lista_timezone.pop(),width=15,height=5, command=self.new_window))
                self.__getattribute__(f'label{i, j}').grid(row=i, column=j)
                self.__getattribute__(f'button{i, j}').grid(row=i, column=j)

    def add_menu(self):
        main_l1 = tkinter.Menu(self.main_window)
        self.main_window.config(menu=main_l1)

        main_l2 = tkinter.Menu(self.main_window)
        main_l1.add_cascade(label='File', menu=main_l2)

        main_l3 = tkinter.Menu(self.main_window)
        main_l2.add_cascade(label='New', menu=main_l3)

        main_l3.add_command(label='New Project', command=self.new_window)
        main_l3.add_command(label='New Project in same Window', command=quit)

        main_l2.add_separator()

        main_l2.add_command(label='Close', command=quit)


    def new_window(self):
        new_window = Exam()
        new_title = self.title + ' Copy'
        new_window.main_window.title(new_title)
        new_window.run()

    def time_getter(city: str):
        pass
    def is_bomb(self):
        return 1

    def do_nothing(self):
        pass

    def run(self):
        self.main_window.mainloop()



login = Exam()
login.run()