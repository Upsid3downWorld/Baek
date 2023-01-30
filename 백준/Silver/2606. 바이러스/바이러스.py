import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

C = int(input()) # C(omputer) 컴퓨터의 수
P = int(input()) # P(air) 쌍의 수
cnt = 0          # c(ou)nt 방문 횟수

def DFS(node) :
    global cnt
    visit[node] = True
    for i in graph[node] :
        if not visit[i] :
            cnt += 1
            DFS(i)
    

graph = [ [] for _ in range(C+1) ]
visit = [False] * ( C + 1 )  # 방문 확인

for i in range(P) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(1)

print(cnt)
