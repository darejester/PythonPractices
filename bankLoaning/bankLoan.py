import numpy as np
from random import *
from fractions import Fraction
import random

def fill(banks,bankNum):
    borrowers = 0

    # go through each row/bank
    for x in range (0, bankNum):
        # input user for filling banks
        line = input()

        # split input
        splitLine = line.split()
        splitLine = splitLine
                    # split_line should hold the line input as an array with each number splitted up
                    
        # parse input 
        banks[x][x] = float(splitLine[0])
        borrowers = int(splitLine[1])
        for y in range (2,(2+borrowers)+1):
            if (y%2 == 0):
                banks[x][int(splitLine[y])] = float(splitLine[y+1])
                    # current bank part of the matrix should be filled out with the correct values
                
    return 0
    

def judge(banks,bankNum,min):
    unsafe = []
    checker = 1

    while(checker > 0 ):
        checker = 0
        for x in range(0,bankNum):
            if(sum(banks[x,:]) < min):
                unsafe.append(x)
                checker = checker+1
            else:
                continue

    print(unsafe)

    
    return 0


def main():
    bankNum = 0
    min = 0

    # ask use how many banks there are and what the minimum asset is
    bankNum, min = input("How many banks are there and what is the minimum total asset?: ").split()
    bankNum = int(bankNum)
    min = int(min)
                # number of banks and minimum total asset is set 

    # make matrix
    banks = ((bankNum,bankNum))
    banks = np.zeros(banks)
                # banks should have the proper size

    # banks lend money to each other
    fill(banks,bankNum)
                # banks should have all of their respective values (loaned and borrowed)

    # judge whether each bank is safe
    judge(banks,bankNum, min)
    return 0
    
    
    
# calls main()
if __name__ == "__main__":
    main() 
