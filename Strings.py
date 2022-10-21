#Getting the first character of the string.
txt = 'Hello World'
x = txt[0]

#Getting the characters from index 2 to index 4 (llo).
txt = 'Hello World'
x = txt[2:5]

#Returning the string without any whitespace at the beginning or the end.
txt = 'Hello World'
x = txt.strip()

#Converting the value of txt to upper case.
txt = 'Hello World'
x = txt.upper()

#Converting the value of txt to lower case.
txt = 'Hello World'
x = txt.lower()

#Replacing the character H with a J.
txt = 'Hello World'
x = txt.replace('H', 'J')

#Inserting the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
