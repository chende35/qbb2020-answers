#!/bin/bash

for SAMPLE in 09 11 23 24 27 31 35 39 62 63
do
    bwa mem -R "@RG\tID:${SAMPLE}\tSM:${SAMPLE}" -o ~/qbb2020-answers/week2/files/${SAMPLE}.sam ~/qbb2020-answers/week2/files/sacCer3.fa ~/qbb2020-answers/week2/files/A01_${SAMPLE}.fastq 
    
done