import tkinter as tk
from tkinter import messagebox
from spreadsheet import update_spreadsheet

def update_value():
    path = 'test_record.xlsx'
    try:
        new_value = update_spreadsheet(path)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Spreadsheet GUI")

increment_button = tk.Button(root, text="Update Spreadsheet", command=update_value)
increment_button.pack()

root.mainloop()