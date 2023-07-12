#ask user for input
weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your heigt in metres: "))
#calculate BMI
BMI = weight / height **2
#round off BMI to one decimal
BMI = round(BMI, 1)
print(f"The body mass index is: {BMI}.")

print("\n.....BMI Categories.....")
#tell user whether he is underweight or overweight
print("<18.5     :Underweight")
print("18.5-24.9 :Normal Weight")
print("25-29.9   :Overweight")
print(">=30      :Obesity")