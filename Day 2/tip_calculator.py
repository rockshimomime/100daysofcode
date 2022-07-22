print("Welcome to the tip calculator.")

total_bill = int(input("What was the total bill?\n"))
number_people = int(input("How many people to split the bill?\n"))
percentage = int(input("What percentage tip would you like to give?"
                       " (e.g. 10, 12 or 15)\n"))
tip = total_bill * percentage / 100
total_per_person = (total_bill + tip) / number_people

print(f"Each person should pay: ${total_per_person:.2f}")
