import tkinter as tk
def check_strength():
    password = entry.get()
    length = len(password)
    if length < 6:
        result_label.config(text="Password Strength: Weak")
    elif length < 10:
        result_label.config(text="Password Strength: Medium")
    else:
        result_label.config(text="Password Strength: Strong")
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")
label = tk.Label(root, text="Enter Password:")
label.pack(pady=10)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)
button = tk.Button(root, text="Check Strength", command=check_strength)
button.pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)
root.mainloop()