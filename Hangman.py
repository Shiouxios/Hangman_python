# Import and clear terminal
import os
os.system('cls')

# Get player to choose a word
word = input("Player 1, choose a word: ")
word = word.lower()
print (word)

os.system('cls')

# Setup blank and wrong list
blanks = []
wrong = [2]

for x in range(0, len(word)):
    blanks.append("_")
 
lives = 10

# Loop of guesses
while lives > 0:
    
    os.system('cls')
    
    print ("Player 2, time to guess the word...", "\n", "\nLives", lives,"\n")

    for x in blanks:
        print (x, end=" ")
    
    letter_choice = 2
    while letter_choice in wrong:
        letter_choice = input ("...choose a letter: ") 
        if letter_choice in wrong:
            print ("Already tried that letter! Try again:")

    if letter_choice == "/":
        exit()


    if letter_choice not in word: # Reduce lives if letter not in word chosen
        lives -= 1
        wrong.append(letter_choice)
    
    for x in range(0, len(word)): # Replace underscore with letter if guessed correctly
        if word[x] == letter_choice:
            blanks[x] = letter_choice
    
    if word == "".join(blanks): # Winning scenario
        os.system('cls')
        print ("Lives", lives)
        print ("")
      
        for x in blanks:
            print (x, end=" ")

        print ("Congratulations!")
        exit()
    
# If all lives are lost, we get here
os.system('cls')

print ("Lives", lives)
print ("")

for x in blanks:
    print (x, end=" ")
print("Game over!")
print("")

        
        


