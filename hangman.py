#Python practice project 
#get a random word, give 4 chances to opponent to guess the correct word, if the person guesses the word then the player wins other they lose

import random
from word_list import word

attempts = 10

# get valid words without spaces, colons, underscores or commas
def get_random_word():
    ran_word = random.choice(word)
    
    # check if the word contains commas, spaces, or dashes 
    while("-" in ran_word or " " in ran_word or "_" in ran_word or len(ran_word) > 6):
        ran_word = random.choice(word)
    return ran_word.upper()

def hangman():
    global attempts
    ranword = get_random_word()
    letters = list(ranword)
    used_letters = list()
    print("Correct word:",ranword)
    correct_word = ['-' for letter in letters]
    print("Word to input: "," ".join(correct_word))
    
    while attempts > 0:
        input_letter = str(input("Enter a letter: ")).upper()
        print("Inputted letter: ", input_letter)
        
        if input_letter in correct_word or input_letter in used_letters:
            print(f"Word used already..\n Remaining Attempts: {attempts}")
            attempts = attempts - 1
        else:
            for i in range(len(letters)):
                if input_letter != correct_word[i] and input_letter == letters[i]:
                    correct_word[i] = input_letter
        
        if input_letter not in used_letters:
            used_letters.append(input_letter)
        

        print("Letters Used: ", " ".join(used_letters))
            
        print("Word: ", " ".join(correct_word))
        
        if(correct_word == letters):
            print("Word Guessed Successfully...\n Congratulations\n")
            return False
        
    print(f"Sorry, you've run out of attempts..\n The correct word is: {ranword}")
        
print("-----------------------------HANGMAN--------------------------")
print("Starting...")
hangman()
