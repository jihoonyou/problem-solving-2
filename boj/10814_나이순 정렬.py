'''
https://boj.kr/10814
'''
import sys
input = sys.stdin.readline

N = int(input())

customers = []

for _ in range(N):
    customer_info = input().split()
    customers.append((int(customer_info[0]), customer_info[1]))

for customer_info in sorted(customers, key = lambda x : x[0]):
    print(customer_info[0], customer_info[1])
