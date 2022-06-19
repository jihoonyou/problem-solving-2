import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    freq = [0]*26
    str1,str2 = input().split()
    isPossible = True
    for c in str1:
        freq[ord(c) - ord('a')] += 1
    
    for c in str2:
        freq[ord(c) - ord('a')] -= 1

    for cnt in freq:
        if cnt != 0:
            isPossible = False
            break
    
    if isPossible:
        print('Possible')
    else:
        print('Impossible')
