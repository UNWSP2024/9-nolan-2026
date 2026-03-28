# By Nolan Nelsen
# Written on 3/27/2026
# Random Number File Writer

# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random

def write_random_numbers():
    amount = int(input("How many random numbers would you like to generate? The max number is 1000. "))

    if amount < 1 or amount > 1000:
        print("Please enter a number between 1 and 1000.")
        return

    with open("random_numbers.txt", "w") as file:
        for i in range(amount):
            num = random.randint(1, 500)
            file.write(str(num) + "\n")

    print(f"{amount} random numbers have been written to random_numbers.txt")


if __name__ == '__main__':
    write_random_numbers()
