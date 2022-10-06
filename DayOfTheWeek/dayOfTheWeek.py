
from random import *
from fractions import Fraction

def func():
    days = ["Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    months = ["Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec","Jan", "Feb"]
    #day of the week
    h = -1
    #day of the month
    q = -1
    #month
    m = -1
    #century
    j = -1
    #year of century
    k = -1
    
    
    print("Enter Year: (e.g., 2008): ")
    year = int(input())

    j = int(Fraction(year/100))
    k = int(year%100)

    print("Enter month: 1-12:")
    m = (int(input()))
    if m <= 2:
        year =-1
        j = int(Fraction(year/100))
        k = int(year%100)

        while m >=12:
            m = m%12
            
    

    #print(m)

    print("Enter the day of the month: 1-31:")
    q = int(input())


        
    #formula
    h = int((q + (Fraction((26*(m+1))/10)) + k + (Fraction(k/4)) + (Fraction(j/4)) + (5*j))%7)
    


    print ("Day of the week is", days[h])
    return 0
    
    
def main():
    func()
    
    return 0
    
    
    
# calls main()
if __name__ == "__main__":
    main() 
