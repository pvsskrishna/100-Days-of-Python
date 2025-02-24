from art import hammer

def find_highest_bidder(bidding_dictionary):


    max_bid = 0
    name_of_bidder = ""

    for bid in bidding_dictionary:

        if bidders[bid] > max_bid:
            max_bid = bidders[bid]
            name_of_bidder = bid
    # or we can use max function to get the highest value from dictionary
    # max_bid = max(bidding_dictionary,key = bidding_dictionary.get)

    print(f"winner is {name_of_bidder} with bidding price of {max_bid} ")

bidders = {}
people = True

while people:
    print(hammer)

    bidder_name = input("what is your name: ")
    price = int(input("what is your bid: $"))

    bidders[bidder_name] = price

    start = input("Is there another bidder?, say Yes or No: ").lower()
    print("\n" * 100)

    if start == "no":
        people = False
find_highest_bidder(bidders)
print(bidders)







