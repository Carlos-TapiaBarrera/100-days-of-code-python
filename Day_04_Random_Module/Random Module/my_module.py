import random

# random_string = random.randint(0, 1)
# if random_string == 0:
#    print("Head")
# else:
#    print("Tails")


# friends = ["Alice", "Bod", "Charlie", "David", "Emanuel"]
# print(random.choice(friends))

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[0][5])


while True:
   choice = int(input("What do you choose? Type 0 for Paper, 1 for Rock or 2 for Scissors: "))

   if choice == 0:
      print("""   Paper
    
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)""")
      break
   elif choice == 1:
      print(""" Rock
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)
   """)
      break
   elif choice == 2:
      print("""   Scissors
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)
   """)
      break
   else:
      print("Invalid option. Try again.")

computer = ("""   Paper
    
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)""", 

      """ Rock
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)
   """, 

   """  Scissors
            _______
         ---'   ____)____
                  ______)
               __________)
      VK      (____)
         ---.__(___)
      )""")
   
print(random.choice(computer))