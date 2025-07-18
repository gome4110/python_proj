# print("🏃‍➡️ STEP COUNTER 🏃‍♂️")

# # user can enter 0, if 0 keep asking the daily step goal
# # only loop out if more than 0
# user_steps_goal = 0

# while user_steps_goal is 0:
#     user_steps_goal = int(input("What is your daily step goal? "))
#     if user_steps_goal > 0:
#         break
#     print("Step goal must be greater than 0.")

# steps_taken = int(input("How many steps have you taken today? "))

# if steps_taken > user_steps_goal:
#     exceed_steps = steps_taken - user_steps_goal
#     print(f"🎉 Big Congratulations! You’ve exceeded your goal by {exceed_steps} steps!")
# elif steps_taken == user_steps_goal:
#     print("✅ Congratulations! You reached your goal exactly!")
# else:
#     remaining_steps = user_steps_goal - steps_taken
#     print(f"👣 Keep going! You need {remaining_steps} more steps to reach your goal.")
# -------------------------------------------------------------------------


# Word Counter
# def count_words(text):
#     words = text.split()
#     return len(words)


# def count_characters(text, include_space):
#     if include_space:
#         return len(text)
#     else:
#         return len(text.replace(" ", ""))


# def count_sentence(text):
#     sentence_endings = [".", "!", "?"]
#     count = 0

#     for char in text:
#         if char in sentence_endings:
#             count += 1

#     if count == 0 and text.strip():
#         count = 1
#     return count


# def analyze_text(text):
#     word_count = count_words(text)
#     char_count_with_space = count_characters(text, True)
#     char_count_without_space = count_characters(text, False)
#     sentence_count = count_sentence(text)

#     if sentence_count > 0:
#         word_per_sentence = word_count / sentence_count
#     else:
#         word_per_sentence = 0

#     if word_count > 0:
#         chars_per_word = char_count_with_space / word_count
#     else:
#         chars_per_word = 0

#     print("=== Text Analysis Results ===")
#     print(f". Words: {word_count}")
#     print(f". Characters (with space): {char_count_with_space}")
#     print(f". Characters (without space): {char_count_without_space}")
#     print(f". Sentences: {sentence_count}")
#     print(f". Average words per sentence: {word_per_sentence:.1f}")
#     print(f". Average characters per words: {chars_per_word:.1f}")

#     reading_time_minutes = word_count / 225
#     if reading_time_minutes < 1:
#         reading_time_seconds = reading_time_minutes * 60
#         print(f". Estimated reading time: {reading_time_seconds:.0f}")


# def main():
#     print("\n=== Word Counter ===")
#     print("Count words, characters, and sentences in your text")

#     while True:
#         print("\nChoose an option:")
#         print("1. Enter text to analyze: ")
#         print("2. Exit")

#         choice = input("\nYour choice (1/2): ")

#         if choice == "1":
#             print("\n Enter or past your text below (press Enter twice to finish): ")
#             lines = []
#             while True:
#                 line = input()
#                 if not line and not lines[-1]:
#                     break
#                 lines.append(line)
#             text = "\n".join(lines)
#             if not text.strip():
#                 print("No text provided. Please try again")
#                 continue
#             analyze_text(text)
#         elif choice == "2":
#             print("Goodbye")
#             break
#         else:
#             print("Invalid choice. Please enter 1/2")


# main()
# ----------------------------------------------------------------

# Currency Conveter (using API for rate)
# from unittest import result
# import requests


# def main():
#     print("Simple Currency Converter")
#     print("Getting exchange rates...")

#     try:
#         response = requests.get("https://open.er-api.com/v6/latest/USD")
#         rates = response.json()["rates"]
#         print("✅Got rates successfully!")

#     except:
#         print("Error: Couldn't connect to exchange rate API")
#         return

#     print("Popular: USD EUR GBP JPY CAD AUD CNY INR")

#     while True:
#         print("Enter details: ")
#         from_currency = input("From currency code (e.g. USD): ").upper()
#         if from_currency not in rates:
#             print(f"Invalid code: {from_currency}")
#             continue
#         to_currency = input("To currency code (e.g. EUR): ").upper()
#         if to_currency not in rates:
#             print(f"Invalid code: {to_currency}")
#             continue

#         try:
#             amount = float(input(f"Amount in {from_currency}: "))
#         except:
#             print("Please enter a valid number")
#             continue

#         amount_in_usd = amount / rates[from_currency]
#         result = amount_in_usd * rates[to_currency]

#         print(f"Result: {amount} {from_currency} = {result:.2f} {to_currency}")
#         print(
#             f"Rate: 1 {from_currency} = {rates[to_currency] / rates[from_currency]:.4f} {to_currency}"
#         )

#         if not input("Convert again? (y/n): ").lower().startswith("y"):
#             print("Goodbye!")
#             break


# main()
# ------------------------------------------------------------------------------
