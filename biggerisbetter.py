import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
value=[2,3,4,5,6,7,8,9,10,11,12,13,1]

re_value=dict(zip(ranks,value))

deck = [rank + ' of ' + suit for suit in suits for rank in ranks]


user_hand=[]
computer_hand=[]

random.shuffle(deck)



print("~"*150)

print("""Hello Guys!
      Welcome to The Card game - 'The Bigger the Better' 
      In this game a deck of cards is randomly shuffled and then you have to decide the number of cards you want to take
      ,depending upon that the same number of cards will be distributed to computer too. Then the values of card present 
      in each hand (user's and computer's) will be added and the one with larger value will win the game""")

print("~"*150)

choice=input("Would you like to see the deck?")
for dec in deck:
    if(choice=="yes" or choice=="y"):

        print(dec)



no_to_pop=int(input("How many cards do you want to draw? \n"))



if(no_to_pop<1 or no_to_pop>10):
    print("Please restart and put correct number between 1 to 10")


for i in range(no_to_pop):
    user_hand.append(deck.pop())
    computer_hand.append(deck.pop())

print("\n")
print("User Cards: ")
for card in user_hand:
    print(f" {card} ")
print("\n")
print("Computer Cards:")
for card in computer_hand:
    print(f" {card} ")




user_total=sum(re_value[card.split(' of ')[0]] for card in user_hand)
comp_total=sum(re_value[card.split(' of ')[0]] for card in computer_hand)


print("\n")
print("~"*150)
if user_total>comp_total:
    print("USER WINS")
elif user_total==comp_total:
    print("IT'S A DRAW")
else:
    print("COMPUTER WINS")
print("~"*150)