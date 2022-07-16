print("Welcome to pizza deliveries!")
size = input("What size pizza do you want? S, M or L \n")
pepperoni = input("Do you want pepperoni? Y or N \n")
cheese = input("Do you want cheese? Y or N \n")
bill = 0

if size == "S":
    bill += 15
    #print(f"Small size is for {bill}")
    if pepperoni == "Y":
        bill += 2
        #print(f"Small size + pepperoni is for {bill}")
elif size == "M":
    bill += 20
    #print(f"Medium size is for {bill}")
    if pepperoni == "Y":
        bill += 3
        #print(f"Medium size + pepperoni is for {bill}")
else:
    bill += 25
    #print(f"Large size is for {bill}")
    if pepperoni == "Y":
        bill += 3
        #print(f"Large size + pepperoni is for {bill}")

if cheese == "Y":
    bill += 1
    #print(f"Your total bill is {bill}")
#else:
    #print(f"Your total bill is {bill}")
print(f"Your final bill is {bill}")