#!/bin/bash

for SAMPLE in 09 11 23 24 27 31 35 39 62 63
do
    samtools sort -o ~/qbb2020-answers/week2/files/${SAMPLE}.bam -O bam ~/qbb2020-answers/week2/files/${SAMPLE}.sam

done