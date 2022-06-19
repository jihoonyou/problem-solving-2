import sys
input = sys.stdin.readline

n,k = map(int,input().split())

male_students = [0]*7
female_students = [0]*7

for _ in range(n):
    s,y = map(int,input().split())
    if s == 0:
        female_students[y]+=1
    else:
        male_students[y]+=1

count = 0
for student_cnt in female_students:
    count += (student_cnt // k)
    if student_cnt % k != 0:
        count += 1

for student_cnt in male_students:
    count += (student_cnt // k)
    if student_cnt % k != 0:
        count += 1

print(count)