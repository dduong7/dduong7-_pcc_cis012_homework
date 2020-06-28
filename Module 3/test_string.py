

# Print a string that uses double quotation marks inside the string.
print('Darth Vader, \"I am your father\"')

# Print a string that uses an apostrophe inside the string.
print('Han Solo\'s Millennium Falcon')

# Print a string that spans multiple lines, with white space preserved.
print('All wings reporting in \nRed 10 standing by \nRed 7 standing by \nRed 3 standing by \nRed 6 standing by ')

# Print a string that is coded on multiple lines but displays on a single line.
print('A long time ago in a galaxy far, far away'
      ' It is a period of civil wars in the galaxy. A brave alliance of underground freedom fighters'
      ' has challenged the tyranny and oppression of the awesome GALACTIC EMPIRE.')

# Create a string and print its length
test_string_length = 'The force is strong with this one'
print(len(test_string_length))

# Create two strings, concatenate them, and print the result
string_1 = 'X'
string_2 = '-Wing'
print(string_1 + string_2)

# Create two string and use concatenation to add a space in-between them and print the result
string_1 = 'Tie'
string_2 = 'Fighter'
print(string_1 + ' ' + string_2)

# Print the sub-string 'nerf' from the string 'nerf herder'
string_1 = 'nerf herder'
print(string_1[0:4])

# Convert the following strings to lower case:
print('Jalin'.lower())
print('Obi-Wan'.lower())
print('Darth Maul'.lower())
print('Rex'.lower())

# Convert the following strings to upper case:
print('Jalin'.upper())
print('Obi-Wan'.upper())
print('Rex'.upper())

# Remove whitespace from the following strings:
print(" Ezra Bridger is my apprentice! ".replace(" ", ""))

# Replace 'Han' with 'Ben', and 'shot' with 'stabbed' in the following string:
print("Han Solo shot first".replace("Han", "Ben").replace("shot", "stabbed"))

# Find the location of the string 'Night' within the following string.
# Then print out the start and end index of that string along with the actual substring:
start = "Dathomir is the home planet of the Night Sisters".find('Night')
end = start + len('Night')
print(str(start) + ':' + str(end), 'Night')

# Using formatted strings, create the following template and store it in a variable:
variable = "The {ship} can make the Kessel Run in less than {distance} parsecs"

# Using the variable from before and the .format method, insert the ship name "Millennium Falcon" and distance of 12
print(variable.format(ship='Millennium Falcon', distance='12'))

# Using an fstring and the same template above, insert the ship name "Ghost" and distance of 20
ship = 'Ghost'
distance = '20'
variable = f"The {ship} can make the Kessel Run in less than {distance} parsecs"
print(variable)
