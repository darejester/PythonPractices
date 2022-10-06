from random import *
from fractions import Fraction
import random

def isbnChecker(isbn):
    total = 0
    sum = 0

    for x in range(0,len(isbn)):
        if x%2 == 0:
            sum+=(3*int(isbn[x]))
        else:
            sum+=int(isbn[x])
    
    #print(sum)

    checkSum = 10-(sum%10)
    if checkSum == 10:
        checkSum = "0"
    #print(checkSum)

    finalIsbn = isbn+str(checkSum)

    print(finalIsbn)
    return 0
    
    
def main():
    isbn =""
    while len(isbn) <12 or isbn.isdigit() == False:
        isbn = input("input the first 12 digits of an ISBN-13 as a string: ")

    isbnChecker(isbn) 

    return 0
    
    
    
# calls main()
if __name__ == "__main__":
    main() 
