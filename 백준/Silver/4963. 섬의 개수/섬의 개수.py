import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**5)

dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]

def DFS(fx,fy) :

    visit[fx][fy] = True

    for v in range(8):
        lx = fx + dx[v] ; ly = fy + dy[v]

        if 0<=lx<h and 0<=ly<w and visit[lx][ly] == False and graph[lx][ly] == 1 :
            DFS(lx,ly)

while True:
    
    w,h = map(int,input().split())

    if (w==0) and (h==0) :
            break

    graph = [ list(map(int,input().split())) for _ in range(h) ]
    visit = [ [False]*w for _ in range(h) ]

    count = 0

    for i in range(h):
        for j in range(w):
            if visit[i][j] == False and graph[i][j] == 1 :
                DFS(i,j)
                count += 1

    print(count)