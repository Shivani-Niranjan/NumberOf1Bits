'''
Write a function that takes an integer and returns the number of 1 bits present in its binary representation.

Input
11

Output
3

Input
6

Output
2
'''

number = int(input())
count = 0

while number > 0:
    if number & 1:
        count += 1
    number >>= 1

print (count)
