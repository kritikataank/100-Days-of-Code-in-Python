print("Welcome to the tip calculator")
bill = float(input("What is the total bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip = (bill*percent)/100

total = bill + tip

per_person = round(total/people,2)

print(f"Each person should pay {per_person} and total bill is {total}")