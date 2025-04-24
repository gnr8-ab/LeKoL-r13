def count_words(sentence):
    # Split the sentence into words and count them
    words = sentence.split()
    return len(words)

def main():
    # Ask for user input
    user_sentence = input("Skriv in en mening: ")
    
    # Count the words
    word_count = count_words(user_sentence)
    
    # Print the result
    print(f"Antalet ord i meningen är {word_count}")

if __name__ == "__main__":
    main() 