from operator import add


print("Self-Checkout")

# Data for movies
dc_adventure_movies = {
    "Aquaman": 11.99,
    "Wonder Woman": 12.50,
    "The Dark Knight": 13.99,
    "Shazam!": 10.99,
    "Justice League": 9.99,
    "Man of Steel": 11.49,
    "The Flash": 12.25,
    "Black Adam": 12.75,
    "Batman v Superman": 10.50,
    "Suicide Squad": 9.75,
}

# Data for fruits
fruits = {
    "Apple": 0.99,
    "Banana": 0.59,
    "Orange": 0.79,
    "Mango": 1.50,
    "Grapes": 2.99,
    "Pineapple": 3.49,
    "Strawberry": 2.50,
    "Blueberry": 3.99,
    "Watermelon": 4.99,
    "Kiwi": 0.89,
}


# this is where movie can store
movie_cart = {}

# this is where fruit can store
fruit_cart = {}

while True:
    print("\n1. Movie")
    print("2. Fruit")
    print("3. Checkout")
    print("4. Exit")
    user_option = input("Choose your option: ")

    print("\n")

    match user_option:
        case "1":
            print("You have chosen option 1. Movie 📽️")
            print("🛒 Here is the list of Movies you can add to your cart: ")
            for title, price in dc_adventure_movies.items():
                print(f"📽️ {title} - 💰${price:.2f}")

            print("\n")

            while True:
                add_movie = (
                    input("➕ Add Movie (Type 'done' to finish) 😊: ").strip().title()
                )

                if add_movie.lower() == "done":
                    break

                if add_movie in dc_adventure_movies:
                    try:
                        quantity = int(input(f"How many {add_movie} would you lilke?"))
                        if quantity <= 0:
                            print("Please enter a positive quantity.")
                            continue
                        if add_movie in movie_cart:
                            movie_cart[add_movie][1] += quantity
                        else:
                            movie_cart[add_movie] = [
                                dc_adventure_movies[add_movie],
                                quantity,
                            ]
                    except ValueError:
                        print("Please enter a valid number for quantity.")
                else:
                    print("❌That movie is not in our data. Try again")

            print("\nMovies in your cart:")
            total_movie_price = 0
            for title, [price, qty] in movie_cart.items():
                subtotal = price * qty
                print(f"✔️ {title} (x{qty}) - ${subtotal:.2f}")
                total_movie_price += subtotal
            print(f"Total price for movies: ${total_movie_price:.2f}")

        case "2":
            print("You have chosen option 2. Fruit 🍎🍇🍋")
            print("🛒 Here is the list of Fruits you can add to your cart: ")
            for fruit_name, fruit_price in fruits.items():
                print(f"✔️ {fruit_name} - ${fruit_price:.2f}")

            print("\n")

            while True:
                add_fruit = (
                    input("➕ Add Fruit (Type 'done' to finish) 😊: ").strip().title()
                )
                if add_fruit.lower() == "done":
                    break
                if add_fruit in fruits:
                    try:
                        quantity = int(input(f"How many {add_fruit} would you like? "))
                        if quantity <= 0:
                            print("Please enter a positive quantity.")
                            continue
                        if add_fruit in fruit_cart:
                            fruit_cart[add_fruit][1] += quantity
                        else:
                            fruit_cart[add_fruit] = [
                                fruits[add_fruit],
                                quantity,
                            ]
                    except ValueError:
                        print("Please enter a valid number for quantity.")
                else:
                    print("❌That fruit is not in our data. Try again.")

            print("\nFruits in your cart:")
            total_fruit_price = 0
            for fruit_name, [price, qty] in fruit_cart.items():
                subtotal = price * qty
                print(f" {fruit_name} (x{qty}) - ${subtotal:.2f}")
                total_fruit_price += subtotal
            print(f"Total price for fruit: ${total_fruit_price:.2f}")

        case "3":
            print("You choose option 3: Checking Out")
            total_movie_price = 0
            total_fruit_price = 0

            print("\nMovie in your cart: ")
            if movie_cart:
                for title, [price, qty] in movie_cart.items():
                    subtotal = price * qty
                    print(f"✔️ {title} (x{qty}) - ${subtotal:.2f}")
                    total_movie_price += subtotal
            else:
                print("No movies in your cart.")

            print("\nFruits in your cart:")
            if fruit_cart:
                for fruit_name, [price, qty] in fruit_cart.items():
                    subtotal = price * qty
                    print(f"✔️ {fruit_name} (x{qty}) - ${subtotal:.2f}")
                    total_fruit_price += subtotal
            else:
                print("No fruits in your cart.")
            grand_total = total_movie_price + total_fruit_price
            print(f"\nYour Grand Total is - ${grand_total:.2f}")

        case "4":
            print("🛍️ Thank you for Shopping 😊")
            break

        case _:
            print("Invalid option. Please choose 1, 2, 3, or 4.")
