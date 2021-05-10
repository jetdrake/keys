
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

file = open('tk_keys.txt', 'a')

def on_key_press(event):
    file.write("{keysym},{keycode},{char},\n".format(keysym=event.keysym, keycode=event.keycode, char=event.char))



print('type keys to add them to file')
root = tk.Tk()
root.wait_visibility(root)
root.wm_attributes('-alpha',0.1)
root.bind('<KeyPress>', on_key_press)

root.mainloop()