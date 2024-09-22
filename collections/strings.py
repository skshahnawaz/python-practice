str = "ATTAGCA" #initialise a string to store the DNA sequence

#take 4 variables which will store the counts of A,G,T,C 
count_a = 0
count_t = 0
count_g = 0
count_c = 0

# Iterate over all the characters in the DNA sequence
for chr in str:
    # For each character in the DNA sequence, check if it is A or T or G or C and accordingly increase the count
    if chr == "A":
        count_a = count_a + 1
    elif chr == "T":
        count_t = count_t + 1
    elif chr == "G":
        count_g = count_g + 1
    elif chr == "C":
        count_c = count_c + 1

# Print the total counts in the required format
print(f"A: {count_a}, T: {count_t}, G: {count_g}, C: {count_c}")