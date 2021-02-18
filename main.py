import random
from teams import wordList
from art import logo, stages
from replit import clear

endGame = False
chosenWord = random.choice(wordList)
wordLength = len(chosenWord)
lives = 6
# call logo from art class
print(logo)
# create the banks for display
display = []
for _ in range(wordLength):
    display += "_"

# Main game loop forcing all entered guesses to be in lower case.
while not endGame:
    guess = input('Guess a letter:  ').lower()
    clear()
    if guess in display:
        print(f"You've already guessed:     {guess}")

    for position in range(wordLength):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosenWord:
        print(f"{guess}:    is not in the word ,you lose a life.")
        lives -= 1
        if lives == 0:
            endGame = True
            print("You Lose!")

# Add elements in list to display
    print(f"{'' .join(display)}")

# End game state.
    if "_" not in display:
        endGame = True
        print("you win!!!!!")
# Print stages ASCII depending on the number of lives.
    print(stages[lives])
