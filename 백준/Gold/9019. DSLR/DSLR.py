import sys
from collections import deque
input = sys.stdin.readline

cmds = ['D', 'S', 'L', 'R']

t = int(input())
for _ in range(t):
    a, b = map(int, input().rstrip().split())
    # a에서 b로 bfs하기
    visited = [0 for _ in range(10000)]
    dists = ['' for _ in range(10000)]
    visited[a] = 1
    q = deque()
    q.append((a))
    while q:
        num = q.popleft()
        if num == b:
            break
        # 갈 수 있는길
        # D => n을 2배로
        # S => n에서 1 빼기
        # L => 왼편으로 회전시키기
        # R => 오른편으로 회전시키기
        d_num = (num * 2) % 10000
        s_num = (num - 1) % 10000
        r1, r2, r3, r4 = num // 1000, num // 100 % 10, (num //
                                                        10) % 10, num % 10
        l_num = r2 * 1000 + r3 * 100 + r4 * 10 + r1
        r_num = r4 * 1000 + r1 * 100 + r2 * 10 + r3
        nums = (d_num, s_num, l_num, r_num)
        for n, cmd in zip(nums, cmds):
            if not visited[n]:
                dists[n] = dists[num] + cmd
                visited[n] = 1
                q.append(n)
    print(dists[b])
