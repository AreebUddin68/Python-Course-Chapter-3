3# Strings

# String slicing

name = "Areeb"
nameshort = name[0:3] # start from index 0 all the way till 3 (excluding)
print(nameshort)

# Negative slicing
namelast = name[-2:] # start from index -2 all the way till end
print(namelast)

# Slicing with skip value
name_skip = name[1:5:2] # start from index 1 all the way till 5 (excluding) with a skip of 2
print(name_skip)

# Strings function
print(len(name)) # length of string
print(name.upper()) # convert to uppercase
print(name.lower()) # convert to lowercase
print(name.replace("Areeb", "Ali")) # replace substring
print(name.endswith("eeb"))
print(name.startswith("Ar"))
print(name.capitalize())

# Question 1
#a = input("Enter your name: ")
#print(f"Hello {a}, welcome to the world of Python!")

# Question 2
letter = '''Dear <|Name|>
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>", "Areeb").replace("<|Date|>", "15th August 2025"))

# Question 3
ar = "Areeb is a  boy"
print (ar.find(" "))

# Question 4
print(ar.replace("  ", " "))  

#Question 5
print("Dear Areeb,\n\tThis is python course is nice.\nThanks!")