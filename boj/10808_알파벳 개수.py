'''
https://boj.kr/10808
'''
import sys
input = sys.stdin.readline

S = input().rstrip()
ASCII_A = 97
alphabet_count = [0]*26

for alphabet in S:
    alphabet_count[ord(alphabet) - ASCII_A] += 1


print(" ".join(str(x) for x in alphabet_count))