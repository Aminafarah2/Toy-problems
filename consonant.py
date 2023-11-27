def solve(word):
    # Define a string containing consonant characters
    consonant = 'bcdfghjklmnpqrstvwxyz'

    # Initialize an empty list to store substrings
    substrings = []
    # Initialize a variable to track the start index of the current substring
    start = 0

    # Iterate over each character in the input word
    for i in range(len(word)):
        # Check if the current character is a consonant
        if word[i] in consonant:
            # If it's the first character or the previous character was not a consonant,
            # update the start index of the current substring
            if i == 0 or word[i - 1] not in consonant:
                start = i
        else:
            # If the current character is not a consonant and the start index is less than the current index,
            # add the substring to the list
            if start < i:
                substrings.append(word[start:i])

    # If the last character is a consonant, add the remaining substring to the list
    if start < len(word):
        substrings.append(word[start:])

    # Initialize a dictionary to store substring values
    substring_values = {}
    # Calculate the value of each substring and store it in the dictionary
    for substring in substrings:
        substring_values[substring] = sum(ord(char) - ord('a') + 1 for char in substring)

    # Return the maximum value among the substring values
    return max(substring_values.values())

# Example usage
print(solve("zodiacs"))
