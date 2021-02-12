import pyshorteners
from tkinter import ttk
import tkinter as tk
import validators
from tkinter import messagebox as msg
import webbrowser

win = tk.Tk()
win.geometry("500x300")
win.title("URL Shortener")


def shorten():
    url = link.get()
    if len(url) == 0:
        msg.showerror("Error", "Field is empty")
    elif "tinyurl" in url:
        msg.showerror("Error", "URL is same as converted")
    elif not validators.url(url):
        msg.showerror("Error", "Wrong URL, try again")
    else:
        result_text.delete(0.0, tk.END)
        _link = pyshorteners.Shortener()
        result = _link.tinyurl.short(url)
        result_text.insert(0.0, f"{result}\n", "tag1")


def callback():
    url = result_text.get(0.0, tk.END)
    webbrowser.open(url)


label = ttk.Label(text="Enter the link").pack(pady=10)
link = ttk.Entry(win, width=300)
link.bind("<Return>", lambda event: shorten())
link.pack(padx=10, pady=10)
btn = ttk.Button(win, text='Click to convert', command=shorten).pack(pady=10)
label1 = ttk.Label(text="Click to open").pack()
result_text = tk.Text(win, cursor="arrow")
result_text.pack(padx=10, pady=10)
result_text.tag_config("tag1", foreground="blue")
result_text.tag_bind("tag1", "<Button-1>", lambda e: callback())

win.mainloop()
