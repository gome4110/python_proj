# print("Reverse Name Generator")

# while True:
#     user_name = input("Enter a name: ")

#     char_list = list(user_name)
#     char_list.reverse()
#     rev_name = "".join(char_list)
#     print(rev_name)

#     user_input = input("Try another name? (y/n): ")
#     if user_input.lower() == "n":
#         print("Bye!")
#         break

# another way
# while True:
#     name = input("Enter a name: ")
#     rev_name = name[::-1]
#     print(rev_name)

# ----------------------------------

# 8
# def is_palindrome(num):
#     if num < 0:
#         return False
#     num_str = str(num)
#     rev_str = num_str[::-1]
#     return num_str == rev_str


# print(is_palindrome(121))
# print(is_palindrome(123))
# print(is_palindrome(-121))

# ---------------------------------


# import random

# proteins = ["chicken", "beef", "tofu", "pork", "shrimp", "salmon", "egg"]
# vegetables = ["carrot", "spinach", "broccoli", "onion", "tomato", "pepper", "zucchini"]
# carbs = [
#     "rice",
#     "pasta",
#     "bread",
#     "tortilla",
#     "noodles",
#     "potatoes",
#     "couscous",
#     "quinoa",
#     "crackers",
#     "sweet potatoes",
#     "ramen",
#     "gnocchi",
#     "bagel",
#     "polenta",
#     "rice noodles",
# ]
# methods = [
#     "grilled",
#     "baked",
#     "roasted",
#     "stir-fried",
#     "steamed",
#     "boiled",
#     "pan-seared",
#     "deep-fried",
#     "braised",
#     "slow-cooked",
#     "sautéed",
#     "broiled",
#     "poached",
#     "smoked",
#     "air-fried",
# ]
# flavors = [
#     "spicy",
#     "sweet",
#     "savory",
#     "tangy",
#     "smoky",
#     "sour",
#     "umami",
#     "mild",
#     "zesty",
#     "buttery",
#     "rich",
#     "herby",
#     "earthy",
#     "garlicky",
#     "citrusy",
# ]


# while True:
#     rand_protain = random.choice(proteins)
#     rand_vege = random.choice(vegetables)
#     rand_carb = random.choice(carbs)
#     rand_method = random.choice(methods)
#     rand_flavor = random.choice(flavors)

#     print(
#         f"{rand_flavor.capitalize()} {rand_method} {rand_protain} served with {rand_vege} and {rand_carb}."
#     )

#     user_input = input("Generate another recipe? (y/n): ")
#     if not user_input.startswith("y"):
#         break
# -------------------------------

# 6
# import random

# first_parts = ["Sun", "Moon", "Olive", "Knight"]
# second_parts = ["Kai", "Luna", "Max", "Crystal"]


# user_nums = int(input("How many name would you like to generate?: "))

# for num in range(user_nums):
#     full_lists = first_parts + second_parts
#     random.shuffle(full_lists)

#     # after shuffel["Kai", "Olive", "Crystal", "Sun", "Moon", "Max", "Knight", "Luna"]
#     # full_lists[:2] - means start at index 0 & stop before index 2.
#     # so it graps "Kai" & "Olive"
#     # and we use "".join() - "KaiOlive"
#     shuffel_name = "".join(full_lists[:2])

#     print(f"{shuffel_name}")

# -----------------------
# another way
# import random

# first_name = ["Sun", "Moon", "Olive", "Knight"]
# last_name = ["Kai", "Luna", "Max", "Crystal"]

# user_num = int(input("How many names do you want to generate?: "))

# for i in range(user_num):
#     firtName = random.choice(first_name)
#     lastName = random.choice(last_name)

#     full_name = firtName + " " + lastName

#     print(f"{full_name}")
# -----------------------------------

# Password Generator
# import random
# import time
# import string


# def generate_password(length, use_lowercase, use_uppercase, use_number, use_special):
#     chars = ""

#     if use_lowercase:
#         chars += string.ascii_lowercase

#     if use_uppercase:
#         chars += string.ascii_uppercase

#     if use_number:
#         chars += string.digits

#     if use_special:
#         chars += string.punctuation

#     # if user type no to all
#     if not chars:
#         print(
#             "⚠️ Oops! No character types selected. Using lowercase letters by default!"
#         )
#         chars = string.ascii_lowercase

#     password = ""
#     for _ in range(length):
#         password += random.choice(chars)
#     return password


# def check_password_strength(password):
#     score = min(len(password) / 16, 1.0)

#     has_lower = any(c.islower() for c in password)
#     has_upper = any(c.isupper() for c in password)
#     has_digit = any(c.isdigit() for c in password)
#     has_special = any(c in string.punctuation for c in password)

#     variety = (has_lower + has_upper + has_digit + has_special) / 4.0

#     final_score = (score * 0.6) + (variety * 4.0)

#     if final_score >= 0.8:
#         return "Ultra Strong"
#     elif final_score >= 0.6:
#         return "Strong"
#     elif final_score >= 0.4:
#         return "Decent"
#     else:
#         return "need to improve"


# def get_yes_no_input(question):
#     while True:
#         response = input(question + " (y/n): ").lower()
#         if response in ["yes", "y"]:
#             return True
#         elif response in ["no", "n"]:
#             return False
#         else:
#             print("I didn't get that! Please enter 'y' or 'n'.")


# def main():
#     print("=== Password Generator ===")
#     print("Create super strong and secure passwords with ease!")

#     while True:
#         try:
#             length = int(input("enter password length (8-20): "))
#             if length >= 8 and length <= 20:
#                 break
#             else:
#                 print("Please choose a length between 8 and 20!")
#         except ValueError:
#             print("Oops! Please enter a number, like 12 or 16.")

#     print("Let's customize your password!")
#     use_lowercase = get_yes_no_input("Include lowercase letters (a-z)?")
#     use_uppercase = get_yes_no_input("Include uppercase letters (a-z)? ")
#     use_number = get_yes_no_input("Include numbers letters (0-9)? ")
#     use_special = get_yes_no_input("Include special character (@#$!)? ")

#     print("\nGenerating your magical password...")
#     time.sleep(0.5)

#     password = generate_password(
#         length, use_lowercase, use_uppercase, use_number, use_special
#     )

#     print("=== Your New Password ===")
#     print(f"🔑{password}")

#     strength = check_password_strength(password)
#     print(f"Strength: {strength}")

#     if get_yes_no_input("\nWould you like to create another: "):
#         main()
#     else:
#         print("Exiting")


# main()
# -------------------------------------------------------------------------
