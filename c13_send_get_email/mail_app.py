import tkinter
from c11_tkinter.app6 import MyApp
from c13_send_get_email.part1 import MainMenu

login = MyApp()
login.run()
# print(login.username_)
# print(login.password_)

window = tkinter.Tk()
main_menu = MainMenu(window,login.username_,login.password_)

main_menu.run()
