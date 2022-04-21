print("BMI of a person")
print("---------------")
weight=input("Enter the weight in Kg: ")# entering weight
if weight.isdigit():# checking whether it is digit
    value_wgt=float(weight) #converting into float
    height=input("Enter the height in cm: ") # entering height in centimeter
    if height.isdigit(): # checking whether it is digit
        value_hgt=float(height) # converting into float
        value_m=value_hgt/100  # converting into metere
        bmi=value_wgt/(value_m**2) # checking BMI 
        
        answer = str(round(bmi, 2)) # rounding float
        print("Your BMI is ", answer)
        if bmi< 18.5: # checking underweight
            print("You are underweight")
        elif bmi >18.5 and bmi < 25: # checking noraml within a range
            print("You are Normal")
        elif bmi >25 and bmi < 30:
            print("You are overweight")
        else:
            print("You are Obse")
    else:
        print("Height should be in numbers") # not in numbers
else:
    print("weight should be in numbers") # not in number