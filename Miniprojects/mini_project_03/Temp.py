def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

choice = input("Convert from (C/F)? ").upper()
temp = float(input("Enter the temperature: "))

if choice == 'C':
    print(f"{temp}°C is {c_to_f(temp)}°F")
elif choice == 'F':
    print(f"{temp}°F is {f_to_c(temp)}°C")
else:
    print("Invalid choice")
