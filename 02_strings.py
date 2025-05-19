multiline_string = """This is a multiline string
It can span multiple lines
And it is useful for documentation or long text blocks."""
print(multiline_string)

# Strings formatting
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)

# str.format() method
formatted_string = 'The area of circle with a radius {} is {:.2f}.'.format(radius, area)
print(formatted_string)

# string interpolation (f-strings)
formatted_string = f'The area of circle with a radius {radius} is {area:.2f}.'
print(formatted_string)

# secuence of characters
language = "Python"
a, b, c, d, e , f = language
print(a, b, c, d, e, f)

# negative index
print(language[-1]) # last character
print(language[-2]) # second to last character

# slicing strings
print(language[0:2]) # first two characters

# reversing string 
print(language[::-1]) # reverse string

# Capitalize string
print(language.capitalize()) # Capitalize first character
print(language.upper()) # Capitalize all characters

# count characters
print(language.count('o')) # count 'o' characters

# check if string ends with a substring
print(language.endswith('on')) # check if string ends with 'on'

# expand tabs
print("Hello\tWorld".expandtabs(4)) # expand tabs to 4 spaces

#find substring
print(language.find('on')) # find 'on' substring
print(language.index('on')) # find 'on' substring

# isalnum method
print(language.isalnum()) # check if string is alphanumeric
print(language.isalpha()) # check if string is alphabetic
print(language.isdigit()) # check if string is digit

# isIdentifier method
print(language.isidentifier()) # check if string is identifier, in this case True

# join method
print(" ".join(language)) # join string with space

print("-".join(language)) # join string with '-'

# strip method
print("   Hello World   ".strip()) # remove spaces from both sides

# replace method
print(language.replace('o', 'O')) # replace 'o' with 'O'

#title method
print("un verano sin ti".title()) # capitalize first character of each word

# swapcase method
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

#end