
from random import *
from fractions import Fraction

def isAnagram(str1,str2):
    #check if lengths are equal
    if (len(str1) == len(str2)):
        print("String lengths are Equal")
    else:
        print("String lengths are not equal")
        print("Strings are not anagrams")
        return 0
    
    #check if both strings have the same characters
    for x in str1:
        ctr = 1
        for y in str2:

            if ((str(x) != str(y)) and (ctr == len(str2))):
                print ("Strings are not anagrams")
                return 0
            elif (str(x) == str(y)):

                ctr +=1
                break
            else:
                ctr +=1
                continue

    print("Strings are anagrams!")
    return 0
    
    
def main():
    #input
    print("Input string 1: ")
    str1 = input()

    print("Input string 2:")
    str2 = input()

    isAnagram(str1,str2)
    
    return 0
    
    
    
# calls main()
if __name__ == "__main__":
    main() 
