import sys
input = sys.stdin.readline

#15,28,19
e,s,m = map(int,input().split())
cur_e,cur_s,cur_m,junkyu_year = 1,1,1,1

while e != cur_e or s != cur_s or m != cur_m:
    cur_e = 1 if (cur_e + 1) % 16 == 0 else cur_e + 1
    cur_s = 1 if (cur_s + 1) % 29 == 0 else cur_s + 1
    cur_m = 1 if (cur_m + 1) % 20 == 0 else cur_m + 1 
    junkyu_year += 1

print(junkyu_year)