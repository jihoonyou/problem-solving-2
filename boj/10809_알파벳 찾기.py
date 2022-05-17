''''
https://boj.kr/10809
'''
import sys
intput = sys.stdin.readline

S = input().rstrip()
ASCII_A = 97
alphabet_location = [-1]*26

for i, alphabet in enumerate(S):
    alphabet_idx = ord(alphabet) - ASCII_A
    if alphabet_location[alphabet_idx] == -1:
        alphabet_location[alphabet_idx] = i

print(" ".join(str(x) for x in alphabet_location))