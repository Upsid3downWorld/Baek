import sys, heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())

heap = []

for i in range(N) :

    x = int(input())

    if x != 0 :
        heapq.heappush(heap, (-x,x))

    else :
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)