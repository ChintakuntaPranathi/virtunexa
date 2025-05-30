import random
import os

def load_words():
    # Automatically adjust path for OS compatibility
    base_path = os.path.dirname(__file__)
    word_file = os.path.join(base_path, "word_list.txt")

    try:
        with open(word_file, 'r') as f:
            words = [line.strip() for line in f if line.strip()]
        if not words:
            raise ValueError("Word list is empty.")
        return words
    except FileNotFoundError:
        print("❌ Error: word_list.txt not found.")
        return []
    except Exception as e:
        print(f"❌ Error loading words: {e}")
        return []

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    words = load_words()
    if not words:
        return

    word = random.choice(words).lower()
    guessed = set()
    wrong_guesses = set()
    attempts = 6

    print("🎯 Welcome to Hangman!")

    while attempts > 0:
        print("\n🔤 Word:", display_word(word, guessed))
        print("❌ Wrong guesses:", ' '.join(sorted(wrong_guesses)))
        print("❤️ Attempts left:", attempts)
        guess = input("👉 Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabetic character.")
            continue

        if guess in guessed or guess in wrong_guesses:
            print("⚠️ Already guessed.")
            continue

        if guess in word:
            guessed.add(guess)
            print("✅ Correct!")
        else:
            wrong_guesses.add(guess)
            attempts -= 1
            print("❌ Incorrect.")

        if all(letter in guessed for letter in word):
            print(f"\n🎉 You won! The word was: {word}")
            return

    print(f"\n💀 Game Over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()



