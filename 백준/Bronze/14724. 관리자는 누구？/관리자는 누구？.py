n = int(input())
# 각 동아리 별 학생 수 n

D = {'PROBRAIN' : 0, 'GROW' : 0, 'ARGOS' : 0,
    'ADMIN' : 0, 'ANT' : 0, 'MOTION' : 0,
    'SPG' : 0, 'COMON' : 0, 'ALMIGHTY' : 0}

admin_club = 'PROBRAIN'
admin_val = D[admin_club]

for i in D.keys(): 
    solved_list = list(map(int,input().split()))
    m = max(solved_list)
    D[i] = m
    if admin_val < m:
        admin_club = i
        admin_val = m

print(admin_club)