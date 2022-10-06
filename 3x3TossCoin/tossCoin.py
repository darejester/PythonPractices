from random import *
from fractions import Fraction
import numpy as np
import random

def coinFlip(num):
    coinBin = ""
    coinRep = ""
    ctr = 0
    zeroCtr = 0

    array = [[0,0,0],
             [0,0,0],
             [0,0,0]]

    #get binary representaiton of num
    coinBin = bin(num)
    zeroCtr = 9 - (len(coinBin)-2)
    coinBin = coinBin.replace("0b","0"*zeroCtr)

    #convert coinBin to H and T's
    coinRep = coinBin.replace("0", "H")
    coinRep = coinRep.replace("1", "T")

    #print coinRep in proper format using 2d arrays
    for r in range (0,3):
        for c in range (0,3):
            array[r][c] = coinRep[ctr]
            ctr +=1
    for r in range (0,3):
        print(" ".join(array[r]))


    return 0
    
    
def main():

    num = input("Enter a number between 0 and 511: ")
    coinFlip(int(num))

    return 0
    
    
    
# calls main()
if __name__ == "__main__":
    main() 
