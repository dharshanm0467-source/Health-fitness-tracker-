# Health & Fitness Tracker

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
water = float(input("Enter water intake (liters): "))
calories = int(input("Enter calories consumed: "))
workout = int(input("Enter workout time (minutes): "))

# BMI Calculation
bmi = weight / (height * height)

print("\n----- Health Report -----")
print("BMI:", round(bmi, 2))
print("Water Intake:", water, "Liters")
print("Calories Consumed:", calories, "kcal")
print("Workout Time:", workout, "minutes")

# BMI Status
if bmi < 18.5:
    print("Status: Underweight")
elif bmi < 25:
    print("Status: Normal Weight")
elif bmi < 30:
    print("Status: Overweight")
else:
    print("Status: Obese")
