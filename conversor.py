from tkinter import *
from tkinter import ttk

#cores
colorBG = "#0d1117"
color2 = "#161b22"
grey ="#5b5b5b"
white = "#ffffff"

page = Tk()
page.title('')
page.geometry('400x310')
page.configure(bg=colorBG)

style = ttk.Style()
style.theme_use('clam') #Melhores thema tkinter "default" & "clam"
ttk.Separator(page, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=200)

#Separando as Frames em 
frame_superior = Frame(page, width=400, height=60, bg=color2, pady=0, padx=0)
frame_superior.grid(row=1, column= 0)
frame_inferior = Frame(page, width=400, height=300, bg=colorBG, pady=12, padx=20)
frame_inferior.grid(row=2, column= 0, sticky=NW)


titulo = Label(frame_superior, text="Conversor de Base Numérica", relief=FLAT, anchor='center', font=('System 20'), bg=color2, fg=white)
titulo.place(x=10, y=15)


bases = ['BINARIO', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']
selectBox = ttk.Combobox(frame_inferior, width=14, justify=CENTER, font=('Ivy 10 bold'))
selectBox['values'] = (bases)
selectBox.place(x=35, y=10)

inputBox = Entry(frame_inferior, width=11, justify=CENTER, font=("", 10), highlightthickness=1, relief='solid')
inputBox.place(x=160, y=10)

btn = Button(frame_inferior, text="CONVERTER", relief=RAISED, overrelief=RIDGE, font=('Ivy 8'), bg=grey, fg=color2)
btn.place(x=250, y=10)


#autput
label_binario = Label(frame_inferior, text="BINARIO", width=12, relief=FLAT, anchor='nw', font=('Ivy 10'), bg=grey, fg=white).place(x=35, y=60)
label_binario = Label(frame_inferior, text="", width=13, relief=FLAT, anchor='center', font=('Ivy 10'), fg='#000000').place(x=170, y=60)

label_octal = Label(frame_inferior, text="OCTAL", width=12, relief=FLAT, anchor='nw', font=('Ivy 10'), bg=grey, fg=white).place(x=35, y=100)
label_octal = Label(frame_inferior, text="", width=13, relief=FLAT, anchor='center', font=('Ivy 10'), fg='#000000').place(x=170, y=100)

label_decimal = Label(frame_inferior, text="DECIMAL", width=12, relief=FLAT, anchor='nw', font=('Ivy 10'), bg=grey, fg=white).place(x=35, y=140)
label_decimal = Label(frame_inferior, text="", width=13, relief=FLAT, anchor='center', font=('Ivy 10'), fg='#000000').place(x=170, y=140)

label_hexadecimal = Label(frame_inferior, text="HEXADECIMAL", width=12, relief=FLAT, anchor='nw', font=('Ivy 10'), bg=grey, fg=white).place(x=35, y=180)
label_hexadecimal = Label(frame_inferior, text="", width=13, relief=FLAT, anchor='center', font=('Ivy 10'), fg='#000000').place(x=170, y=180)


page.mainloop()