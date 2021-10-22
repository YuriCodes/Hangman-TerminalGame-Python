import random
from words import words
import string 
from hangman_visual import lives_visual

def get_valid_word(words):
    # Randomly pick a word from the list
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 7
    
    # Get user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print("You have", lives, "lives left and You have used these letters: ", " ".join(used_letters))

        # what current word is with dashes in the characters they haven't guessed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual[lives])
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
    # If it's on the alphabet and not in the used letters, add it
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter) 
                print('')
            
            else: lives = lives - 1
            print(user_letter, 'Letter is not in the word.')
        
        elif user_letter in used_letters:
            print("You have already used that character. Try again.")
        else:
            print("That's not a valid character. Try again.")

    if lives == 0:
        print(lives_visual[lives])
        print("You have died. The word is: ", word)
    else:
        print("You guessed the word! It's:", word)




if __name__ == '__main__':
    hangman()