from modules.art import logo, vs
from modules.gameData import data
import random
import os

clear = lambda: os.system('clear')

def format_data(account):
    """Format the account data into a printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    

# Display Art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # Generate random data.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    # Format the account data into printable format
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check user answer if correct.
    ## Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    ### Use if statement to check if user is correct.
    clear()
    print(logo)
    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Current score is {score}")
    else:
        game_should_continue = False
        print(f"sorry, that's wrong. Final score. {score}")  