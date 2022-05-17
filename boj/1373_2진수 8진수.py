'''
https://boj.kr/1373
'''
import sys

print(oct(int(sys.stdin.readline(),2))[2:])

# num = sys.stdin.readline().strip()
# result = ''
# count = 0
# while num:
#     count = 0
#     temp = 0
#     while count < 3 and num:
#         r = num % 10
#         num = num // 10
#         temp += r*(2**count)
#         count += 1
#     result = str(temp) + result
# print(result)