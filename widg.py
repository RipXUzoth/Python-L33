import tkinter as tk
from datetime import date
root = tk.Tk()
root.title('Getting started with widgets')
lbl = tk.Label(text="hey there!", fg="white", bg = "blue", height = 1, width = 300)
name_lbl = tk.Label(text="full name", bg = "red")
name_entry = tk.Entry()
def display():
    name = name_entry.get()
    message = "Welcome to the applcation! \nToday's date is: "
    greet = "hello "+name+"\n"
    text_box.insert(tk.END, greet)
    text_box.insert(tk.END, message)
    text_box.insert(tk.END, date.today())
text_box = tk.Text(height=3)
btn = tk.Button(text="begin", command=display, height=1, bg = "black", fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()