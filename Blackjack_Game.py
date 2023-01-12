#Rodrigo Banos Hernandez

#Blackjack Game

import os 
import random
os.system("clear")

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

#Functions---------------------------------------------------------------------------------------------

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and return the calculated score"""
    #Finds a blackjack in the hand
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    #replaces the Ace's value of 11 for 1 when the total score is over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)

def compare(user_score, computer_score):
    """Determines the winner or if it's a draw with the final score"""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

#Game Function Start-----------------------------------------------------------------------------------------

def black_jack():

    #Variables and lists:
    user_cards = []
    computer_cards = []
    user_should_deal = ""
    is_game_over = False

    print(logo)

    #Game stars here, we deal two cards:
    for c in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #Adding cards to the player's hand
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, your score {user_score}")
        print(f"CPU's first card: {computer_cards[0]}")
        #Game ends if there is a blackjack or the user_score is over 21:
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        #User can draw another card:
        else:
            user_should_deal = input("Do you want to draw another card? y/n: \n").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #Adding cards to the computer's hand
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"computer: {computer_cards}, cpu score: {computer_score}")
    print(f"{compare(user_score, computer_score)}")

#Game Function End-----------------------------------------------------------------------------------------

#Game loop:
while input("Do you want to play another Blackjack game?: y/n \n").lower() == "y":
    os.system("clear")
    black_jack()





