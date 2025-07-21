import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Multiply Two Numbers")
root.geometry("300x200")

# Labels and Entry fields
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Button to calculate
tk.Button(root, text="Calculate Product", command=calculate_product).pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="Product: ")
result_label.pack(pady=10)

# Run the application
root.mainloop()
