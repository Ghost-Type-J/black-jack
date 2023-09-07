import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
numberofcards = len(cards)


def end_game():
    return

# Function specifies to clear screen and begin the blackjack game (note: the clear() function is imported from the replit module. Unsure of best alternative currently

def start_game():
    start = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if start == "y":
        clear()
        black_jack()

    else:
        end_game()

# Similar to start_game except with different text

def start_again():
    again = input(
        "\nDo you want to play another game of Blackjack?\n    Type 'y' or 'n': "
    ).lower()

    if again == "y":
        clear()
        black_jack()

    else:
        end_game()

# Function has three parameters, and creates a list of random cards for the number of specified draws. Also changes 11 to 1 if the total value of the list > 21. Returns a the current hand as a list 

def random_card_selector(whose_hand, how_many, score):
    for n in range(0, how_many):
        random_card = cards[random.randint(0, numberofcards - 1)]
        whose_hand.append(random_card)
        score = sum(whose_hand)
        if 11 in whose_hand and score > 21:
            pos = whose_hand.index(11)
            whose_hand[pos] = 1

    return whose_hand


def outcomes(u_score, o_score, u_hand, o_hand):
    print(
        f"\n    Your final hand: {u_hand}. Final score: {u_score}.\n    Opponent's final hand: {o_hand}. Final score: {o_score}"
    )
    if o_score > 21:
        print("You win!")
    elif u_score > o_score:
        print("You win!")
    elif u_score < o_score:
        print("You lose!")
    elif u_score == o_score:
        print("You draw!")

# Function defines the logic of the black jack game, also prompts the user to draw more cards or keep current hand

def black_jack():
    re_deal = True
    hand_size = 2
    your_hand = []
    computer_hand = []
    your_score = 0
    opponent_score = 0
    print(logo)
    while re_deal:

        random_card_selector(your_hand, hand_size, your_score)
        your_score = sum(your_hand)

        if opponent_score < 17:
            random_card_selector(computer_hand, hand_size, opponent_score)
            opponent_score = sum(computer_hand)

        print(
            f"\n    Your current hand: {your_hand}. Your score is: {your_score}. \n    The opponent's first card is: {computer_hand[0]}."
        )

        if your_score > 21:
            re_deal = False
        else:
            choice = input("\nPick another card? Type 'y' or 'n': ")
            if choice == "y":
                hand_size = 1
                re_deal = True

            if choice == "n":
                while opponent_score < 17:
                    random_card_selector(computer_hand, 1, opponent_score)
                    opponent_score = sum(computer_hand)
                re_deal = False

    if your_score > 21:
        print(
            f"\n    Your final hand: {your_hand}. Final score: {your_score}.\n    Opponent's final hand: {computer_hand}. Final score: {opponent_score}.\n      You lose! Your score is higher than 21."
        )
        start_again()
    else:
        outcomes(u_score=your_score,
                 o_score=opponent_score,
                 u_hand=your_hand,
                 o_hand=computer_hand)
        start_again()


start_game()
