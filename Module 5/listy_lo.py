

# Create a list named food with two elements 'rice' and 'beans'.
food = ['rice', 'beans']
for i in food:
    print(i)

# Append the string 'broccoli' to food using .append().
food.append('broccoli')
print(food)

# Add the strings 'bread' and 'pizza' to food using .extend().
carbs = ['bread', 'pizza']
food.extend(carbs)
print(food)

# Print the first two items in the food list using print() and slicing notation.
print(food[0])
print(food[1])

# Print the last item in food using print() and index notation.
print(food[4])

# Create a list called breakfast from the string "eggs,fruit,orange juice" using the split() method.
breakfast = 'eggs, fruit, orange juice'
breakfast = breakfast.split(',')
print(breakfast)

# Verify that breakfast has 3 elements using the len built-in.
print(len(breakfast))

# prompts the user for a floating-point value until they enter stop. Store their entries in a list, and then find the
# average, min, and max of their entries and print them those values.
q = None
number_list = []
while q != 'stop':
    if q is not None and q.isdigit():
        number_list.append(int(q))
    q = input('Enter your numbers, until you type stop')
s = sum(number_list)
l = len(number_list)
average = s / l
print(f'The {number_list} sum is {s}, with a length of {l} = {average}')


