import numpy as np
from random import *
from fractions import Fraction
import random
from pandas import Series, DataFrame
import pandas as pd
import wget

def highest_population(df):
    #print(df)
    print("HIGHEST POPULATION: ")
    print(df.loc[(df[4] == max(df.loc[(df[1] == 1),4]))])
    print(df.loc[(df[4] == max(df.loc[(df[1] == 5),4]))])

    return 0

def biggest(df):
    print("BIGGEST COUNTRY")
    print(df.loc[(df[3] == max(df.loc[(df[1] == 4),3]))])
                
    return 0

def religion(df):
    print("DOMINANT RELIGION")
    print(df.loc[(df[1] == 6),6].mode())
    
    return 0



def main():
    # dataset url
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data'

    #download file from internet
    filename = wget.download(url)

    #put file in a pandas dataframe
    df = pd.read_csv(filename, header=None )

    #formatting
    print("\n")

    highest_population(df)
    print("\n")
    biggest(df)
    print("\n")
    religion(df)

    



    return 0
    
    
    
# calls main()
if __name__ == "__main__":
    main() 
