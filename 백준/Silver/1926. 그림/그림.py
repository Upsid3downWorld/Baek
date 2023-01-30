from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

# 그림의 개수, 그림 중 가장 넓은 것의 넓이 출력
# 0과 1중 1만 그림(단, 가로와 세로로 이어진 것만 인정, 대각선은 떨어진 그림.) → 상하좌우 필요

dx = [-1,1,0,0] # 좌, 우, 상, 하
dy = [0,0,-1,1] # 좌, 우, 상, 하

cnt = 0 # 그림의 개수
aop = 0 # a(rea)o(f)p(aint) : 그림 중 가장 넓은 것의 넓이

def BFS(x,y) :
    deq = deque()
    deq.append([x,y])
    visit[x][y] = 1
    check = 1

    while deq:
        x,y = deq.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and graph[nx][ny] == 1 :
                visit[nx][ny] = 1
                check += 1
                deq.append([nx,ny])

    return check

graph = [list(map(int,input().split())) for _ in range(N) ]
visit = [ [0] * M for _ in range(N) ]

for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 1 and not visit[i][j] :
            aop = max(aop, BFS(i,j))
            cnt += 1

print(cnt, aop, sep ='\n')