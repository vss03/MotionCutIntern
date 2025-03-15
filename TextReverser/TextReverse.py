def reverse_characters(text):
    return text[::-1]

def reverse_words(text):
    return " ".join(text.split()[::-1])

def save_to_file(content):
    try:
        with open("reversed_text.txt", "w", encoding="utf-8") as file:
            file.write(content)
        print("Reversed text saved to 'reversed_text.txt'")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    while True:
        print("\nText Reverser")
        print("1. Reverse Character Order")
        print("2. Reverse Word Order")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "3":
            print("Exiting program. Goodbye!")
            break
        
        text = input("Enter text: ").strip()
        if not text:
            print("Error: Input cannot be empty. Please enter valid text.")
            continue
        
        if choice == "1":
            reversed_text = reverse_characters(text)
        elif choice == "2":
            reversed_text = reverse_words(text)
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
            continue
        
        print("Reversed Text:", reversed_text)
        
        save_option = input("Do you want to save the reversed text? (y/n): ")
        if save_option.lower() == "y":
            save_to_file(reversed_text)

if __name__ == "__main__":
    main()
