#!/usr/bin/env python3
# so that the computer knows how to read this
import sys
#so that the user can input info from the command line
from fasta_iterator_class import FASTAReader
#we reference these functions

def main():
    reader = FASTAReader(open(sys.argv[1]))
    # so that the target file is the first argument
    
    kmers = {}
    k = int(sys.argv[3])
    # so that the kmer size is the third argument
    
    for seq_id, sequence in reader:
        for i in range(0, len(sequence) - (k + 1)):
            kmer = sequence[i:(i + k)]

            if kmers.get(kmer) == None:
                kmers.setdefault(kmer, 0)
                kmers[kmer] = (seq_id, i)
                
            else:
                kmers[kmer] += (seq_id,i)
        
        
    reader_2 = FASTAReader(open(sys.argv[2]))
    #so the querry seq is the third argument
    
    k = int(sys.argv[3])
  
    for seq_id, sequence in reader_2:
        
        for i in range(0, len(sequence) - k + 1):
            kmer_2 = sequence[i:(i + k)]
            
            if kmers.get(kmer_2) == None:
                continue
                
            else:
                print(kmers.get(kmer_2), i, kmer_2)

        
if __name__ == "__main__":
    main()