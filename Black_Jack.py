import random

def dealcard():
    """Return a Random card"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, comp_score):
    if u_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Lose, opponent has BlackJack"
    elif u_score == 0:
        return "Win With a BlackJack"
    elif u_score >21:
        return "You went Over, You Lose"
    elif comp_score > 21:
        return "Opponent Went Over, You Win"
    elif u_score > comp_score:
        return "You Win"
    else:
        return "You Lose"

def play_game():
    user_cards = []
    user_score = -1
    computer_cards = []
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(dealcard())
        computer_cards.append(dealcard())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}, current Score: {user_score}")
        print(f"Computer's First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score ==0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get a new card or type 'n' to pass")
            if user_choice == 'y':
                user_cards.append(dealcard())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealcard())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Deck is: {user_cards}, Final Score: {user_score}")
    print(f"Computer Final Deck is: {computer_cards}, Final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of ClackJack? Type 'y' or 'n': ") == "y":
    play_game()
