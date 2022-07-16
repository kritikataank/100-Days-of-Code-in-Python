print("Welcome to the love calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

n1= name1.lower()
n2= name2.lower()

first = str(n1.count("t") + n1.count("r") + n1.count("u") + n1.count("e") + n2.count("t") + n2.count("r") + n2.count("u") + n2.count("e"))
second = str(n1.count("l") + n1.count("o") + n1.count("v") + n1.count("e") + n2.count("l") + n2.count("o") + n2.count("v") + n2.count("e"))

x= int(first + second) 

if x <10 or x> 90:
    print(f"Your score is {x}, you go together like coke and mentos.")
elif x > 40 and x <50:
    print(f"Your score is {x}, you are alright together.")
else:
    print(f"Your score is {x}")