# Create a dictionary to store codon-to-amino acid mappings
codon_to_amino_acid = {
    "ACA": "Threonine",
    "AGA": "Arginine",
    "AGG": "Arginine",
    "AUC": "Isoleucine"
}

# Create a dictionary to count occurrences of each amino acid
amino_acid_count = {}

# Iterate through the codon_to_amino_acid dictionary and count amino acids
for codon, amino_acid in codon_to_amino_acid.items():
    if amino_acid in amino_acid_count:
        amino_acid_count[amino_acid] += 1
    else:
        amino_acid_count[amino_acid] = 1

# Find the amino acid with the highest count
most_frequent_amino_acid = max(amino_acid_count, key=amino_acid_count.get)
count = amino_acid_count[most_frequent_amino_acid]

# Output the result
print(f"{most_frequent_amino_acid} with {count} codons")
