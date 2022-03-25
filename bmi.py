

while True:
    weight = input("enter your weight (kg) : ")
    height = input("enter your heiht  (m)  : ")
    bmi = float(weight)/float(height)**2
    if bmi < 18.5:
       print("Underweight")
    if bmi >= 18.5:
       if bmi < 25:
          print("Normal")
    if bmi >= 25:
       if bmi < 30:
          print("Overweight")
    if bmi >= 30:
       print("Obesity")
    desire = input('do you wanna continue ? then press (y) or press (q) to quit ')
    if desire == "y":
        continue
    if desire == "q":
        break 