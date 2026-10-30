# # Subscripting
# print("Hello"[0])

# mystery = 734_529.678
# print(type(mystery))

# print(type("Hello"))

# print("Number of letters in your name: " + str(len(input("Enter your name "))))

# print(6/2)

# float

# print("Welcome to the calculator")
# tip=int(input(f"How much tip would you like to give? 10, 12, or 15? "))
# people=int(input(f"How many people to split the bill? "))
# result=int(round(tip/people, 0))
# print(f"Each person should pay: {result}")


print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")