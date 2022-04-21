

print("WELCOME TO THE TIP CALCULATOR")
total_bill=input("What was the total bill :")# total bill amt


to_flo=float(total_bill) # converting total amt into float
bill_total=isinstance(to_flo,float) # checking entered data type is float#

per=float(input("What percentage tip would you like to give 10, 12 or 15 :"))# converting percentage into float
total_per=(per*to_flo)/100 #calucalating percentage
#print(total_per)
total_val=to_flo+total_per #adding percentage to total bill
#print(total_val)
spilt_bill=int(input("How many peopele to split the bill :")) #converting person to split in int
bill=round(total_val/spilt_bill,2) # dividing total amt with split people and rounding as 2 float
print("Each person should pay ",bill)