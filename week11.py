#확률형 게임 
# 1. 최초의 금액을 입금한다 
# 2. 토끼랑 거북이한테 현상금을 건다 
# 3. 내가 선택한 캐릭터가 이기면, 3배
# 4. 지면 현상금을 뺏긴다 
# 5. 무한 반복 
# -> 최초의 금액이 0원 이하이거나, 사용자가 끝이라고 입력할 때까지 

import random
import time

money = int(input("최초 금액을 입력하세요: "))

while money > 0:
    print(f"현재 보유 금액: {money}원")
    winner = input("배팅할 캐릭터를 선택하세요 (토끼/거북이), 또는 '끝' 입력 시 종료: ")
    if winner == "끝":
        print("게임을 종료합니다.")
        break

    if winner not in ["토끼", "거북이"]:
        print("잘못된 입력입니다. '토끼' 또는 '거북이' 중에서 선택하세요.")
        continue

    bet = int(input("배팅할 금액을 입력하세요: "))
    if bet > money:
        print("보유 금액보다 많이 배팅할 수 없습니다.")
        continue

    r = 0  # 토끼 위치
    t = 0  # 거북이 위치

    while True:
        print("\n" * 20)
        print("=" * 30)
        r_sleep = random.randint(1, 11)

        if r_sleep > 5:
            print(" " * r + "💤")  # 토끼는 잠
        else:
            print(" " * r + "🐰")
            r += 3

        print("-" * 50)
        print(" " * t + "🐢")
        print("=" * 30)
        t += 1
        time.sleep(0.4)

        if r > 53:
            print("🏁 토끼 승리!")
            if winner == "토끼":
                money += bet * 3 
                print(f"축하합니다! +{bet * 3}원 획득")
            else:
                money -= bet
                print(f"졌습니다. -{bet}원 회수")
            break
        elif t > 53:
            print("🏁 거북이 승리!")
            if winner == "거북이":
                money += bet * 3
                print(f"축하합니다! +{bet * 3}원 획득")
            else:
                money -= bet
                print(f"졌습니다. -{bet}원 회수")
            break

    if money <= 0:
        print("금액이 0원이 되어 게임을 종료합니다.")
        break