def count_words(text):
    #Function to count the number of words in a given text
    if not text.strip():
        print("Please type something..!!")  # Return 0 for empty input
    
    words = text.split()  # Split the text into words based on spaces
    return len(words)

def main():
    #Main function to handle user input and display word count
    print("Welcome to the Word Counter Program!")
    user_input = input("Enter a sentence or paragraph: ")
    
    word_count = count_words(user_input)
    print(f"Word Count: {word_count}")
    
if __name__ == "__main__":
    main()
