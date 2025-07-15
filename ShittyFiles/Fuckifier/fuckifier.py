import customtkinter as ctk
import base64
import random

def to_hex(s): return s.encode().hex()
def from_hex(s): return bytes.fromhex(s).decode('utf-8', errors='replace')

def to_base64(s): return base64.b64encode(s.encode()).decode()
def from_base64(s): return base64.b64decode(s).decode('utf-8', errors='replace')

def flip_text(s):
    return ''.join(reversed(s.translate(str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz∀𐐒ƆᗡƎℲ⅁HIſʞ⅂WNOԀQᴚS⊥∩ΛMⅩ⅄Z0ƖᄅƐㄣϛ9ㄥ86"
    ))))

def glitchify(s):
    chars = ['@', '#', '%', '&', '*', '!', '~', '^', 'ø', '∆']
    return ''.join(random.choice(chars) if random.random() < 0.15 else c for c in s)

def descramble_glitch(s):
    return ''.join(c for c in s if c.isalnum() or c in '=/')

def scramble():
    input_text = entry.get()
    result = to_hex(input_text)
    result = to_base64(result)
    result = flip_text(result)
    result = result[::-1]
    result = to_hex(result)
    result = to_base64(result)
    result = glitchify(result)
    output_label.configure(text=f"Scrambled:\n{result}")
    copy_btn.configure(state="normal")
    last_result.set(result)

def redeem():
    result = entry.get()
    if glitch_var.get():
        result = descramble_glitch(result)
    if reverse_var.get():
        result = result[::-1]
    if unflip_var.get():
        result = result[::-1]
    if base64_var.get():
        try: result = from_base64(result)
        except: result = "[failed]"
    if hex_var.get():
        try: result = from_hex(result)
        except: result = "[failed]"
    output_label.configure(text=f"Decoded:\n{result}")
    copy_btn.configure(state="normal")
    last_result.set(result)

def copy_to_clipboard():
    final = last_result.get()
    root.clipboard_clear()
    root.clipboard_append(final)
    root.update()

# === GUI Setup ===
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Fuckifier")
root.geometry("600x500")

entry = ctk.CTkEntry(root, width=500)
entry.pack(pady=10)

mode_frame = ctk.CTkFrame(root)
mode_frame.pack()

ctk.CTkButton(mode_frame, text="Fuckifier", command=scramble).grid(row=0, column=0, padx=5)
ctk.CTkButton(mode_frame, text="Defuckifier", command=redeem).grid(row=0, column=1, padx=5)

ctk.CTkLabel(root, text="Options").pack(anchor='w', padx=20)

glitch_var = ctk.BooleanVar(value=True)
reverse_var = ctk.BooleanVar(value=True)
unflip_var = ctk.BooleanVar(value=True)
base64_var = ctk.BooleanVar(value=True)
hex_var = ctk.BooleanVar(value=True)

ctk.CTkCheckBox(root, text="Remove glitch symbols", variable=glitch_var).pack(anchor='w', padx=20)
ctk.CTkCheckBox(root, text="Reverse string", variable=reverse_var).pack(anchor='w', padx=20)
ctk.CTkCheckBox(root, text="Unflip characters", variable=unflip_var).pack(anchor='w', padx=20)
ctk.CTkCheckBox(root, text="Base64 → UTF-8", variable=base64_var).pack(anchor='w', padx=20)
ctk.CTkCheckBox(root, text="Hex → UTF-8", variable=hex_var).pack(anchor='w', padx=20)

output_label = ctk.CTkLabel(root, text="", wraplength=540, justify='left')
output_label.pack(pady=15)

last_result = ctk.StringVar()
copy_btn = ctk.CTkButton(root, text="Copy2Clip", command=copy_to_clipboard, state="disabled")
copy_btn.pack(pady=5)

root.mainloop()
