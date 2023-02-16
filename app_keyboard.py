from keyboard_commands import *
from tkinter import ttk
from ttkthemes import ThemedTk

PAUSE = 3.0
t = PAUSE

def NEXT(a):
	window.withdraw()
	copy()
	t
	switch_screen()
	t
	select_area()
	t
	paste()
	t
	r_arrow()
	t
	backspace()
	t
	enter()
	t
	switch_screen()
	t
	d_arrow()
	window.deiconify()

def CHECK(b):
	window.withdraw()
	r_arrow()
	t
	u_arrow()
	t
	num(nome='CHECK')
	t
	l_arrow()
	t
	d_arrow()
	window.deiconify()
	
def ERROR(c):
	window.withdraw()
	r_arrow()
	t
	u_arrow()
	t
	num(nome='ERROR')
	t
	l_arrow()
	t
	d_arrow()
	window.deiconify()

def EXIT(d):
	window.destroy()
	
window = ThemedTk(theme='arc')
style = ttk.Style
window.geometry('200x180-120+800')
window.resizable(False,False)

title = ttk.Label(text='App Comandos', anchor='center')
b1 = ttk.Button(window, text='Prosseguir', command=NEXT)
b2 = ttk.Button(window, text='Confirmar', command=CHECK)
b3 = ttk.Button(window, text='Erro', command=ERROR)
b4 = ttk.Button(window, text='Exit', command=EXIT)

title.pack(fill='both', padx=5, pady=5,)
b1.pack(fill='both', padx=5, pady=5,)
b2.pack(fill='both', padx=5, pady=5,)
b3.pack(fill='both', padx=5, pady=5,)
b4.pack(fill='both', padx=5, pady=5,)

window.bind('<Return>', lambda a: NEXT(a))
window.bind('<Key-0>', lambda b: CHECK(b))
window.bind('<Key-1>', lambda c: ERROR(c))
window.bind('<Escape>', lambda d: EXIT(d))

window.mainloop()


