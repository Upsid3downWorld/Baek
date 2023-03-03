c_score = 100  # 창영이의 기본점수
s_score = 100  # 상덕이의 기본점수

n = int(input()) # 게임을 할 횟수

for i in range(n) : # 횟수만큼 돌아가는 for 문
    c_dice, s_dice = map(int,input().split())
    if (c_dice > s_dice) : # 창영이의 주사위 눈의 수가 더 클 경우
        s_score -= c_dice  # 창영이의 주사위 눈의 수만큼 상덕이의 점수 감소
    elif (s_dice > c_dice) : # 상덕이의 주사위 눈의 수가 더 클 경우
        c_score -= s_dice  # 상덕이의 주사위 눈의 수만큼 창영이의 점수 감소
    else :
        continue # 두 명의 점수가 같을 경우 continue

print(c_score)
print(s_score)