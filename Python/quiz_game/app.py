# Quiz Game
import random
from sre_compile import dis
import time

print("\n" + "=" * 60)
print("🎮 Welcome To The Ultimate Quiz Challenge! 🎮")
print("=" * 60)
print("Instructions:")
print("- Choose a quiz category")
print("- Each correct answer is worth 10 point")
print("- See your final score at the end")
print("- Have fun and learn something new!")


# --------------------------------------------
general_knowledge = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A",
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": [
            "A. Vincent van Gogh",
            "B. Pablo Picasso",
            "C. Leonardo da Vinci",
            "D. Michelangelo",
        ],
        "answer": "C",
    },
    {
        "question": "What is the largest planet in our Solar System?",
        "options": ["A. Earth", "B. Saturn", "C. Jupiter", "D. Mars"],
        "answer": "C",
    },
    {
        "question": "Which language has the most native speakers worldwide?",
        "options": ["A. English", "B. Mandarin Chinese", "C. Spanish", "D. Hindi"],
        "answer": "B",
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C",
    },
]
movie_tv_trivia = [
    {
        "question": "Which movie features the quote, 'I'll be back'?",
        "options": ["A. Rambo", "B. Terminator", "C. Die Hard", "D. Predator"],
        "answer": "B",
    },
    {
        "question": "What is the name of the coffee shop in the sitcom 'Friends'?",
        "options": [
            "A. Central Brew",
            "B. Central Coffee",
            "C. Central Perk",
            "D. Café Friends",
        ],
        "answer": "C",
    },
    {
        "question": "Who played Iron Man in the Marvel Cinematic Universe?",
        "options": [
            "A. Chris Evans",
            "B. Robert Downey Jr.",
            "C. Chris Hemsworth",
            "D. Mark Ruffalo",
        ],
        "answer": "B",
    },
    {
        "question": "Which animated movie features a talking snowman named Olaf?",
        "options": ["A. Frozen", "B. Moana", "C. Tangled", "D. Encanto"],
        "answer": "A",
    },
    {
        "question": "In 'Stranger Things', what is the name of the parallel dimension?",
        "options": [
            "A. The Nether",
            "B. The Shadow Realm",
            "C. The Other Side",
            "D. The Upside Down",
        ],
        "answer": "D",
    },
]
science_nature_trivia = [
    {
        "question": "What gas do plants absorb from the atmosphere for photosynthesis?",
        "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
        "answer": "B",
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Quartz", "C. Diamond", "D. Obsidian"],
        "answer": "C",
    },
    {
        "question": "How many legs does an insect have?",
        "options": ["A. 4", "B. 6", "C. 8", "D. 10"],
        "answer": "B",
    },
    {
        "question": "Which planet is known for its rings?",
        "options": ["A. Jupiter", "B. Saturn", "C. Neptune", "D. Uranus"],
        "answer": "B",
    },
    {
        "question": "What part of the human body produces insulin?",
        "options": ["A. Liver", "B. Pancreas", "C. Kidney", "D. Spleen"],
        "answer": "B",
    },
]
video_game_trivia = [
    {
        "question": "Which video game character is known for collecting rings?",
        "options": ["A. Mario", "B. Sonic", "C. Link", "D. Donkey Kong"],
        "answer": "B",
    },
    {
        "question": "In which game do players compete in a battle royale on an island called Erangel?",
        "options": ["A. Fortnite", "B. PUBG", "C. Apex Legends", "D. Warzone"],
        "answer": "B",
    },
    {
        "question": "What is the name of the princess that Mario is always trying to save?",
        "options": ["A. Zelda", "B. Rosalina", "C. Daisy", "D. Peach"],
        "answer": "D",
    },
    {
        "question": "Which company developed the game 'The Legend of Zelda'?",
        "options": ["A. Sony", "B. Microsoft", "C. Nintendo", "D. Sega"],
        "answer": "C",
    },
    {
        "question": "What color is Pac-Man?",
        "options": ["A. Yellow", "B. Red", "C. Blue", "D. Green"],
        "answer": "A",
    },
]


def display_information():
    return "Answer each question by typing the letter of your choice (A,B,C,D)."


def general_knowledge_quizs():
    print("Starting The General Knowledge Quiz!")
    display_information()
    score = 0
    correct_answer = 0

    random_question_generalKnowledge = general_knowledge.copy()
    random.shuffle(random_question_generalKnowledge)

    for i, question in enumerate(random_question_generalKnowledge):
        print(f"{question['question']}")
        for option in question["options"]:
            print(option)

        user_choice = input("Your answer (A/B/C/D): ").strip().upper()
        if user_choice == question["answer"]:
            score += 10
            correct_answer += 1
            print("✅ Correct! +10 point")
        else:
            print(f"❌ Incorrect! The correct answer is {question['answer']}")

        if i < len(random_question_generalKnowledge) - 1:
            print("Next question coming up...\n")
            time.sleep(0.5)

    print(
        f"\nCorrect Answer: {correct_answer} / {len(random_question_generalKnowledge)}"
    )
    print(f"🏁 Final Score for General Knowledge Quiz: {score}")


def movie_tvshow_quizs():
    random_question_movieTVshow = movie_tv_trivia.copy()
    random.shuffle(random_question_movieTVshow)

    score = 0
    correct_answer = 0

    for i, question in enumerate(random_question_movieTVshow):
        print(f"{question["question"]}")
        for option in question["options"]:
            print(option)

        user_choice = input("Your answer (A/B/C/D): ").strip().upper()
        if user_choice == question["answer"]:
            score += 10
            correct_answer += 1
            print("✅Correct! +10 point")
        else:
            print(f"❌ Incorrect! The correct answer is {question['answer']}")
        if i < len(random_question_movieTVshow) - 1:
            print("Next question coming up...\n")
            time.sleep(0.5)
    print(f"\nCorrect Answer: {correct_answer} / {len(random_question_movieTVshow)}")
    print(f"🏁 Final Score for General Knowledge Quiz: {score}")


def science_nature_quizs():
    random_question_science_nature = science_nature_trivia.copy()
    random.shuffle(random_question_science_nature)

    score = 0
    correct_answer = 0

    for i, question in enumerate(random_question_science_nature):
        print(f"{question["question"]}")
        for option in question["options"]:
            print(option)

        user_choice = input("Your answer (A/B/C/D): ").strip().upper()
        if user_choice == question["answer"]:
            score += 10
            correct_answer += 1
            print("✅Correct! +10 point")
        else:
            print(f"❌ Incorrect! The correct answer is {question['answer']}")
        if i < len(random_question_science_nature) - 1:
            print("Next question coming up...\n")
            time.sleep(0.5)
    print(f"\nCorrect Answer: {correct_answer} / {len(random_question_science_nature)}")
    print(f"🏁 Final Score for General Knowledge Quiz: {score}")


def video_game_quizs():

    random_question_video_game = video_game_trivia.copy()
    random.shuffle(random_question_video_game)

    score = 0
    correct_answer = 0

    for i, question in enumerate(random_question_video_game):
        print(f"{question["question"]}")
        for option in question["options"]:
            print(option)

        user_choice = input("Your answer (A/B/C/D): ").strip().upper()
        if user_choice == question["answer"]:
            score += 10
            correct_answer += 1
            print("✅Correct! +10 point")
        else:
            print(f"❌ Incorrect! The correct answer is {question['answer']}")
        if i < len(random_question_video_game) - 1:
            print("Next question coming up...\n")
            time.sleep(0.5)
    print(f"\nCorrect Answer: {correct_answer} / {len(random_question_video_game)}")
    print(f"🏁 Final Score for General Knowledge Quiz: {score}")


def random_mix_quizs():
    score = 0
    correct_answer = 0
    all_questions = (
        general_knowledge + movie_tv_trivia + science_nature_trivia + video_game_trivia
    )

    all_questions = random.sample(all_questions, 5)

    for i, question in enumerate(all_questions):
        print(f"{question["question"]}")
        for option in question["options"]:
            print(f"{option}")

        user_choice = input("Your answer (A/B/C/D): ").strip().upper()
        if user_choice == question["answer"]:
            score += 10
            correct_answer += 1
            print("✅Correct! +10 point")
        else:
            print(f"❌ Incorrect! The correct answer is {question['answer']}")
        if i < len(all_questions) - 1:
            print("Next question coming up...\n")
            time.sleep(0.5)
    print(f"\nCorrect Answer: {correct_answer} / {len(all_questions)}")
    print(f"🏁 Final Score for General Knowledge Quiz: {score}")


def main():
    while True:
        print("\n🗃️ Quiz Categories:")
        print("1. 🌏 General Knowledge")
        print("2. 🎬 Movies and TV Shows")
        print("3. 🔬 Science and Nature")
        print("4. 🎮 Video Game")
        print("5. 🎲 Random Mix (questions from all categories)")
        print("6. 📤 Exit")

        choice = input("\nSelect a category (1-5): ")
        match choice:
            case "1":
                general_knowledge_quizs()
            case "2":
                movie_tvshow_quizs()
            case "3":
                science_nature_quizs()
            case "4":
                video_game_quizs()
            case "5":
                random_mix_quizs()
            case "6":
                print("Exiting...")
                break
            case _:
                print("Invalid choicd! Please enter a number from 1 to 3.")
    pass


main()
