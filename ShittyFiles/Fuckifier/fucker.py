import tkinter as tk
import base64
import random

def to_hex(s): return s.encode().hex()
def from_hex(s): return bytes.fromhex(s).decode('utf-8', errors='replace')

def to_base64(s): return base64.b64encode(s.encode()).decode()
def from_base64(s): return base64.b64decode(s).decode('utf-8', errors='replace')

def flip_text(s):
    # Stylized mirror mapping (can be expanded)
    return ''.join(reversed(s.translate(str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz∀𐐒ƆᗡƎℲ⅁HIſʞ⅂WNOԀQᴚS⊥∩ΛMⅩ⅄Z0ƖᄅƐㄣϛ9ㄥ86"
    ))))

def glitchify(s):
    chars = ['@', '#', '%', '&', '*', '!', '~', '^', 'ø', '∆']
    return ''.join(random.choice(chars) if random.random() < 0.15 else c for c in s)

def descramble_glitch(s):
    return ''.join(c for c in s if c.isalnum() or c in '=/')

# === Scramble Workflow ===
def scramble():
    input_text = entry.get()
    result = to_hex(input_text)
    result = to_base64(result)
    result = flip_text(result)
    result = result[::-1]
    result = to_hex(result)
    result = to_base64(result)
    result = glitchify(result)
    output_label.config(text=f"Scrambled:\n{result}")
    copy_btn.config(state=tk.NORMAL)
    last_result.set(result)

# === Redeem Workflow ===
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

    output_label.config(text=f"Decoded:\n{result}")
    copy_btn.config(state=tk.NORMAL)
    last_result.set(result)

# === Clipboard ===
def copy_to_clipboard():
    final = last_result.get()
    root.clipboard_clear()
    root.clipboard_append(final)
    root.update()

# === GUI Setup ===
root = tk.Tk()
root.title("Fuckifier")

entry = tk.Entry(root, width=60)
entry.pack(pady=8)

mode_frame = tk.Frame(root)
mode_frame.pack()

tk.Button(mode_frame, text="Fuckifier", command=scramble).grid(row=0, column=0, padx=5)
tk.Button(mode_frame, text="Defuckifier", command=redeem).grid(row=0, column=1, padx=5)

# === Redeem Options ===
tk.Label(root, text="Options").pack(anchor='w', padx=10)

glitch_var = tk.BooleanVar(value=True)
reverse_var = tk.BooleanVar(value=True)
unflip_var = tk.BooleanVar(value=True)
base64_var = tk.BooleanVar(value=True)
hex_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Remove glitch symbols", variable=glitch_var).pack(anchor='w')
tk.Checkbutton(root, text="Reverse string", variable=reverse_var).pack(anchor='w')
tk.Checkbutton(root, text="Unflip characters", variable=unflip_var).pack(anchor='w')
tk.Checkbutton(root, text="Base64 → UTF-8", variable=base64_var).pack(anchor='w')
tk.Checkbutton(root, text="Hex → UTF-8", variable=hex_var).pack(anchor='w')

output_label = tk.Label(root, text="", wraplength=500, justify='left')
output_label.pack(pady=10)

last_result = tk.StringVar()
copy_btn = tk.Button(root, text="Copy2Clip", command=copy_to_clipboard, state=tk.DISABLED)
copy_btn.pack(pady=5)

root.mainloop()
