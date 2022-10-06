from random import *
from fractions import Fraction
import random

def pickWord():
    words = ["write", "that", "program"]
    ind = random.randint(0,2)
    #print(words[ind])

    return(words[ind])
    
    
def main():
    repeat = 1
    ans = 1
    done = 0
    miss = 0
    letters = ''
    # generate random word
    currWord = pickWord()
    hiddWord = ["*"]*len(currWord)

    while repeat != 0:
        
        #print(currWord)
        print("(Guess) Enter a letter in word ",''.join(hiddWord), " > ", end = "")

        # guess letter
        guess = input()

        if(guess in currWord):
            if(guess in letters):
                print("  ", guess, " is already in the word")
            else:
                for char in range(0,len(currWord)):
                    if(currWord[char] == guess):
                        hiddWord[char] = guess
                    else:
                        continue
                letters+=guess
        else:
            if(guess in letters):
                print("  ", guess, " is already guessed")
            else:
                print("  ", guess, " is not in the word")
                letters+=guess
                miss += 1



        if ('*' not in hiddWord):
            # play agian?
            print("The word is ", ''.join(hiddWord))
            print("You missed ", miss)

            print("Do you want to guess another word? Enter 1 for yes, 0 for no")
            ans = input()
            if ans == "0":
                print("Program exiting...")
                repeat = 0
            else:
                currWord = pickWord()
                hiddWord = ["*"]*len(currWord)
                letters = ''
                miss = 0
                continue
        else:
            continue





    
    return 0
    
    
    
# calls main()
if __name__ == "__main__":
    main() 
