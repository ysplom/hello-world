from tkinter import *
import datetime,pyautogui,threading

win=Tk()
win.geometry('400x400')

b=datetime.datetime.today()

def ab():
    global running
    t10=e10.get()
    t11 = e11.get()
    t12 = e12.get()
    t20 = e20.get()
    t21 = e21.get()
    t22 = e22.get()

    while running:
        win.after(1000)
        b = datetime.datetime.today()
        if int(t10)<=int(b.strftime('%H')):
            if int(t11) <= int(b.strftime('%M')):
                if int(t12) <= int(b.strftime('%S')):
                    pyautogui.click()
                    break
    while running:
        win.after(1000)
        b = datetime.datetime.today()
        if int(t20)<=int(b.strftime('%H')):
            if int(t21) <= int(b.strftime('%M')):
                if int(t22) <= int(b.strftime('%S')):
                    pyautogui.click()
                    break

def a():
    global running
    if running:
        running = False
        but.config(text='Start')
    else:
        running = True
        threading.Thread(target=ab).start()
        but.config(text='Stop')

but=Button(win,text='START',command=a)
but.grid(column=10,row=0)

running = False

e10=Entry(win,width=2)
e10.insert(0,8)
e10.grid(column=0,row=0)
e20=Entry(win,width=2)
e20.insert(0,19)
e20.grid(column=0,row=1)
e11=Entry(win,width=2)
e11.insert(0,b.strftime('%M'))
e11.grid(column=1,row=0)
e21=Entry(win,width=2)
e21.insert(0,b.strftime('%M'))
e21.grid(column=1,row=1)
e12=Entry(win,width=2)
e12.insert(0,b.strftime('%S'))
e12.grid(column=2,row=0)
e22=Entry(win,width=2)
e22.insert(0,'')
e22.insert(0,b.strftime('%S'))
e22.grid(column=2,row=1)




win.mainloop()