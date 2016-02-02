import random
import time
global hand
global suit

hand = []
suit = []

deck = dict(hearts=('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'),
            spades=('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'),
            diamonds=('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'),
            clubs=('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'))

def main():
    begin()
    dealHand()
    checkHand()
    trade()

def begin():
    global hand
    print("Welcome!\n")
    print("You will be dealt 4 cards from a 52 card deck.")
    print("The object of the game is to have the same card for each suit.")
    print("For example, all '4s' or all Kings.")
    print("You can only have 4 cards at any given time.")
    start = input("Would you like to start the game? y/n ")
    if start == "y":
        print("")
        dealHand()
        checkHand()
    elif start == "n":
        print("\nGoodbye!")

def dealHand():
    global hand
    readHand = []
    for key, val in deck.items():
        randCards = (key, str(random.choice(val))) #deal 4 random cards from deck
        hand.append(randCards)
        temp = ": ".join(map(str, randCards))
        readHand.append(temp) #make cards more presentable
    print('\n'.join(readHand))

def checkHand():
    global hand
    global suit
    cardNum = [x[1] for x in hand] #get card numbers from each card in hand
    match = all(map(lambda x: x == cardNum[0], cardNum)) #check to see if all card numbers match
    if match == True:
        print("")
        print("Congratulations! You have a complete set of '{}s'!".format(cardNum[0]))
        exit()
    elif match == False:
        print("")
        suit = input("Enter the suit of the card you want to trade in: ")
    trade()

def trade():
    global suit
    readHand = []
    throw = [item for item in hand if suit in item]
    hand.remove(throw[0]) #get rid of card traded in
    time.sleep(1)

    for key, val in deck.items():
        if key == suit:
            newCard = (key, str(random.choice(val))) #deal 1 new random card from the same suit
            hand.append(newCard)
    for x in hand:
        temp = x
        temp2 = ": ".join(map(str, temp))
        readHand.append(temp2)
    print("")
    print("Your new hand is:\n")
    print('\n'.join(readHand))
    checkHand()


if __name__ == "__main__": main()
