import random

# Word list for the game
word_list = ['python', 'hangman', 'challenge', 'developer', 'keyboard']

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts_remaining = 6
    wrong_guesses = set()

    print(" Welcome to Hangman Game!")
    print("Guess the word one letter at a time.\n")

    while attempts_remaining > 0:
        print("Word: ", display_word(word_to_guess, guessed_letters))
        print(f"Wrong guesses: {', '.join(wrong_guesses)}")
        print(f"Attempts left: {attempts_remaining}")

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(" Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print(" You already guessed that letter.\n")
            continue

        if guess in word_to_guess:
            guessed_letters.add(guess)
            print(" Good guess!\n")
        else:
            wrong_guesses.add(guess)
            attempts_remaining -= 1
            print(" Wrong guess!\n")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"🎉 Congratulations! You guessed the word: {word_to_guess}")
            break
    else:
        print(f" Game Over! The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
