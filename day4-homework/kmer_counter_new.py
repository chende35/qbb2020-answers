#!/usr/bin/env python3
import sys
from fasta_iterator_class import FASTAReader
def main():
    reader = FASTAReader(open(sys.argv[1]))
    kmers = {}
    k = int(sys.argv[3])
    for seq_id, sequence in reader:
        for i in range(0, len(sequence) - (k + 1)):
            kmer = sequence[i:(i + k)]

            if kmers.get(kmer) == None:
                kmers.setdefault(kmer, 0)
                kmers[kmer] = (seq_id, i)
            else:
                kmers[kmer] += (seq_id,i)
    #for key, value in kmers.items():
     #   print("{}: {}".format(key, kmers[key]))
        
        
    reader_2 = FASTAReader(open(sys.argv[2]))
    k = int(sys.argv[3])
   # count = 0
    for seq_id, sequence in reader_2:
        for i in range(0, len(sequence) - k + 1):
            kmer_2 = sequence[i:(i + k)]
            if kmers.get(kmer_2) == None:
               # count += 1
                continue
            else:
                #master_list.append((kmers[kmer_2], kmers, i, kmer_2))
                print(kmers.get(kmer_2), i, kmer_2)
                #instead of appending, define vars and print indiv
                #if count >10000:
                #    break

        
if __name__ == "__main__":
    main()