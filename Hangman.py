
import random
from WordLIB import words


# Hangman game!
# Assume the answer is "hangman"
A = random.choice(words)
B = list(A.upper())
C = " _" * len(B)
L = list("_" * len(B))
U = " "
D = " "
play = True
counter = 8
print(C)
while play == True and counter > 0:
    # Ask the user to guess a letter
    print(" ")
    letter = str(input("Guess a letter: ")).upper()
    D += letter
    
    # Check to see if that letter is in the Answer
    i=0
    if letter in U:
        print("")
        print("ALREADY GUESSED AND DISPLAYED!!")
        print(" ")

    for currentletter in B:
        # If the letter the user guessed is found in the answer, # set the underscore in the user's answer to that letter
        if letter == currentletter:
            L[i] = letter
            U+= letter
            
        i+=1
    print(" ")
    print(D)
    print(" ")

    if letter not in B:
        print("bad guess")
        print(" ")
    counter-=1


            
        
    # Display what the player has thus far (L) with a space # separating each letter
    print(' '.join(str(n) for n in L))
    # Test to see if the word has been successfully completed, # and if so, end the loop
    if B == L:
        play = False
        print(" ")
        print("GREAT JOB!!")
        print("")
        
    
    elif counter == 0:
        print(" ")
        print("GAME OVER!!")
        print("")
        print(A)

        print(" ")
    



