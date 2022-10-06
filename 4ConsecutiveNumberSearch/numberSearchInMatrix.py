from random import *
from fractions import Fraction
import numpy as np
import random
from itertools import combinations

def isConsecutiveFour(values):
    #input number of rows and columns
    #rows = int(input("enter number of rows: "))
    #cols = int(input("enter number of columns: "))
    rows = 5
    cols = 5
    #this holds if there are 4 consecutive numbers
    case = False
    #this holds the four numbers to be examined
    four = []
    
    #print matrix
    print(values)
    
    #check if matrix can fit 4 consecutive numbers
    if (rows < 4 and cols < 4):
        case = False
        #print(case)
        return 0
    else:
        #continue
        
                                #DEBUG: matrix is big enough to fit 4 consecutive numbers at this point
    
     #check horizontal
     for r in range(rows):
        for c in range(cols-3):
            four = values[r,c:c+4]
            #print(four)
            four = set(four)
            if(len(set(four))==1):
                   case = True
                   print(case)
                   return 0
            else:
                continue

                                #DEBUG: we know that the matrix doesnt have any horizontal 4 consecutive numbers at this point


     #check vertical
     for c in range(cols):
        for r in range(rows-3):
            four = values[r:r+4,c]
            #print(four)
            four = set(four)
            if(len(set(four))==1):
                   case = True
                   print(case)
                   return 0
            else:
                continue 

                                #DEBUG: we know that the matrix doesnt have any vertical 4 consecutive numbers at this point

     #check diagonal1: highRight to lowLeft
     for r in range(3,rows):
        for c in range(cols-3):
            four = [values[r,c],values[r-1,c+1],values[r-2,c+2],values[r-3,c+3]]
            #print(four)
            four = set(four)
            if(len(set(four))==1):
                   case = True
                   print(case)
                   return 0
            else:
                continue

                                #DEBUG: we know that the matrix doesnt have any diagonal1 4 consecutive numbers at this point

     #check diagonal2: lowRight to highLeft
     for r in range(3,rows):
        for c in range(cols-1,2,-1):
            four = [values[r,c],values[r-1,c-1],values[r-2,c-2],values[r-3,c-3]]
            #print(four)
            four = set(four)
            if(len(set(four))==1):
                   case = True
                   print(case)
                   return 0
            else:
                continue

                                #DEBUG: we know that the matrix doesnt have any diagonal2 4 consecutive numbers at this point
        
     #print case when didnt pass any checks
     print(case)
    
    return 0
    
def main():
 
    #input here


    values = np.array([
                         [1,2,3,4,5],
                         [7,3,7,8,4],
                         [6,7,9,10,7],
                         [11,3,7,8,4],
                         [10,3,6,7,10]
                     ])
    
                                #DEBUG: numpy array matrix is filled out with values at this point

    #pass values(matrix) to function
    isConsecutiveFour(values)
    return 0
    
    
# calls main()
if __name__ == "__main__":
    main() 
