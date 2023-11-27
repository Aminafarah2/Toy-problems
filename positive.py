def exactly_two_positive(a, b, c):
    #initializing a variable to count the number of positive integers
    positive_count = 0
    # Check if 'a' is positive
    if a > 0:
        positive_count += 1
        # Check if 'b' is positive
    if b > 0:
        positive_count += 1
        # Check if 'c' is positive
    if c > 0:
        positive_count += 1
    # Return True if exactly two of the three integers are positive
    return positive_count == 2
#print(exactly_two_positive(2, 4, -3)) 
#print(exactly_two_positive(-14, -3, -4))  