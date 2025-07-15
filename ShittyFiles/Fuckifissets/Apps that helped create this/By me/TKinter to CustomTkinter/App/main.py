import tkinter as tk
from tkinter import filedialog, messagebox
import re
import os

def convert_tkinter_to_customtkinter(source_path, output_path):
    with open(source_path, "r", encoding="utf-8") as src:
        code = src.read()

    # Replace imports
    code = re.sub(r"import tkinter as tk", "import customtkinter as ctk", code)
    code = re.sub(r"from tkinter import (.+)", "import customtkinter as ctk", code)

    # Replace common widgets
    widget_map = {
        "tk.Tk(": "ctk.CTk()",
        "tk.Label(": "ctk.CTkLabel(",
        "tk.Button(": "ctk.CTkButton(",
        "tk.Entry(": "ctk.CTkEntry(",
        "tk.Checkbutton(": "ctk.CTkCheckBox(",
        "tk.Text(": "ctk.CTkTextbox(",
    }

    for old, new in widget_map.items():
        code = code.replace(old, new)

    # Inject theme setup
    if "ctk.set_appearance_mode" not in code:
        theme_setup = '\nctk.set_appearance_mode("dark")\nctk.set_default_color_theme("blue")\n'
        code = re.sub(r"(ctk\.CTk\(\))", r"\1" + theme_setup, code, count=1)

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(code)

def browse_file():
    path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, path)

def run_conversion():
    source = entry_path.get()
    custom_name = entry_name.get().strip()
    if not source or not custom_name:
        messagebox.showerror("Missing Info", "Choose a file and name the output.")
        return

    dir_path = os.path.dirname(source)
    new_file = os.path.join(dir_path, f"{custom_name}.py")

    try:
        convert_tkinter_to_customtkinter(source, new_file)
        messagebox.showinfo("Success", f"✅ Converted to:\n{new_file}")
    except Exception as e:
        messagebox.showerror("Conversion Failed", str(e))

# GUI setup
root = tk.Tk()
root.title("🧬 Tkinter Mutator")
root.geometry("420x220")

tk.Label(root, text="Select Tkinter .py file").pack(pady=(10, 0))
entry_path = tk.Entry(root, width=50)
entry_path.pack(pady=5)
tk.Button(root, text="Browse", command=browse_file).pack()

tk.Label(root, text="Name for converted file").pack(pady=(15, 0))
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

tk.Button(root, text="Mutate GUI", command=run_conversion, bg="#222", fg="#0f0").pack(pady=20)

root.mainloop()
