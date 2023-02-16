from pyautogui import *

def copy():
	hotkey('ctrl', 'c')
def switch_screen():
	hotkey('alt', 'tab')
def select_area():
	hotkey('ctrl', 'a')
def paste(): 
	hotkey('ctrl', 'v')
def r_arrow():
	press('right')
def l_arrow():
	press('left')
def u_arrow():
	press('up')
def d_arrow():
	press('down')
def backspace():
	press('backspace')
def enter():
	press('enter')
def num(nome):
	if nome =='CHECK':
		press('0')
	else:
		press('1')