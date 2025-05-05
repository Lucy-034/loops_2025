# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]

# Challenge:
# Use a for loop to print each fruit on a new line.
for fruit in fruits:
    print(f"{fruit}")
    break

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]

# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
for subject in subjects:
    if subject == "Math":
        print("Subject 0: Math")
    elif subject == "Science":
        print("Subject 1: Science")
    elif subject == "History":
        print("Subject 2: History")
    elif subject == "Art":
        print("Subject 3: Art")
    else:
        print("There is no subject!")

# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.
for number in numbers:
    print(number + numbers)