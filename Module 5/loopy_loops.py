# Create a tuple named pokemon that holds the strings 'picachu', 'charmander', and 'bulbasaur'.
# pikachu != picachu
pokemon = ('picachu', 'charmander', 'bulbasaur')
print(pokemon)

# Using index notation, print() the string that located at index 1 in pokemon
print(pokemon[1])

# Unpack the values of pokemon into the following three new variables with names starter1, starter2, starter3.
starter1 = pokemon[0]
starter2 = pokemon[1]
starter3 = pokemon[2]
print(starter1, starter2, starter3)

# Create a tuple using the tuple() built-in, that contains the letters of your name.
name = ('d', 'i', 'a', 'n', 'e')
print(name)

# Check whether the character i is in your tuple representation of your name.
if 'i' in name:
    print(True)
else:
    print(False)

# Write a for loop that prints out the integers 2 through 10, each on a new line, by using the range() function.
for i in range(2, 11):
    print(i)

# Use a while loop that prints out the integers 2 through 10.
i = 2
while i <= 10:
    print(i)
    i += 1

# Write a for loop that iterates over the string 'This is a simple string' and prints each character.
string_name = 'This is a simple string'
for l in string_name:
    print(l)

# Using a nested for loop, iterate over the following set ('this', 'is', 'a', 'simple', 'set') and print each word,
# three times.
string_names = ['this', 'is', 'a', 'simple', 'set']
for x in string_names:
    print(x*3)