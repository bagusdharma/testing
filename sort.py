animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
  print animal


# Write a for-loop that iterates over start_list and .append()s each number squared (x ** 2) to square_list.

# Then sort square_list!

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()

print square_list

# Key Value print
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number