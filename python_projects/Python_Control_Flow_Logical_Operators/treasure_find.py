

print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island")
print("Your mission is to find treasue")
way_one=input("You are at cross road. Where do you want to go Type 'L' for Left or 'R' for Right : ")
way_ans1=way_one.lower()
len_way_ans1=len(way_ans1)
if len_way_ans1==1 and way_ans1=='l':
    way_two=input("You came to a lake. There is an island in the middle of the lake. Type 'W' to wait for a boat or Type 'S' to Swim across.")
    way_ans2=way_two.lower()
    len_way_ans2=len(way_ans2)
    if len_way_ans2==1 and way_ans2=='w':
        way_three=input("You arrived at island unharmed. There is a house with 3 doors.Type 'R' for Red Door, 'Y' for Yellow Door or 'B' for Blue Door ")
        way_ans3=way_three.lower()
        len_way_ans3=len(way_ans3)
        if len_way_ans3==1 and way_ans3=='y':
            print("You Won !!!!!!")
        elif len_way_ans3==1 and way_ans3=='r':
            print("Burned by Fire !!! Game Over")
        elif len_way_ans3==1 and way_ans3=='b':
            print("Eaten by Beast !!! Game Over")
        else:
            print("Game Overs")
    else:
        print("Attacked by trout !!! Game Over")
else:
    print("Fall into Hole!!! Game Over")
    
