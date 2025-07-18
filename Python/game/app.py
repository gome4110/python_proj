# import random

# print("Rock Paper Sciccors")


# ai = ["r", "p", "s"]
# ai_play = random.choice(ai)

# user_play = input("Rock(r) Paper(p) Sciccor(s): ")

# if ai_play == "r" and user_play == "s":
#     print(f"{ai_play} - {user_play} Ai win this round")
# elif ai_play == "p" and user_play == "s":
#     print(f"{ai_play} - {user_play} You win this round")
# elif ai_play == "s" and user_play == "p":
#     print(f"{ai_play} - {user_play} Ai win this round")
# elif ai_play == "r" and user_play == "p":
#     print(f"{ai_play} - {user_play} You win this round")
# elif ai_play == "p" and user_play == "r":
#     print(f"{ai_play} - {user_play} Ai win this round")
# elif ai_play == "s" and user_play == "r":
#     print(f"{ai_play} - {user_play} You win this round")
# else:
#     print(f"{ai_play} - {user_play} Draw")
# ---------------------


# import random

# print("Coin Fliping Game")

# while True:
#     user_guess = input("Enter your guess (head/tails): ")

#     head_tails = ["head", "tails"]
#     coin_result = random.choice(head_tails)

#     print(f"The coin shows: {coin_result}")
#     if coin_result == user_guess:

#         print("You guess correctly! You Win")
#     else:
#         print("Sorry, wrong guess: Tray again!")

#     user_exit = input("Play again? (y/n)")

#     if user_exit.lower() == "n":
#         print("Thank for playing!")
#         break
# -------------------------------


# another way
# import random


# print("Coin Fliping Game")

# while True:
#     user_guess = input("Enter your guess (head/tails): ")

#     if user_guess != "head" and user_guess != "tails":
#         print("Please enter 'head' or 'tails'")
#         continue  # it goes back to the start, if got the wrong input

#     head_tails = ["head", "tails"]
#     flip_coin = random.choice(head_tails)

#     print(f"The coin shows: {flip_coin}")

#     if user_guess == flip_coin:
#         print("You guess correctly! You Win")
#     else:
#         print("Sorry, wrong guess: Tray again!")

#     y_n = input("Play again? y/n ")
#     if not y_n.startswith("y"):
#         print("Thank for playing!")
#         break
# -------------------------------


# Guessing game
# import random


# print("Welcome To Guessing Words Game 🎮")

# scramble_words = {
#     "elppa": "apple",
#     "odg": "dog",
#     "rac": "car",
#     "teehclpa": "cheetah",
#     "caek": "cake",
#     "moosr": "rooms",
#     "ilpecna": "pencil",
#     "trwae": "water",
#     "koob": "book",
#     "olhel": "hello",
# }

# while True:
#     rand_words_key = random.choice(list(scramble_words.keys()))
#     correct_answer = scramble_words[rand_words_key]

#     print(f"Scrambled word: {rand_words_key}")

#     user_answer = input("What's the word? - ").lower()
#     if user_answer == correct_answer:
#         print("Correct! You Win!")
#     else:
#         print(f"Sorry, the word was: {correct_answer}")

#     play_again = input("Would you like to play again? (y/n): ").lower()
#     if not play_again.startswith("y"):
#         print("Exiting.....")
#         break

# Another way
# import random

# print("Welcome To Guessing Words Game 🎮")

# words = ["apple", "orange", "banana", "grape", "lime"]


# while True:
#     origional_words = random.choice(words)

#     letters = list(origional_words)
#     random.shuffle(letters)
#     scramble_words = "".join(letters)
#     print(f"Scrambled word: {scramble_words}")
#     user_answer = input("What's the word? - ").lower()
#     if user_answer == origional_words:
#         print("Correct! You Win!")
#     else:
#         print(f"Sorry, the word was: {origional_words}")

#     play_again = input("Would you like to play again? (y/n): ").lower()
#     if not play_again.startswith("y"):
#         print("Exiting.....")
#         break
# -------------------------------------


# Guessing Number
# import random

# print("Welcome To The Number Guessing Game 🎮")
# print("Guess The Number Between 1 and 100. You only have 10 attempts.")

# rand_num = random.randint(1, 100)
# total_attempt = 10
# attempt = 0

# while attempt < total_attempt:
#     attempt += 1

#     user_guess = int(input(f"Attempt {attempt} / {total_attempt}. Enter your guess: "))

#     if user_guess > rand_num:
#         print("Too high! Try a lower number.")
#     elif user_guess < rand_num:
#         print("Too low! Try a higher number.")
#     else:
#         print(f"Congratulation! You guessed it in {attempt} attempts!")
#         break
# else:
#     print(f"You ran out of attempts! The number was: {rand_num}")

# another way
# import random

# print(" Welcome to the Number Guessing Game!")
# print("Guess the number between 1 and 100. You have 10 attempts.")

# number = random.randint(1, 100)
# attempts_left = 10

# while attempts_left > 0:
#     print(f"\nAttempts left: {attempts_left}")
#     guess_num = int(input("Enter your guess: "))
#     attempts_left -= 1

#     if guess_num == number:
#         print(f"You have Guess the number {number} in {10 - attempts_left}")
#         break
#     elif guess_num < number:
#         print("Too low. Try higher number.")
#     else:
#         print("Too high. Try lower number")

# if attempts_left == 0:
#     print(f"Out of attempts. The correct number is {number}")
# --------------------------------------------------------------------


# Related Word Game
# import random
# import time

# word_associations = {
#     "dog": ["pet", "bark", "puppy", "bone", "tail"],
#     "cat": ["meow", "pet", "kitten", "whiskers", "fur"],
#     "car": ["drive", "engine", "wheel", "vehicle", "road"],
#     "school": ["teacher", "student", "class", "homework", "learning"],
#     "apple": ["fruit", "red", "sweet", "tree", "juice"],
#     "sun": ["hot", "light", "day", "bright", "sky"],
#     "computer": ["keyboard", "screen", "mouse", "code", "internet"],
#     "music": ["song", "melody", "sound", "band", "instrument"],
#     "phone": ["call", "text", "mobile", "ring", "app"],
#     "water": ["drink", "wet", "river", "ocean", "clear"],
# }

# print("Word Association Game")

# score = 0
# rounds = 0

# while True:
#     ran_word = random.choice(list(word_associations.keys()))
#     print(f"Prompt word: {ran_word}")

#     start_time = time.time()

#     user_answer = input("Quick! Type a word related to this prompt!: ")

#     end_time = time.time()

#     respond_time = end_time - start_time
#     print(f"Response time: {respond_time:.1f}")

#     if user_answer.lower() in word_associations[ran_word]:
#         points = max(1, 5 - int(respond_time))
#         score += points
#         print(f"Good associationi! +{points} (answered in {respond_time:.1f}s)")
#     else:

#         print(
#             f"Not a common association. Related words included: {', '.join(word_associations[ran_word])}"
#         )
#     rounds += 1
#     print(f"Score: {score}/{rounds * 5} possible points")

#     play_again = input("Play again? (y/n): ")
#     if not play_again.startswith("y"):
#         print(f"Final Score: {score}. Thanks for playing!")
#         break
# -------------------------------------------------------


# Memory Sequence Game
# import random
# import time
# import os


# def clear_screen():
#     """Clear the terminal screen"""
#     os.system("cls" if os.name == "nt" else "clear")


# print("Memory Sequence Game")
# print("Remember the sequence and type it back!")
# print("Rules of the game:")
# print("- Watch as number appear one by one")
# print("- After the sequence is shown, type it back in order")
# print("- Each round adds one more number to remember")
# print("- How far can you go?\n")

# input("Press Enter to start...")

# sequence = []
# current_round = 1
# game_over = False

# while not game_over:
#     sequence.append(random.randint(1, 9))

#     clear_screen()
#     print(f"\n=== Round {current_round} ===")
#     print(f"Remember this sequence of {len(sequence)} numbers: ")

#     for num in sequence:
#         time.sleep(0.7)
#         print(f"\n{num}")
#         time.sleep(0.7)
#         clear_screen()

#     print("\nNow repeat the sequence by typing each number, separated by spaces: ")
#     player_answer = input(" Respond Here: ")

#     try:
#         player_sequence = [int(num) for num in player_answer.split()]
#     except ValueError:
#         print("Please enter numbers only!")
#         game_over = True
#         continue

#     if player_sequence == sequence:
#         print(f"Congrat! You remembered all these {len(sequence)} numbers!")
#         current_round += 1
#         time.sleep(2)
#     else:
#         print(f"Game Over! You remembered all {current_round -1} numbers!")
#         print(f"The correct sequence was : {"".join(str(num) for num in sequence)}")
#         game_over = True

#     if game_over:
#         play_again = input("Play again? (y/n): ").lower()
#         if play_again.startswith("y"):
#             sequence = []
#             current_round = 1
#             game_over = False
#         else:
#             print("Thanks for playing!")

# -----------------------------------------------------


# R/P/S Game
# import random
# import time


# def get_user_choice():
#     while True:
#         print("\nMake your choice: ")
#         print("1. Rock")
#         print("2. Paper")
#         print("3. Scissors")

#         try:
#             choice = int(input("Enter your choice(1-3): "))
#             if 1 <= choice <= 3:
#                 return choice
#             else:
#                 print("Please enter a number between 1 and 3")
#         except ValueError:
#             print("Please enter a valid  number.")


# def get_computer_choice():
#     return random.randint(1, 3)


# def convert_choice_to_text(choice):
#     option = {1: "Rock", 2: "Paper", 3: "Scissors"}
#     return option[choice]


# def determine_winner(user_choice, comp_choice):
#     # tie
#     if user_choice == comp_choice:
#         return "tie"
#     # user wins cases:
#     elif (
#         (user_choice == 1 and comp_choice == 3)
#         or (user_choice == 3 and comp_choice == 2)
#         or (user_choice == 2 and comp_choice == 1)
#     ):
#         return "user"
#     else:
#         return "computer"


# def display_welcome():
#     print("\n========================================")
#     print("\nRock Paper Scissors")
#     print("\nRules: ")
#     print("- Rock > Scissors")
#     print("- Scissors > Paper")
#     print("- Paper > Rocks")
#     print("First to win 3 rounds is the champion!")
#     print("\n-----------------------------------------")


# def display_round_result(user_choice, comp_choice, result):
#     user_text = convert_choice_to_text(user_choice)
#     computer_text = convert_choice_to_text(comp_choice)

#     print(f"\nYou chose: {user_text}")
#     print("Computer is choosing")
#     for i in range(3):
#         print(".")
#         time.sleep(0.5)
#     print(f"Computer chose: {computer_text}")

#     if result == "tie":
#         print("It's a tie!")
#     elif result == "user":
#         print("You win this rounds")
#     else:
#         print("Computer wins this round")


# def play_game():
#     """Main game function"""
#     display_welcome()
#     user_score = 0
#     computer_score = 0
#     target_score = 3
#     round_num = 1

#     while user_score < target_score and computer_score < target_score:
#         print(f"\n=== Round {round_num} ===")
#         print(f"Score: You {user_score} - {computer_score} Computer")

#         user_choice = get_user_choice()
#         comp_choice = get_computer_choice()

#         result = determine_winner(user_choice, comp_choice)

#         display_round_result(user_choice, comp_choice, result)
#         if result == "user":
#             user_score += 1
#         elif result == "computer":
#             computer_score += 1

#         round_num += 1

#     print("\n=== Game Over ===")
#     print(f"Final Score: You {user_score} - {computer_score} Computer")

#     if user_score > computer_score:
#         print("Congrats! you are the champion")
#     else:
#         print("Better luck next time. Computer is a winner the champion!")

#     play_again = input("\nDo you want to play again? (y/n): ")
#     if play_again.startswith("y"):
#         play_game()
#     else:
#         print("Good Bye")


# play_game()
