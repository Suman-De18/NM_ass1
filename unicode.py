#List methods

S = 'mumbai'
unicode_list_method = []

for char in S:
    unicode_list_method.append(ord(char))

print("Using list methods:", unicode_list_method)

#List Comprehension
S = 'mumbai'
unicode_list_comp = [ord(char) for char in S]
print("Using list comprehension:", unicode_list_comp)

#Map Class
S = 'mumbai'
unicode_map_class = list(map(ord, S))
print("Using map class:", unicode_map_class)