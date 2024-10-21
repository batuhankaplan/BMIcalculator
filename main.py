import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(entry_weight.get())  # Kiloyu al
        height_cm = float(entry_height.get())  # Boyu cm olarak al
        height_m = height_cm / 100  # Boyu metreye çevir
        bmi = weight / (height_m ** 2)  # BMI hesapla
        category = bmi_category(bmi)  # Kategori bul

        # Sonucu ekranda göster
        result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")


def bmi_category(bmi):
    if bmi < 16:
        return "Severe Thinness"
    elif 16 <= bmi < 16.9:
        return "Moderate Thinness"
    elif 17 <= bmi < 18.4:
        return "Mild Thinness"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif 30 <= bmi < 34.9:
        return "Obesity Class I"
    elif 35 <= bmi < 39.9:
        return "Obesity Class II"
    else:
        return "Obesity Class III"


# Ana pencereyi oluştur
window = tk.Tk()
window.title("BMI Calculator")

#Pencere çözünürlüğü (genişlikxuzunluk)
window.geometry("400x200")


# Kilo için etiket ve giriş alanı
label_weight = tk.Label(window, text="Enter your weight (kg):")
label_weight.pack()

entry_weight = tk.Entry(window)
entry_weight.pack()

# Boy için etiket ve giriş alanı
label_height = tk.Label(window, text="Enter your height (cm):")
label_height.pack()

entry_height = tk.Entry(window)
entry_height.pack()

# BMI hesaplama düğmesi
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Sonuçları göstermek için etiket
result_label = tk.Label(window, text="")
result_label.pack()

# Uygulamayı çalıştır
window.mainloop()
