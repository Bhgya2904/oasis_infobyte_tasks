def BMI(weight,height):
    bmi=(weight/(height*height))*10000
    return bmi

def category(bmi):
    if bmi<=18.4:
         return "Under Weight"
    elif bmi>=18.5 and bmi<=24.9:
         return "Normal"
    elif bmi>=25 and bmi<=39.9:
         return "Over Weight"
    else:
         return "Obesity"
try:
    weight=float(input("enter your weight in Kg:"))
    height=float(input("Enter your height in cm:"))
    if weight<0 and height<0:
        print("please enter valid input")
    else:
        bmi=BMI(weight,height)
        print("Your Body Mass Index is:",bmi)
        print("category:",category(bmi))
except ValueError:
    print("value error")