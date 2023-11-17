S = 'mumbai'
unicode_sum = 0

for char in S:
    unicode_sum += ord(char)

print(f"The sum of Unicode code points in '{S}' is: {unicode_sum}")