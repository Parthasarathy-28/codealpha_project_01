import random

# Predefined list of words
word_list = ["apple", "banana", "cherry", "grape", "lemon"]

# Select a random word
secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Display the word with underscores for unguessed letters
def display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

# Main game loop
print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while incorrect_guesses < max_incorrect:
    print("\nWord: ", display_word())
    print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess.")
        incorrect_guesses += 1

    # Check if all letters have been guessed
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        break
else:
    print("\nGame over. The word was:", secret_word)
