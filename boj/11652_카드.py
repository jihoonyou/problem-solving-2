'''
https://boj.kr/11652
'''
import sys
input = sys.stdin.readline

N = int(input())
max_cards = []
curr_max = None
card_count = {}

for _ in range(N):
    card = int(input())
    
    if curr_max is None:
        curr_max = 1
    
    if card not in card_count:
        card_count[card] = 1
    else:
        card_count[card]+= 1
    
    if card_count[card] > curr_max:
        curr_max = card_count[card]

for key, value in card_count.items():
    if value == curr_max:
        max_cards.append(key)

print(min(max_cards))