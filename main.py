import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        category = bmi_category(bmi)

        result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


# Main window
window = tk.Tk()
window.title("BMI Calculator")

# Labels and input fields
label_weight = tk.Label(window, text="Enter your weight (kg):")
label_weight.pack()

entry_weight = tk.Entry(window)
entry_weight.pack()

label_height = tk.Label(window, text="Enter your height (m):")
label_height.pack()

entry_height = tk.Entry(window)
entry_height.pack()

# Button to calculate BMI
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the application
window.mainloop()
