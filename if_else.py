# if statement
# Syntax:
# if condition:
#           statement


age=int(input("Enter your age:"))

if age>= 18:
    print("Congratulations! Your are eligible for voting.")


# pass statement
# use for skip if statement without writing any condition

age=int(input("Enter your age:"))

if age< 18:
    pass

# else statement
# Syntax:
# if condition:
#           statement
#  else:
#        statement


age=int(input("Enter your age:"))

if age>= 18:
    print("Congratulations! Your are eligible for voting.")
else:
    print("Sorry!! Your are not eligible for voting.")


# nested if-else statement
# Syntax:
# if condition:
#        statement
#  else:
#      if condition:
#             statement
#  else:
#       statement

age=int(input("Enter your age:"))

if age> 18:
    print("Congratulations! Your are eligible for voting.")
else:
    if age == 18:
        print("Congratulations! for you first voting..")
    else:
        print("Sorry!! Your are not eligible for voting.")


#  if elif else statement
# Syntax:
# if condition:
#        statement
#  elif condition:
#             statement
#  else:
#       statement

age=int(input("Enter your age:"))

if age> 18:
    print("Congratulations! Your are eligible for voting.")
elif age == 18:
    print("Congratulations! for you first voting..")
else:
    print("Sorry!! Your are not eligible for voting.")


# in keyword
# Syntax:
# if word in string:
#           statement
#   else:
#      statement

eligible = "Mr"
name = input("Enter your nick name: ")

if eligible in name.lower():
    print("Your name start with Mr.")
else:
     print("Your name is not start with Mr.")


