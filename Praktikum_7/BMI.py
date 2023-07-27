def calculate_bmi(height, weight):
    return weight / (height ** 2)

def bmi_category(bmi_value):
    if bmi_value < 18.5:
        return "Kurus"
    elif 18.5 <= bmi_value < 24.9:
        return "Normal"
    elif 24.9 <= bmi_value < 29.9:
        return "Gemuk"
    else:
        return "Obesitas"

def bmi_calculator_decorator(func):
    def wrapper(height, weight):
        bmi = func(height, weight)
        category = bmi_category(bmi)
        return bmi, category
    return wrapper

@bmi_calculator_decorator
def calculate_bmi_with_category(height, weight):
    return calculate_bmi(height, weight)

if __name__ == "__main__":
    height = float(input("Masukkan tinggi badan (dalam meter): "))
    weight = float(input("Masukkan berat badan (dalam kilogram): "))

    bmi, category = calculate_bmi_with_category(height, weight)
    print(f"BMI Anda: {bmi:.2f}")
    print(f"Kategori Berat Badan: {category}")
