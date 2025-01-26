import random
import string

def generate_username(adjectives, nouns, include_numbers, include_specials, length):
    #Generates a random username based on user preferences.
    adj = random.choice(adjectives)
    noun = random.choice(nouns)

    username = adj + noun

    if include_numbers:
        username += str(random.randint(0, 999))

    if include_specials:
        username += random.choice(string.punctuation)

    if length:
        username = username[:length]

    return username

def save_usernames_to_file(usernames, filename="usernames.txt"):
    #Saves the generated usernames to a file.
    with open(filename, "w") as file:
        file.write("\n".join(usernames))
    print(f"Usernames saved to {filename}")

def main():
    print("Welcome to the Username Generator!")

    # Predefined lists of adjectives and nouns
    adjectives = ["Cool", "Happy", "Fast", "Silly", "Brave", "Bright", "Lazy", "Wild"]
    nouns = ["Tiger", "Dragon", "Eagle", "Wizard", "Phoenix", "Knight", "Pirate", "Shark"]

    # User preferences
    include_numbers = input("Include numbers in usernames? (yes/no): ").strip().lower() == "yes"
    include_specials = input("Include special characters in usernames? (yes/no): ").strip().lower() == "yes"

    try:
        length = int(input("Set a maximum length for usernames (0 for no limit): ").strip())
        length = length if length > 0 else None
    except ValueError:
        print("Invalid input for length. Using no limit.")
        length = None

    try:
        num_usernames = int(input("How many usernames would you like to generate? ").strip())
    except ValueError:
        print("Invalid number of usernames. Generating 10 by default.")
        num_usernames = 10

    # Generate usernames
    usernames = [
        generate_username(adjectives, nouns, include_numbers, include_specials, length)
        for _ in range(num_usernames)
    ]

    # Display usernames
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)

    # Save to file
    save_usernames = input("Would you like to save these usernames to a file? (yes/no): ").strip().lower()
    if save_usernames == "yes":
        save_usernames_to_file(usernames)

if __name__ == "__main__":
    main()
