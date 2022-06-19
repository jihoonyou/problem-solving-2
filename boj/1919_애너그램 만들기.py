import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

freq = [0]*26

for c in str1:
    freq[ord(c) - ord('a')] += 1

for c in str2:
    freq[ord(c) - ord('a')] -= 1

count = 0
for cnt in freq:
    if cnt != 0:
        count += abs(cnt)
print(count)
