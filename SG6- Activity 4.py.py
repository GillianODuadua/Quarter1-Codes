fullname = input("Enter your full name (First, Middle, Last): ")
parts = fullname.split(",")
First = parts[0].strip().capitalize()
Middle = parts[1].strip().capitalize()
Last = parts[2].strip().title()
MiddleInitial = Middle[0].upper() + "."
print("Formatted Name:", Last + ", " + First + " " + MiddleInitial)
