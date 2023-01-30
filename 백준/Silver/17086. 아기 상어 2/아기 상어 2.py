from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def BFS() :
    while deq:
        x,y = deq.popleft()
        for i in range(8) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and graph[nx][ny] == 0 :
                visit[nx][ny] = visit[x][y]+1
                deq.append([nx,ny])
    

N, M = map(int,input().split())
graph = [ list(map(int,input().split()) ) for _ in range(N) ]
visit = [ [0] * M for _ in range(N) ]
deq = deque()

for i in range(N) :
    for j in range(M) :
        if (graph[i][j] == 1) :
            deq.append([i,j])
            visit[i][j] = 1

BFS()
answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, visit[i][j]-1)

print(answer)