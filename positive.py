def exactly_two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2
#print(exactly_two_positive(2, 4, -3)) 
#print(exactly_two_positive(-14, -3, -4))  