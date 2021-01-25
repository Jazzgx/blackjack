"""
This is a program that will play Blackjack with the user!
"""

from random import randint  #This is for the 'card dealing'.

def draw_one_card():    #Returns a random number from 1 to 10 with equal chance.
    return randint(1,10)

def add_up_cards(x, y): #Though not necessary, it looks cleaner if I use a function for adding.
    return x + y

def players_turn(): #This huge amount of code needs to be repeated in several places. As such, this saves space.
    global hit_or_stand #These need to be accessed and altered by the function.
    global total_cards
    global new_draw

    while hit_or_stand == 'h' and total_cards < 21: #The player shouldn't hit if they have 21 cards, even if they want to.
        new_draw = draw_one_card()  #Assigns a random 'card' with value 1 to 10.
        total_cards = add_up_cards(new_draw, total_cards)   #Updates total_cards points by adding the latest draw.
        print("You have decided to hit!")
        print(f"You have drawn a {new_draw}. Your total is {total_cards}.")
        if total_cards < 21:
            hit_or_stand = input("Do you want to hit or stand? [h/s]: ")
        else:   #Nested loop for simplicity. Either the player can keep playing, or they can't (else).
            if total_cards > 21:
                print(f"You have gone bust with {total_cards}. Better luck next time!")
                exit()
            if total_cards == 21:
                print("Your cards total has reached 21! You must stand.")
                dealers_turn() #The dealer begins her turn whenever the player stands.
            if hit_or_stand == 's':
                print(f"You have decided to stand with {total_cards}!")
                dealers_turn()

def dealers_turn(): #This huge amount of code needs to be repeated in several places. As such, this saves space.
    global dealer_new_draw  #These need to be accessed and altered by the function.
    global dealer_total_cards

    print(f"The dealer reveals her hidden card: {dealer_hidden_card}. The dealer's total is {dealer_total_cards}.")
    while dealer_total_cards < 17:  #The dealer will continue to draw new cards until she has over 16.
        dealer_new_draw = draw_one_card()
        dealer_total_cards = add_up_cards(dealer_new_draw, dealer_total_cards)
        print(f"The dealer draws {dealer_new_draw}. Her new total is {dealer_total_cards}.")
    else:
        if dealer_total_cards <= 21:    #If the dealer has 21 or less, she has not gone bust...
            print(f"The dealer stands with {dealer_total_cards}.")
            if total_cards > dealer_total_cards:    #...therefore neither player has gone bust, so I need to compare.
                print("Congratulations, you've won!")
                exit()
            else:
                print("You've lost! Better luck next time!")
                exit()    #This else encapsulates if total_cards <= dealer_total_cards
        else:
            print(f"The dealer has gone bust with {dealer_total_cards}. You win!")  #Win by default. If the player had gone bust, dealer would not get a turn at all.
            exit()

#The variables are declared after the functions, since they all rely on functions.
new_draw = draw_one_card()
first_draw = draw_one_card()
total_cards = add_up_cards(first_draw, new_draw)
dealer_new_draw = draw_one_card()
dealer_hidden_card = draw_one_card()
dealer_total_cards = add_up_cards(dealer_new_draw, dealer_hidden_card)

print("Welcome to Jazz's Blackjack!")

start = input("Do you want to start a new game? Input y for yes, any other input to exit: ") #It's much simpler if the user is just asked to input 'y' to play.
while not start:
    print("You have left the space empty. Please try again.")
    start = input("Do you want to start a new game? y if yes: ") #Leaving the space blank is probably an accident.
else:
    if start.upper() != 'Y': #They may input Y instead of y, which should still work.
        print("You did not input y. The program will now terminate.")
        exit()
    else:
        print("You have input y. Let's begin the game!")

print(f'You have drawn {new_draw} and {first_draw}. Your total is {total_cards}.')
print(f'The dealer has drawn {dealer_new_draw} as well as a hidden card.') #Technically, these were all 'drawn' when I declared the variables.

hit_or_stand = input("Do you want to hit or stand? [h/s]: ")
while not hit_or_stand:
    print("You have left the space empty. Please try again.")
    hit_or_stand = input("Do you want to hit or stand? [h/s]: ")
if hit_or_stand == 'h':
    players_turn()  #The players_turn function executes as seen above.
if hit_or_stand == 's':
    print(f"You have decided to stand with {total_cards}!")
    dealers_turn() #The dealers_turn function executes as seen above.
else:
    print("You have input an invalid letter. Please try again, or input another invalid letter to terminate the program.")
    hit_or_stand = input("Do you want to hit or stand? [h/s]: ")
    if hit_or_stand == 'h':
        players_turn()
    if hit_or_stand == 's':
        print(f"You have decided to stand with {total_cards}!")
        dealers_turn()
    else:
        print("You have failed to input a valid letter. The program will now terminate.")
        exit()
