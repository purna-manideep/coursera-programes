'''
In this assignment you will read through and parse a file with text and numbers.
You will extractall the numbers in the file and compute the sum of the numbers.
'''
import re

hand = open("regex_sum_437172.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)

