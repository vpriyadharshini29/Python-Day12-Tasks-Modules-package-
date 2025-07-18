def km_to_miles(km):
    return km * 0.621371

km = float(input("Enter distance in kilometers: "))
print(f"{km} km is equal to {km_to_miles(km):.2f} miles.")
