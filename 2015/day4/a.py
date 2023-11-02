def is_nice_string(s):
    # Condition 1: At least three vowels
    vowels = "aeiou"
    vowel_count = sum(1 for char in s if char in vowels)
    if vowel_count < 3:
        return False

    # Condition 2: Contains a letter that appears twice in a row
    if not any(s[i] == s[i+1] for i in range(len(s) - 1)):
        return False

    # Condition 3: Does not contain "ab," "cd," "pq," or "xy"
    if any(substring in s for substring in ["ab", "cd", "pq", "xy"]):
        return False

    return True

def count_nice_strings_in_file(filename):
    nice_count = 0
    with open(filename, 'r') as file:
        for line in file:
            if is_nice_string(line.strip()):
                nice_count += 1
    return nice_count

# Example usage:
filename = "input.txt"  # Replace with the path to your text file
nice_count = count_nice_strings_in_file(filename)
print(f"Number of nice strings: {nice_count}")
    
