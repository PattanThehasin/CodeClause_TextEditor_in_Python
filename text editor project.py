
import tkinter as tk
from tkinter import filedialog, messagebox

current_file = None

def open_file():
    global current_file
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r') as file:
                text_editor.delete('1.0', tk.END)
                text_editor.insert(tk.END, file.read())
            current_file = file_path
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {str(e)}")

def save_file():
    global current_file
    if current_file:
        try:
            with open(current_file, 'w') as file:
                file.write(text_editor.get('1.0', tk.END))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")
    else:
        save_file_as()

def save_file_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(text_editor.get('1.0', tk.END))
            current_file = file_path
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")

root = tk.Tk()
root.title("Text Editor")

# Create a text widget
text_editor = tk.Text(root)
text_editor.pack()

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add a File menu with Open, Save, and Save As options
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)

root.mainloop()
