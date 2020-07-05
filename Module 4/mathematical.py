# Create two variables (you pick the name) that have an integer value of 25,000,000 but one uses underscores as a
# thousand separator and the other doesn't.

var_int = 25000000
varr_int = 25_000_000

# Print out each variable using an f string with the following format "<Var Name>: <Var Value>" where <Var Name> is
# replaced with the variable name you selected and <Var Value> is it's variable.

print(f'var_int: {var_int}')
print(f'varr_int: {varr_int}')

# Create a variable (you pick the name) that has a float value of 175000.0 using the exponential (e) notation.
# Print the value to the terminal.

floating = 1.75e5
print(floating)

# Finally, prompt the user to enter a base and then an exponent.  Print out to the user the following:
# <base> to the power of <exponent> = <value>

base = float(input("Enter a base"))
exponent = float(input("Enter a exponent"))
value = base**exponent
print(f'{base} to the power of {exponent} = {value}')


