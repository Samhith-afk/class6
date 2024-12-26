a=23
b=24
c=22
if a>b or a<c:
    print("we are using or operater")
elif a>b and a<c:
    print("we are using and operater")
#task 3
height=float(input("enter your height in cm"))
weight=float(input("enter your weight in kg"))
bmi=weight / (height/100)**2
print("your BMI is",bmi)
if bmi<=18.4:
    print("you are underweight")
elif bmi<=24.9:
    print("you are healthy")
elif bmi<= 29.9:
    print("you are owerweight")
elif bmi<= 34.9:
    print("your severely overweight")
elif bmi<= 39.9:
    print("your obese")
else:
    print("your severely obese")