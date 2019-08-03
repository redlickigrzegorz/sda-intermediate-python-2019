from heapq import heappush, heappop

if __name__ == '__main__':
    new_list = []
    heappush(new_list, (2, 3))
    heappush(new_list, (0, 6))
    heappush(new_list, (5, 5))
    heappush(new_list, (0, 5))
    print(heappop(new_list))
