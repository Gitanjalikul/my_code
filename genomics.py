'''
write a python script to find out largest and smallest seq length and find out how many times
it is appearing in the given fasta file.
'''
from Bio import SeqIO
records = list(SeqIO.parse('E:\my_programs\python_programs\dna2.fasta', 'fasta'))
print(len(records))
#or
#seq_ = SeqIO.index('E:\my_programs\python_programs\dna.example.fasta', 'fasta')
#print('len of seq is', len(seq_))

#find len of all sequences
seq_len = []
for record in records:
    seq_len.append(len(record))
print(seq_len)

#find longest and shortest seq length
longest_seq_len = max(seq_len)
shortest_seq_len = min(seq_len)

#find Is there more than one longest or shortest sequence
longest_seq = 0
shortest_seq = 0
for record in records:
    if len(record) == longest_seq_len:
        longest_seq += 1
        print('id of longest seq is', record.id)
    elif len(record) == shortest_seq_len:
        shortest_seq += 1
        print('id of shortest seq is', record.id)

print('The largest seq length is:', longest_seq_len)
print('The shortest seq length is:', shortest_seq_len)

print(f"There are {shortest_seq} shortest sequences", )
print(f"There are {longest_seq} longest sequences", )




