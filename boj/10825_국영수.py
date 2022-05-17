'''
https://boj.kr/10825
'''
import sys
intput = sys.stdin.readline

N = int(input())
students = []

for _ in range(N):
    student_info = input().split()
    students.append((student_info[0], int(student_info[1]), int(student_info[2]), int(student_info[3])))

for student_info in sorted(students, key = lambda x : (-x[1],x[2],-x[3],x[0])):
    print(student_info[0])
