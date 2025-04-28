intro = "My name is"
firstName = "Arpon"
lastName = "Sarker"
print(f"{intro} {firstName} {lastName}")

addString = intro + " " + firstName + " " + lastName
print(addString)
print("Lower Case: ", addString.lower())
print("Upper Case: ",addString.upper())
print("Capitalize: ", addString.capitalize())
print("Delete at the last: ", addString.rstrip("Sarker"))
print("Convert it into list: ", addString.rsplit(" "))
print("Make the string as a Title: ", addString.title()) #All words are capitalized
print("Replace: ", addString.replace("Sarker", "The GOAT"))
print("Add in the end: ", addString, end = " The GOAT\n")
print("Length of the string: ", len(addString))
print("Check if finds: (Index)", addString.find("Arpon")) #Return the index of first letter
print("Check if ends with: ", addString.endswith("Sarker"))
print("Check if ends with: ", addString.endswith("Arpon")) #Return True or False
print("Check if starts with: ", addString.startswith("My"))
print("Check if starts with: ", addString.startswith("Arpon")) #Return True or False
print(addString[:]) #This will return All
print(addString[1:8]) #From the starting index to the last index
print(addString[-20:23]) # Negative means len(addString) + (negative value)
