import tkinter

def print_something():
    print('message')

main_window=tkinter.Tk()
main_window.title('Myapp')

button1=tkinter.Button(main_window,text="Sign In",command=print_something)
button1.grid(row=0,column=0)


text=tkinter.Text(main_window)
text.grid(row=0,column=1)

entry=tkinter.Entry(main_window)
entry.grid(row=0,column=1)



main_window.mainloop()