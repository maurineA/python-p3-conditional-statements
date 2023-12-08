# # Python
# dog = "cuddly"

# if dog == "hungry":
#     owner = "Refilling food bowl."
# elif dog == "thirsty":
#     owner = "Refilling water bowl."
# elif dog == "playful":
#     owner = "Playing tug-of-war."
# elif dog == "cuddly":
#     owner = "Snuggling."
# else:
#     owner = "Reading newspaper."


# print(owner)


# age = 8

# is_child="baby" if age < 5 else "is a teen"

# print(is_child)



# def divide(num1, num2):

#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except:
#         print("An error occurred")


# divide(18,3)

# def divide(num1, num2):
#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot be equal to 0")
#     except TypeError:
#         print("Error: input must be of type int or float")

# divide(18,5)

dog = "cuddly"

activities = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

# Remember that a dictionary's .get() method lets us set a default value!
owner = activities.get(dog, "Reading newspaper.")

print(owner)