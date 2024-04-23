import random
from hangman_art import logo, stages
import hangman_words
from replit import clear
#Step 1

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-1: - Create an empty List called display.
#TODO For each letter in the chosen_word, add a "_" to 'display'.
#TODO So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#TODO Set 'lives' to equal 6.
print(logo)
chosen_word = random.choice(hangman_words.word_list)
split_word = list(chosen_word)
lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
number_of_letters = len(chosen_word)
display1 = []
for x in range(0, number_of_letters):
  display1 += "_"

end_game = False
while end_game  == False:#display1 != split_word:
    clear()

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-2: - Loop through each position in the chosen_word;
#TODO If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#TODO e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# TODO-2: - If guess is not a letter in the chosen_word,
# TODO Then reduce 'lives' by 1.
# TODO If lives goes down to 0 then the game should stop and it should print "You lose."

    guess = input("Guees a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#TODO Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    letter_repent = False
    if guess in display1:
        letter_repent = True
    for letter in range(0,number_of_letters):
        if split_word[letter] == guess:
            display1[letter] = guess

    if guess not in split_word:
        lives  -= 1
        print(stages[lives])
        print(f"You guessed '{guess}' that is not in word, you lose a life.")
        if lives == 0:
            end_game = True
            print("You lose")
    elif letter_repent:
        print(f"You've already guessed '{guess}'")

    print(f"{''.join(display1)}")
    if "_" not in display1:
        end_game = True
        print("You win")
