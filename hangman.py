import random #importing python random function
from words import words #getting a list of all the words from the words file in the hangman folder
import string

def get_valid_word(words): #creating a function so the computer chooses a VALID random word
    word = random.choice(words) #randomly chooses a word from the list
    while '-' in word or ' ' in word: #if the chosen word contains '-' or a space, it is an invalid word,
        # so we keep loopin until we get a valid word
        word = random.choice(words)
    return word.upper()


def hangman(): # function for the main game
    word = get_valid_word(words) #using the above function to get a word to be used
    word_letters = set(word) #getting each letter seprately into a set
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed stored in an empty set

    lives = 9
    #getting User input
    while len(word_letters) > 0 and lives > 0:
        # we keep iterating until the word letters are equal to 0 or the th
    #re are no more lives
        print(f'You have {lives} lives left and You have used the letters: {" and ".join(used_letters)}')# used letters

        word_list = [] #creating an empty list to store the word guessed
        for letter in word:
            if letter in used_letters: #condition to chect if letters have already been used
                word_list.append(letter) #adding each correctly guessed letter to the word list
            else:
                word_list.append('-') #if the guessis wrong, display a '-'
        print('Current word: ', ' '.join(word_list)) #display

        user_letter = input('Guess a letter: ').upper()#getting the user input and convert to upper case
        if user_letter in alphabet and user_letter not in used_letters: #condition for a valid letter
            used_letters.add(user_letter)
            if user_letter in word_letters : #condition for guessing correctly
                word_letters.remove(user_letter)#if the user guesses correctly,  remove the letter rom the word letter
            elif user_letter not in word_letters:
                lives = lives-1
                print(f'Letter {user_letter} is not in the word')
        elif user_letter in used_letters: #condition for guessing a used letter
            print('You have already used that character please try again')
        else:
            print('Invalid character please try again')
    if lives == 0:
        print(f'You died sorry.The correct word was {word}')
    else:
        print(f'You guessed the word, {word} correctly')


hangman()







