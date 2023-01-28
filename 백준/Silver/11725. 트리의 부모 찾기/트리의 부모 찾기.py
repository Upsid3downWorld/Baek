import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(node) :
    for i in Tree[node]:
        if dp[i] == 0 :
            dp[i] = node
            DFS(i)
    
N = int(input()) # 노드의 개수

Tree = [ [] for _ in range(N+1) ]

for i in range(N-1) : # 간선의 개수 = 정점의 개수 - 1
    a, b = map(int,input().split())
    Tree[a].append(b)
    Tree[b].append(a)

dp = [0] * (N+1)

DFS(1)

for i in range(2,len(dp)):
    print(dp[i], end = "\n")