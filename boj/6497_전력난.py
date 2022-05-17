import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

while True:
    m,n = map(int,input().split())
    if m == 0 and n == 0:
        break
    
    parents = list(range(m+1))
    
    edges = []
    for _ in range(n):
        x,y,z = map(int,input().split())
        edges.append((z,x,y))
    
    edges.sort()

    total_cost = 0
    saving_cost = 0
    for z,x,y in edges:
        total_cost += z
        if find(x) != find(y):
            saving_cost += z
            union(x,y)
    print(total_cost - saving_cost)