# # Functions with input
# # Create a function with multiple inputs

# def greet_with_name(name, last):
#     print(f"Hello {name} {last}")
#     print(f"How do you do {name} {last}?")
    

# greet_with_name("Jack", "Bauer")

# Modify the function so that it prints the expected values.


# def greet_with_name(name, location):
#     print(f"Hello {name} {location}")
#     print(f"How do you do {name} {location}?")
    

# greet_with_name("Jack", "Pudahuel")

# def greet_with(a, b):
#     print(a)
#     print(b)       

# greet_with(2,1)


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")        

# greet_with(location="Santiago", name="Jack")


# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
    
#     lower_names = combined_names.lower()
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
        
#     first_digit = t + r + u + e
        
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")

#     second_digit = l + o + v + e
        
#     score = int(str(first_digit)+str(second_digit))
#     print(r)
#     print(score)
        
# calculate_love_score("Kanye West", "Kim Kardashian")
    
def calculate_love_score(name1, name2):
    combined_names = name1 + name2

    lower_names = combined_names.lower()
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")

    first_digit = (t + r + u + e)

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    #e = lower_names.count("e") mejor definirla una sola vez

    second_digit = (l + o + v + e)

    score = int(str(first_digit)+str(second_digit))
    print(score)


calculate_love_score("Kanye West", "Kim Kardashian")