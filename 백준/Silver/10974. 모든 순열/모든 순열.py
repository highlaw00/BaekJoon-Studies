from itertools import permutations

n = int(input())

lis = [i for i in range(1, n + 1)]

perm = permutations(lis, n)

for elem in perm:
    string = " ".join(map(str, elem))
    print(string)
