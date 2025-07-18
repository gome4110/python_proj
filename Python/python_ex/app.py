# 1
# print("Text Capitalizer")
#
# while True:
#     user_text = input("Enter some text: ")
#     print("\n1. UpperCase")
#     print("2. LowerCase")
#     print("3. TitleCase")
#     print("4. SentenceCase")
#     print("5. Exit")
#     user_input = input("Choose a format (1-5): ")
#
#     match user_input:
#         case "1":
#             print(user_text.upper())
#         case "2":
#             print(user_text.lower())
#         case "3":
#             print(user_text.title())
#         case "4":
#             print(user_text.capitalize())
#         case "5":
#             print("Exit...")
#             break


# print("TEXT CAPITALIZER")
# text = input("Enter some text: ")
# print("\n1. UpperCase")
# print("2. LowerCase")
# print("3. TitleCase")
# print("4. SentenceCase")
# user_input = input("Choose a format (1-5): ")

# if user_input == "1":
#     print(text.upper())
# elif user_input == "2":
#     print(text.lower())
# elif user_input == "3":
#     print(text.title())
# elif user_input == "4":
#     print(text.capitalize())


# 2
# print("Welcome To Character Type Checker")

# user_input = input("Enter a single character: ")

# # condition
# if user_input.isalpha():
#     print("This is a letter.")
# elif user_input.isdigit():
#     print("This is a number.")
# else:
#     print("This is special case.")


# 3
# print("Grade Calculator")

# while True:
#     user_score = input("Enter a test score (or 'done'): ")

#     if user_score == "done":
#         print("Goodbye")
#         break

#     try:
#         score = int(user_score)
#     except ValueError:
#         print("Invalid input. Please enter a number or 'done'.")
#         continue

#     print(f"Average Score: {user_score}")

#     if score >= 90:

#         print("Grade: A")
#     elif score >= 80:

#         print("Grade: B")
#     elif score >= 50:

#         print("Grade: C")
#     else:

#         print("Grade: D")


# ----------------

# print("GRADE CALCULATOR")

# scores = []

# while True:
#     score = input("Enter a test score (or 'done'): ")
#     if score.lower() == "done":
#         print("Goodbye")
#         break

#     scores.append(float(score))
#     average = sum(scores) / len(scores)
#     print(f"Average score: {average:.1f}")
#     if average >= 90:
#         print("Grade: A")
#     elif average >= 80:
#         print("Grade: B")
#     elif average >= 70:
#         print("Grade: C")
#     else:
#         print("Grade: D or F")

# -------------------

# 4
# from operator import le
# import random

# print("Word Scrambler")

# while True:
#     user_input = input("Enter a word to scramble or type 'done': ")

#     if user_input.lower() == "done":
#         print("Bye")
#         break

#     # User input: "another"
#     # 1: Convert it to a list of characters => ["a", "n", "o", "t", "h", "e", "r"]
#     # 2: Shuffle the list randomly using random.shuffle() ["o", "n", "a", "e", "h", "t", "r"]
#     # 3: Join the shuffled characters back into a string

#     letters = list(user_input)
#     random.shuffle(letters)
#     shuffel_word = "".join(letters)
#     print(f"Scrambled: {shuffel_word} ")

# ------------------------

# 5
# import random

# # music data
# music_data = {
#     "rock": [
#         "Bohemian Rhapsody – Queen",
#         "Hotel California – Eagles",
#         "Smells Like Teen Spirit – Nirvana",
#         "Stairway to Heaven – Led Zeppelin",
#         "Sweet Child O' Mine – Guns N' Roses",
#     ],
#     "pop": [
#         "Blinding Lights – The Weeknd",
#         "Levitating – Dua Lipa",
#         "Shake It Off – Taylor Swift",
#         "Uptown Funk – Bruno Mars",
#         "Sorry – Justin Bieber",
#     ],
#     "hip-hop": [
#         "Sicko Mode – Travis Scott",
#         "God's Plan – Drake",
#         "Lose Yourself – Eminem",
#         "HUMBLE. – Kendrick Lamar",
#         "Old Town Road – Lil Nas X",
#     ],


# print("Music Recommender App")

# while True:
#     user_input = input("What genre do you like? (Rock/ Pop/ Hip-Hop): ")

#     if user_input.lower() == "done":
#         print("Exiting.....")
#         break

#     if user_input.lower() == "rock":
#         print(f"Check out: {random.choice(music_data[user_input])}")
#     elif user_input.lower() == "pop":
#         print(f"Check out: {random.choice(music_data[user_input])}")
#     elif user_input.lower() == "hip-hop":
#         print(f"Check out: {random.choice(music_data[user_input])}")
#     else:
#         print("Sorry, that genre is not in our data.")

# -------------------

# another way
# print("Music Recommender")

# user_choice = input("What genre do you like? (rock / pop / hip-hop): ")

# if user_choice not in music_data:
#     print("Sorry, We don't have that genre.")
# else:
#     print(f"Check out: {random.choice(music_data[user_choice])}")
# ---------------------------------

# Color Mixer

# print("Color Mixer")

# color_mixes = {
#     ("red", "white"): "pink",
#     ("blue", "yellow"): "green",
#     ("red", "yellow"): "orange",
#     ("blue", "red"): "purple",
#     ("black", "white"): "gray",
#     ("blue", "white"): "light blue",
#     ("green", "yellow"): "lime",
#     ("brown", "white"): "tan",
# }

# while True:
#     color1 = input("Enter your first color: ").lower()
#     color2 = input("Enter your second color: ").lower()

#     mix = None

#     if (color1, color2) in color_mixes:
#         mix = color_mixes[(color1, color2)]

#     if mix:
#         print(f"When you mix {color1} and {color2}, you get {mix}")
#     else:
#         print("I don't know what those colors make when mixed.")

#     user_input = input("Would you like to try again? (y/n): ").lower()
#     if not user_input.startswith("y"):
#         print("Exiting......")
#         break
# ---------------------------------------

# Countdown Timer
# import time

# print("CountDown Timer")

# while True:
#     user_input = int(input("Enter your choosen coutdonw: "))

#     for count in range(user_input, 0, -1):
#         print(f"{count}...")
#         time.sleep(1)
#     print("Countdown Complete")

#     again = input("Try again? (y/n)").lower()
#     if not again.startswith("y"):
#         print("Exiting....")
#         break
# ---------------------------------------

# Calculator
# print("Calculator🧮")


# def addition(num1, num2):
#     return num1 + num2


# def subtraction(num1, num2):
#     return num1 - num2


# def multiplication(num1, num2):
#     return num1 * num2


# def division(num1, num2):
#     return num1 / num2


# while True:
#     print("Select operation:")
#     print("1. ➕  Addition")
#     print("2. ➖  Subtraction")
#     print("3. ✖️  Multiplication")
#     print("4. ➗  Division")
#     user_choice = input("Enter choice (1-4): ")

#     while True:
#         try:
#             first_num = float(input("Enter first number: "))
#             break
#         except ValueError:
#             print("❌ Invalid input. Please enter a number.")

#     while True:
#         try:
#             second_num = float(input("Enter second number: "))
#             break
#         except ValueError:
#             print("❌ Invalid input. Please enter a number.")

#     match user_choice:
#         case "1":
#             print(
#                 f"{first_num:.1f} ➕  {second_num:.1f} = {addition(first_num, second_num)}"
#             )

#         case "2":
#             print(
#                 f"{first_num:.1f} ➖  {second_num:.1f} = {subtraction(first_num, second_num)}"
#             )

#         case "3":
#             print(
#                 f"{first_num:.1f} ✖️  {second_num:.1f} = {multiplication(first_num, second_num)}"
#             )

#         case "4":
#             if second_num == 0:
#                 print("Error: Cannot divide by zero.")
#             print(
#                 f"{first_num:.1f} ➗  {second_num:.1f} = {division(first_num, second_num)}"
#             )

#     again = input("Do you want to perform another calculation? (y / n): ")
#     if not again.startswith("y"):
#         print("Exiting....")
#         break
# ------------------------------------------------------------------------------


# ----------------------------------------------------

# tasks = []


# def add_task():
#     title = input("Enter task title: ")
#     tasks.append({"title": title, "completed": False})
#     print(f"Task {title} added successfully")


# def view_tasks():
#     if not tasks:
#         print("No tasks found")
#         return
#     print("\n=== My Tasks ===")
#     for index, task in enumerate(tasks):
#         status = "✓" if task["completed"] else ""
#         print(f"{index + 1}. [{status}] {task["title"]}")

#     print("===========================\n")


# def complete_task():
#     view_tasks()

#     if not tasks:
#         return

#     try:
#         task_num = int(input("Enter task number to mark as completed: "))
#         if task_num < 1 or task_num > len(tasks):
#             print("Invalid task number.")
#             return
#         task_to_completed = tasks[task_num - 1]
#         task_to_completed["completed"] = True
#         print(f"Task '{task_to_completed["title"]}' marked as completed!")
#     except ValueError:
#         print("Please enter a valid number.")


# def delete_task():
#     view_tasks()
#     if not tasks:
#         return

#     try:
#         task_num = int(input("Enter task number to delete: "))
#         if task_num < 1 or task_num > len(tasks):
#             print("Invalid task number.")
#             return
#         deleted_task = tasks.pop(task_num - 1)
#         print(f"Task {deleted_task['title']} deleted successfully!")
#     except ValueError:
#         print("Please enter a valid number!")


# def display_menu():
#     print("\n=== Task Manager ===")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Complete Task")
#     print("4. Delete Task")
#     print("5. Exit")


# def main_program():
#     while True:
#         display_menu()
#         choice = input("Enter yoru choice (0-4): ")

#         if choice == "1":
#             add_task()
#         elif choice == "2":
#             view_tasks()
#         elif choice == "3":
#             complete_task()
#         elif choice == "4":
#             delete_task()
#         elif choice == "5":
#             print("GoodBye!")
#             break
#         else:
#             print("Invalid Choice. Please go with (0-4)")


# main_program()
# ------------------------------------------------------------------

# ChatBot
# import random
# import time


# def chatbot():
#     greetings = [
#         "Hello there! 😊",
#         "Hi friend!😊",
#         "Hey! Nice to meet you!🤚",
#         "How do you do!🐻",
#     ]

#     farewells = ["Goodbye!", "See you later!", "Bye bye!", "Until next time friend!"]

#     jokes = [
#         "Why do programmers prefer dark mode? Because the light attracts bugs!",
#         "Why did the Python developer go broke? Because he couldn’t find his `__cache__`.",
#         "Why did the function return early? It had a date with `None`.",
#         "How do you comfort a JavaScript bug? You `console` it.",
#     ]

#     facts = [
#         "A day on Venus is longer than its year.",
#         "Octopuses have three hearts and blue blood.",
#         "Napoleon was once attacked by a horde of bunnies.",
#         "Your stomach gets a new lining every 3–4 days.",
#     ]

#     bot_name = "ChatBot"
#     print(f"🤖 {bot_name} is starting up...")
#     time.sleep(1)

#     print(
#         f"""
#         🤖 Welcome to {bot_name} 🤖

#         I can chat about:
#         'joke' - Hear a funny jokoe
#         'fact' - Learn something new
#         'color' - My favorite  color
#         'bye' - End our chat
#           """
#     )

#     chatting = True

#     user_name = input("What is your name: ").lower().strip()

#     print(f"{bot_name}: Nice to meet you, {user_name}! How can I help you today?🤖")

#     while chatting:
#         user_input = input("😀You: ").strip()

#         if user_input in ["hi", "hello", "hey", "how do you do"]:
#             print(f"🤖{bot_name}: {random.choice(greetings)}")
#         elif "joke" in user_input:
#             print(f"🤖{bot_name}: {random.choice(jokes)}")
#         elif "facts" in user_input:
#             print(f"🤖{bot_name}: {random.choice(facts)}")
#         elif "color" in user_input:
#             print(f"🤖{bot_name}: My favorite color is blue🔵! What's yours?")
#             color = input("😀You: ")
#             print(f"🤖{bot_name}: {color} is a great color!")
#         elif user_input in ["bye", "goodbye", "exit", "quit"]:
#             print(f"🤖{bot_name}: {random.choice(farewells)}")
#             print(f"🤖{bot_name}: It was fun chatting with you, {user_name}")
#             chatting = False
#         else:
#             responses = [
#                 "That's interesting! Tell me more!",
#                 "I'm not sure I understand. Can you try again?",
#                 "Hmm, let's talk about something else. Try asking for joke or fact!",
#                 "Beep boop! My robot brain is processing t hat...🤔",
#             ]
#             print(f"🤖{bot_name}: {random.choice(responses)}")

#     print("Thanks for chatting! Run the program again to talk to me later!😊")


# chatbot()
# ---------------------------------------------------------------------------
