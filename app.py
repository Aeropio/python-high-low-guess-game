from game_data import data
import random
from art import logo, vs
from replit import clear

# get random account
def get_random_account():
  return random.choice(data)

# printable format
def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"
  
# get inputs from user and compare
def check_answer(user_guess, num_a_followers, num_b_followers):
  if num_a_followers > num_b_followers:
    return user_guess == "a"
  else:
    return user_guess == "b"

def game():
  print(logo)
  account_a =  get_random_account()
  account_b =  get_random_account()
  play_game = True
  score = 0
  while play_game:
    clear()
    account_a = account_b
    account_b = get_random_account()
    # ensure both a & b account r diff
    while(account_a == account_b):
      account_b = get_random_account()
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if check_answer(guess, account_a["follower_count"], account_b["follower_count"]):
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      play_game = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
