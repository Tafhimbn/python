
str = "Python" # "P" = 0/-6, "y" = 1/-5, "t" = 2/-4, "h" = 3/-3, "o" = 4/-2, "n" = 5/-1

# Print compete string
print(str) 
print("This is a {} Program".format(str)) # Python 3
print(f"This is a {str} Program") # Python 3.6

# To print "P"
print("First Character of this String:",str[0])  # print first character
print("First Character of this String:",str[-6]) # print first character

# To print "n"
print("Last Character of this String:",str[5])   # print second character
print("Last Character of this String:",str[-1])  # print second character

# To print "thon"
print("Last 4 Characters of this String:",str[2:6]) # Print Character starting from 3rd to 5th
print("Last 4 Characters of this String:",str[-4:])

# To print "thon"
print("Last 4 Characters of this String:",str[2:]) # Print String starting from 2nd position
print("Last 4 Characters of this String:",str[-4:])

# To print String 2 times
print(str*2)

# To print concatenated string
print("This is a "+ str + " Program")

# To print string in Reverse order
print("Reversed String:",str[::-1])

# To print after every 2 step string
print("Character after every 2 steps of this String:",str[::2])

# Use len() method to print length of String
print(f"Length of String: {len(str)}")


# Use lower() method to print lowercase of String
print(f"Lowercase of String: {str.lower()}")

# Use upper() method to print Uppercase of String
print(f"Uppercase of String: {str.upper()}")

# Use title() method to make Uppercase of every word of string
name = "tafhim bin nasir"
print(f"My name is {name.title()}")

# Use count() method to count how many time a specific character is used in string
print(f"'t' is used in Python {str.count('t')} times")




