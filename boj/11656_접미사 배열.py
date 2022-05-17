'''
https://boj.kr/11656
'''
import sys

S = sys.stdin.readline().rstrip()
words = []

for i in range(len(S)):
    words.append(S[i:])

for word in sorted(words):
    print(word)