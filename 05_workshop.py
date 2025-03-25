#program to calculate BMI


def calculate_bmi(weight, height):
    bmi = (weight * 100) / (height **2)
    return round(bmi,2)


weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height in cm:"))

bmi=calculate_bmi(weight, height)
print("Your BMI is: ",bmi)