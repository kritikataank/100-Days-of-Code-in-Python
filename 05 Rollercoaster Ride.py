print("Welcome to the Rollercoster!")
height= int(input("Enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the Rollercoster.")
    
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets $5")
        bill = 5
    elif age <= 18:
        print("Youth tickets $7")
        bill = 7
    elif age >=45 and age <= 55:
        print("Your tickets are free!")
    else:
        print("Adult tickets $12")
        bill = 12

    photo = input("Do you want a photo to be taken? Y or N. ")
    if photo == "Y":
        bill += 3
        print(f"Your total bill is {bill}")
    else:
        print(f"Your total bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
