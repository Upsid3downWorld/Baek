import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M, K = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = [ ["."]*M for _ in range(N) ]

for i in range(K) :
  r, c = map(int,input().split())
  graph[r-1][c-1] = "#"

def DFS(x,y):
  global size
  size += 1
  visit[x][y] = 1
  for i in range(4):
    lx = x + dx[i] ; ly = y + dy[i]
    if 0<=lx<N and 0<=ly<M and graph[lx][ly] == "#" and visit[lx][ly]==0:
      DFS(lx,ly)


com = 0
visit = [[0]*M for _ in range(N)]

for i in range(N) :
  for j in range(M) :
    if graph[i][j] == "#" and not visit[i][j] :
      size = 0
      DFS(i,j)
      com = max(com,size)

print(com)
