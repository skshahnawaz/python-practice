def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def longest_palindromic_subsequence(s):
    """Find the longest palindromic subsequence."""
    longest = ""
    
    # Generate all subsequences
    for i in range(1, 1 << len(s)):  # This loops through all subsets
        subsequence = "".join(s[j] for j in range(len(s)) if (i & (1 << j)))
        
        if is_palindrome(subsequence) and len(subsequence) > len(longest):
            longest = subsequence
            
    return longest

# Example run for the input string "AAB"
example_string = "AAB"
result = longest_palindromic_subsequence(example_string)
print(result)
