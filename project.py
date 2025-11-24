import tkinter as tk

root = tk.Tk()                     
root.title("BMI Calculator")
root.geometry("300x500")           

def bmi_calc():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    bmi_label.config(text=f"BMI: {bmi:.2f}")

height_label = tk.Label(root, text="Height(metre):")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

weight_label = tk.Label(root, text="Weight(Kg):")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

bmi_label = tk.Label(root, text="")
bmi_label.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=bmi_calc)
calculate_button.pack()

root.mainloop()


