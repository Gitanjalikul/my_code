'''
write a script to get all repeat sequences of specific length 'k' and also how may times this repeats 
are occuring in a given sequence. 
find out the most repeated k-mer with the number of time it is repeated.
'''

from Bio import SeqIO
records = list(SeqIO.parse('E:\my_programs\python_programs\dna2.fasta', 'fasta'))

k=7
repeates = {}
for record in records:
    sequence = str(record.seq)
    for i in range (len(sequence)-(k-1)):
        k_mer = sequence[i:i+k]
        if k_mer in repeates:
            repeates[k_mer] += 1
        else:
            repeates[k_mer] = 1

print(repeates)

max_value = max(repeates.values())
most_repeated_kmer = [k_mer for k_mer, count in repeates.items() if count == max_value]

print(f'The most repeated k_mer is {most_repeated_kmer} wih count {max_value}')