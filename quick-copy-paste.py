import pyperclip
import tkinter as tk

snippets = {
    "X": "Desc-X",
    "Y": "Desc-Y",
}

def copy_text(text):
    pyperclip.copy(text)

root = tk.Tk()
root.title("Quick Copy Tool")

for label, content in snippets.items():
    btn = tk.Button(root, text=label, command=lambda c=content: copy_text(c))
    btn.pack(pady=5)

root.mainloop()
