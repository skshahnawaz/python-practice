str = "AAAACCCGGT" # Store the DNA Sequence in a string

reversed_string = "" # Define a variable reversed_string to store the reverse of the dna sequence string
reverse_compliment_string = "" # Define a variable reverse_compliment_string to store the compliments of the reversed string

reversed_string = str[::-1] # Reverse the DNA sequence and store in reversed_string

# Iterate over all characters in the Reversed String
for chr in reversed_string:
    # Check if the current character is A, then replace it with T
    if (chr == "A"):
        reverse_compliment_string = reverse_compliment_string + "T"
    # Check if the current character is T, then replace it with A
    elif (chr == "T"):
        reverse_compliment_string = reverse_compliment_string + "A"
    # Check if the current character is G, then replace it with C
    elif (chr == "G"):
        reverse_compliment_string = reverse_compliment_string + "C"
    # Check if the current character is C, then replace it with G
    elif (chr == "C"):
        reverse_compliment_string = reverse_compliment_string + "G"

print(reverse_compliment_string) #Print the reverse compliment string