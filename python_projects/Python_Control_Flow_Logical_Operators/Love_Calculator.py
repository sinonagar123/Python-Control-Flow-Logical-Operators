print("Welcome to True Love Calculator")
print("-------------------------------")
y_name=input("Enter your name : ") #first name
l_name=input("Enter their name: ") # second name
name=y_name+l_name #concating both names
lower_name=name.lower() #converting into lower case

t_val=name.count("t") # checking how many t
r_val=name.count("r")# checking how many r
u_val=name.count("u")# checking how many u
e_val=name.count("e")# checking how many e
l_val=name.count("l") # checking how many l
o_val=name.count("o")# checking how many 0
v_val=name.count("v")# checking how many v
le_val=name.count("e")# checking how many e
true_val=t_val +r_val + u_val + e_val # calculating true count values
love_val=l_val +o_val + v_val + le_val # calculating love count value
true_love=str(true_val)+str(love_val) #concatinating both true love
truelove=int(true_love)#converting to int
if truelove < 10 or truelove > 90:
    print("Your love score is ",true_love+" you go together coke and mentos")
elif truelove > 40 and truelove <50:
    print("Your love score is ",true_love+"you are alright together")
else:
    print("Your love score is ",true_love)
 