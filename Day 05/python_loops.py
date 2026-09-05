# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(max_score)


# total = 0
# for number in range (1, 101):
#     total += number 
#     # if number == 100:
# print(total)

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#        print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

import random
     
password=""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for letras in range(nr_letters):
        password += random.choice(letters)
        # print(random.choice(letters, end=""))
        # continue

for numeros in range(nr_numbers):
    password += random.choice(numbers)
    # print(random.choice(numbers, end=""))
    # continue

for simbolos in range(nr_symbols):
    password += random.choice(symbols)
    # print(random.choice(symbols, end=""))
                
word = list(password)

random.shuffle(word)
delimiter = ""# Define a delimiter
join_str = delimiter.join(word)

print(f"You password is: {join_str}")





# for letras in range(nr_letters + 1):
#     if letras > 0:
#         print(random.choice(letters))
#         continue

#     for numeros in range(nr_numbers + 1):
#         if numeros > 0:
#             print(random.choice(numbers))
#             continue

#         for simbolos in range(nr_symbols + 1):
#             if simbolos > 0:
#                 print(random.choice(symbols))
  
        