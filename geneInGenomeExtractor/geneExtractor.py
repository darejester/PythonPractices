from random import *
from fractions import Fraction
import random

def findGene(genome):
    start = "ATG"
    split_genome = []
    end = ["TAG","TAA","TGA"]
    
    split_genome = genome.split(start)
    #print(split_genome)

    for x in range(0,len(split_genome)):

        if any(i in split_genome[x] for i in end):
            for y in range (0,len(end)):

                if (split_genome[x].find(end[y])>0):
                    ind = split_genome[x].find(end[y])
                    print(split_genome[x][0:ind])
                else:
                    continue
        else:
            continue

    return 0
    
    
def main():
    genome = "TTATGTTTTAAGGATGGGGCGTTAGTT"
    #print(genome)

    findGene(genome)

    return 0
    
    
    
# calls main()
if __name__ == "__main__":
    main() 
