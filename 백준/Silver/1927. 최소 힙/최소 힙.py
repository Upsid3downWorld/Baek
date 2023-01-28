import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

heap = []

for i in range(N) :
    x = int(input())

    if x != 0 :
        heapq.heappush(heap, x) # 배열 이름, 원소명

    else :
        if heap :
            print( heapq.heappop(heap) )
        else :
            print(0)
