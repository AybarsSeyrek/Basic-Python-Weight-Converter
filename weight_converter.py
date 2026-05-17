# Python weight converter
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

# If the user entered K, convert kilograms to pounds
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
# If the user entered L, convert pounds to kilograms
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
# If the user entered anything other than K or L, show an error message
else:
    print(f"{unit} was not valid")
