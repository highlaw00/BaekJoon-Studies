import sys
sys.setrecursionlimit(100_000)

is_same = False

def quick_sort(A, B, p, r):
    if p < r:
        q = partition(A, B, p, r)
        quick_sort(A, B, p, q-1)
        quick_sort(A, B, q+1, r)

def partition(A, B, p, r):
    global answer
    x = A[r] # 기준 원소 선택
    i = p - 1 # i는 기준 원소보다 작거나 같은 원소들의 시작 지점
    for j in range(p, r):
        if (A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
            check_equality(A, B, i, j)
    if (i+1 != r):
        A[i+1], A[r] = A[r], A[i+1]
        check_equality(A, B, i+1, r)
    return i+1

def check_equality(A, B, i, j):
    global is_same, same_arr, same_cnt
    if is_same:
        return
    # 변경 후 동일한지 확인
    before_status_i = same_arr[i]
    before_status_j = same_arr[j]
    same_arr[i] = A[i] == B[i]
    same_arr[j] = A[j] == B[j]
    # i번째가 달라졌고, 이전이 True였다면, 
    if before_status_i == True and same_arr[i] == False:
        same_cnt -= 1
    elif before_status_i == False and same_arr[i] == True:
        same_cnt += 1
    
    if before_status_j == True and same_arr[j] == False:
        same_cnt -= 1
    elif before_status_j == False and same_arr[j] == True:
        same_cnt += 1
    
    if same_cnt == len(A):
        is_same = True
    
    

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
same_arr = [A[i] == B[i] for i in range(n)]
same_cnt = same_arr.count(True)
if same_cnt == n:
    is_same = True
quick_sort(A, B, 0, n-1)

if is_same:
    print(1)
else:
    print(0)