from random import randint

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pyssword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many numbers would you like?\n"))
nr_letters = 4
nr_symbols = 4
nr_numbers = 4
password = ""

for character in range(1, nr_letters + 1):
    letter = letters[randint(1, (len(letters) - 1))]
    password = password + letter

for character in range(1, nr_numbers + 1):
    number = numbers[randint(1, (len(numbers) - 1))]
    password = password + number

for character in range(1, nr_symbols + 1):
    symbol = symbols[randint(1, (len(symbols) - 1))]
    password = password + symbol

print(f"Your new password: {password}")
