# # number1=int(input())
# # number2=int(input())

# # if number1 % number2 == 0:
# #     print("par")
# # else: 
# #     print("impar")


# bill = 0

# print("Welcome to Python pizza deliveries!")
# size = input("What size pizza do you want? S, M, L: ").upper

# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# else:
#     bill = 25

# pepperoni = input("Do you want pepperoni on your pizza ? Y or N: ").upper
# if pepperoni == "Y" and size == "S":
#     bill += 2
# elif pepperoni == "Y" and (size == "M" or size == "L"):
#     bill += 3 
# else:
#     print("Sin peperoni")

# extra_cheese = input("Do you want extra cheese? Y or N: ").upper
# if extra_cheese == "Y":
#     bill += 1
# else:
#     print("Sin queso")
    
# print(f"La cuenta total es {bill}")

print('''
*******************************************************************************
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
*******************************************************************************
''')

print("Welcome to treasure island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

left_right = input("Type 'left' or 'right' ")
print(left_right)

if left_right == "right":

    print("Fall into a hole. Game Over")

elif left_right == "left":

    print("You've come to a lake. There is an island in the middle of the lake.")

    wait_swim = input("Type 'wait' to wait for a boat. Type 'swim' to swim across ")

    if wait_swim == "wait":
        print("You wait for a boat.")
        door = input("Type 'blue' or 'red' or 'yellow' ")

        if door == "blue":
            print("Eaten by beasts. Game Over.")

        elif door == "red":
            print("Burned by fire. Game Over.")

        elif door == "yellow":
            print("You win")    

        else:
            print("Game Over.")


    elif wait_swim == "swim":
        print("Attacked by trout. Game Over.")

    else:
        print("Attacked by trout. Game Over.")

else:
        print("Fall into a hole. Game Over.")





    
    
