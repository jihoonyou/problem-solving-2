'''
https://boj.kr/10820
'''
import sys

for string in sys.stdin:
    lower_count = 0
    upper_count = 0
    digit_count = 0
    blank_count = 0

    for char in string:
        if 'a' <= char <= 'z':
            lower_count += 1
        elif 'A' <= char <= 'Z':
            upper_count += 1
        elif '0' <= char <= '9':
            digit_count += 1
        elif char == ' ':
            blank_count += 1
    # 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력
    print(lower_count, upper_count, digit_count, blank_count)
