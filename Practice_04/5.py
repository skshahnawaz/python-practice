# Find nucleotide frequencies.
# Input: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Output: 
# A: 20, C: 12, G: 17, T: 21

def nucleotide_frequencies(sequence):
    frequencies = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in sequence:
        frequencies[nucleotide] += 1
    for key in frequencies.keys():
        print(key + ": " + str(frequencies[key]))

input_str = input("Enter a string: ")
nucleotide_frequencies(input_str)