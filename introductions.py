# Write a function that takes 2 pieces of input (two people), and introduces one to another
# Prompt the user for 2 names
# Call your function, which should then print an introduction: introducing one person to the other

def introduction(person1, person2):
    print("Hello", person1, "meet ", person2 + ".")

p1 = input("Name a person: ")
p2 = input("Name another person: ")

introduction(p1, p2)