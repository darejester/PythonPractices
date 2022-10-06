from random import *
from fractions import Fraction
import random

def isConsecutiveFour(values):
    a = ""
    ctr = 1

    for val in range(0,len(values)):
        a = values[val]
        if (val == len(values)-1):
            print ("There are NO four consecutive numbers with the same value")
            return 0
        else:

            if (values[val+1] == a):
                ctr+=1

                if (ctr == 4):
                    print ("There are four consecutive numbers with the same value")
                    return 0
                else:
                    ctr = ctr
            else:
                ctr = 1

    return 0
    
    
def main():
    values = [1,2,1,1,5,6,7,9,1,4,4,4,4] 

    print ("These are the values: ", values)


    isConsecutiveFour(values)

    return 0
    
    
    
# calls main()
if __name__ == "__main__":
    main() 
