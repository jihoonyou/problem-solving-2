import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

res = a*b*c
freq = [0]*10

while res:
    digit = res % 10
    freq[digit] += 1
    res //= 10 

for n in freq:
    print(n)