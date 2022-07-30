import os
clear = lambda: os.system('cls')

auction = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}! Their bid was {highest_bid}")

while not bidding_finished:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    auction[name] = bid
    finished = input("Are there any other bidders? Yes or No ")
    if finished == "No":
        bidding_finished = True
        find_highest_bidder(auction)
    elif finished == "Yes":
        clear()
