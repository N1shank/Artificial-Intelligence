# Travelling Salesman Problem

from sys import maxsize
e = 5

def travelling_salesman_function(graph, s):
    edge = []  
    for i in range(e):
        if i != s:
            edge.append(i)

    min_path = maxsize
    while True:
        current_cost = 0
        k = s
        for i in range(len(edge)):
            current_cost += graph[k][edge[i]]
            k = edge[i]
        current_cost += graph[k][s]
        min_path = min(min_path, current_cost)

        if not next_perm(edge):
            break
    return min_path


def next_perm(l):
    n = len(l)
    i = n-2

    while i >= 0 and l[i] > l[i+1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    left = i+1
    right = n-1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return True


graph = [[0,12,10,19,8], [12,0,3,7,6], [10,3,0,2,20], [19,7,2,0,4],[8,6,20,4,0]]
s = 0
path = travelling_salesman_function(graph, s)
print(graph)
print(path)