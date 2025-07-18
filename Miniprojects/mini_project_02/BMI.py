def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = calculate_bmi(weight, height)

print("Your BMI is:", bmi)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obese")
