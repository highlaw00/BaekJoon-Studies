a_dmg, a_hp = map(int, input().split())
b_dmg, b_hp = map(int, input().split())

# 카드가 두 장 남았다면 비교
while a_hp > 0 and b_hp > 0:
    # 두 카드의 체력을 모두 상대의 공격력 만큼 차감
    a_hp -= b_dmg
    b_hp -= a_dmg

# a가 졌는지 b가 졌는지 비겼는지 확인
if a_hp <= 0 and b_hp <= 0:
    print("DRAW")
elif a_hp <= 0:
    print("PLAYER B")
else:
    print("PLAYER A")
