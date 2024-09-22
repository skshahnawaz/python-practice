dna_string = "GATGGAACTTGACTACGTAAATT" 

# Replacement Logic
# Replace G with C and C with G
# Replace A with U and T with A

rna_string = ""

for chr in dna_string:
    if (chr == "A"):
        rna_string = rna_string + "U"
    elif (chr == "G"):
        rna_string = rna_string + "C"
    elif (chr == "C"):
        rna_string = rna_string + "G"
    elif (chr == "T"):
        rna_string = rna_string + "A"

print(rna_string)