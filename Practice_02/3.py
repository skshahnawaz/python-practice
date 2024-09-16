dna_seq = input("Enter a DNA sequence: ")
dna_seq = dna_seq.upper()
dna_seq = dna_seq[::-1]
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
reverse_complement = ''
for nucleotide in dna_seq:
    reverse_complement += complement[nucleotide]
print(f'Reverse complement: {reverse_complement}')