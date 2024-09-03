'''
find out the length of each sequence present in the given fasta file. find the length of largets and 
smallest sequence and how may time it has appeared.
'''

from Bio import SeqIO
class Genome:
    def __init__(self, input_file):
        self.input_file = input_file
        self.my_list = []

    def len_list(self):
        seq = SeqIO.parse(self.input_file, 'fasta')
        self.my_list = []
        for self.record in seq:
            self.my_list.append(len(self.record.seq))
        print(self.my_list)

    def get_largest_seq(self):
        largest_seq = max(self.my_list)
        no_largest = self.my_list.count(largest_seq)
        print('The largest seq length is,', largest_seq)
        print(f'the largest seq has accured {no_largest} times')

    def get_smallest_seq(self):
        smallest_seq = min(self.my_list)
        no_smallest_seq = self.my_list.count(smallest_seq)
        print('The smallest seq length is,', smallest_seq)
        print(f'the smallest seq has accured {no_smallest_seq} times')

obj = Genome('E:\my_programs\python_programs\dna.example.fasta')
obj.len_list()
obj.get_largest_seq()
obj.get_smallest_seq()
