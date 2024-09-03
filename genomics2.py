'''
for a given fasta file, find total number of possible ORFs in each sequence. find the length of largest
ORF along with its sequence id. mention the orf starting point inthat fasta sequence.
'''

from Bio import SeqIO
records = list(SeqIO.parse('E:\my_programs\python_programs\dna2.fasta', 'fasta'))
all_ORFs = []
longest_orf = ''
longest_orf_len = 0
longest_orf_id = ''
orf_starting_position = 0
for record in records:
    orfs = []
    for i in range(2,len(record.seq)-2):
        start_codon = record.seq[i:i+3]
        if start_codon == 'ATG':
            for x in range(i+3, len(record.seq)-2, 3):
                stop_codon = record.seq[x:x+3]
                if stop_codon == 'TAA' or stop_codon == 'TAG' or stop_codon == 'TGA':
                    orf_seq = record.seq[i:x+3]
                    orfs.append(orf_seq)  # append the sequence from start to stop codon
                    
                    if len(orf_seq) > longest_orf_len:
                        longest_orf = orf_seq
                        longest_orf_len = len(orf_seq)
                        longest_orf_id = record.id
                        orf_starting_position = i+1


    print(f"there are {len(orfs)} orfs available for {record.id} are", orfs, )
     # Append the found ORFs to the all_ORFs list
    all_ORFs.extend(orfs)

# Print the total number of ORFs found in all records
print(f"Total number of ORFs found: {len(all_ORFs)}")
print(f'length of longest ORF is {longest_orf_len}')
print(f'longest ORF belongs to {longest_orf_id}')
print(f'orf starting position in {longest_orf_id} is {orf_starting_position}')
