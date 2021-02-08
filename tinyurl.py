import pyshorteners
from tkinter import ttk
import tkinter as tk
import validators

win = tk.Tk()
win.geometry("500x300")
win.title("URL Shortener")


def shorten():
    url = link.get()
    if not validators.url(url):
        result_text.insert(0.0, "Wrong URL, try again\n")
    else:
        _link = pyshorteners.Shortener()
        result = _link.tinyurl.short(url)
        result_text.insert(0.0, f"Result: {result}\n")


label = ttk.Label(text="Enter the link").pack(pady=10)
link = ttk.Entry(win, width=300)
link.bind("<Return>", lambda event: shorten())
link.pack(padx=10, pady=10)
btn = ttk.Button(win, text='Click to convert', command=shorten).pack(pady=10)
result_text = tk.Text(win)
result_text.pack(padx=10, pady=10)

win.mainloop()
