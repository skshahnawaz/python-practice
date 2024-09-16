dna_seq = input("Enter a DNA sequence: ")
dna_seq = dna_seq.upper()

a_count = dna_seq.count('A')
c_count = dna_seq.count('C')
g_count = dna_seq.count('G')
t_count = dna_seq.count('T')

print(f"A: {a_count}, T: {t_count}, G: {g_count}, C: {c_count}")