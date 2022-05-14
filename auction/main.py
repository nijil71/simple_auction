from click import clear
from art import logo
print(logo)

        
def find_highestbidder(bidding_record):
    highest_bid=0
    winner=""
    for i in bidding_record:
        bid_amount=bidding_record[i]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=i
    print(f"the winner is {winner},the bidding amount is {highest_bid}")

istrue=True
while istrue:
    bidders={}
    name=input("enter the name: \n")
    bid=int(input("enter the bidding amount: \n"))
    
    bidders[name]=bid
    another=input("Do u have another bidder,type yes or no\n")
    
    clear()
    
    if another=="no":
        istrue=False
        find_highestbidder(bidders)

