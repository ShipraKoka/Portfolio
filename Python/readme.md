###Card Game

I was assigned to create a text-based game applying what I have learned so far in Python. I decided to create a simple card game in Python 3.

#####Game Objective

The user is dealt a hand of 4 cards from a 52 card deck, one for each suit.
 
Example:	

	+2 of Diamonds
	+7 of Hearts
	+Queen of Spades
	+Ace of Clubs
	
The object of the game is to acquire a hand where all 4 cards are of the same rank.

#####How to Play

The user must trade in one card that he/she does not need and will be randomly dealt another. This trade-off will continue until all 4 cards match.

#####Lessons Learned

I created a dictionary of 4 keys to store the deck of cards. Each key corresponds to a suit and has 13 values, one for each rank. I had to access the data in the dictionary and attempt to retrieve a random value. Mapping each key to multiple values made this a lot more challenging than if I had defined key:value pairs with a one-to-one relationship. I practiced iterating with for loops and using the built-in map() function. This project really helped me to understand the differences between managing data in a dictionary and managing data in a list. It also taught me to be aware of the data type of each object within a program, and its features.
