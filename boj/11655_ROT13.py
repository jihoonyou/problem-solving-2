'''
https://boj.kr/11655
'''
import sys
input = sys.stdin.readline
ROT13 = 13

S = input().rstrip()

for alphabet in S:
    alphabet_in_ascii = ord(alphabet)
    if alphabet_in_ascii < 65:
        print(alphabet, end='')
    elif alphabet_in_ascii <= 77:
        print(chr(alphabet_in_ascii + ROT13), end='')
    elif alphabet_in_ascii <= 90:
        print(chr(alphabet_in_ascii - ROT13), end='')
    elif alphabet_in_ascii < 97:
        print(alphabet, end='')
    elif alphabet_in_ascii <= 109:
        print(chr(alphabet_in_ascii + ROT13), end='')
    elif alphabet_in_ascii <= 122:
        print(chr(alphabet_in_ascii - ROT13), end='')
    else:
        print(alphabet, end='')
    