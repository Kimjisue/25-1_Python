######################################################
####월요일

# money = 50000
# if money >5000:
#     print("5000원 보다 많다영")
#     if money > 50000:
#         print("5만원 보다 많아영 ")
#         print("뭐먹지")
#         if money > 100000:
#             print("10만원보다 많아...???")
#             print("먹지마")


######################################################
# money = int(input("상상의 잔액 : "))

# if money > 1000:
#     if money > 100000000:
#         print("집을 산다. ")
#     elif money > 1500:
#         print("차를 산다.")
#     # elif money > 100000000:
#     #     print("집을 산다. ")
# elif money > 100:
#     if money > 500: 
#         print("노트북")
#     elif money > 150:
#         print("아이패드")
#     # elif money > 500: 
#     #     print("노트북")
# elif money > 10:
#     print("사지마")


######################################################
#나라 입력 받음 
#도시 입력 받음 
#나라랑, 도시를 입력 하면 그 도시의 특산물을 출력하기 
#나라랑 도시가 없는 경우 그런건 없어요 라고 출력하기 

# country = input("나라를 입력하세요 : ")
# city = input("도시를 입력하세요 : ")

# if country == "일본":
#     if city == "오사카":
#         print("타코야끼")
#     elif city == "삿포로":
#         print("눈")
#     else:
#         print("그런건 없어")
# elif country == "한국":
#     if city == "대전":
#         print("성심당")
#     elif city == "포항":
#         print("과메기")
#     else:
#         print("그런건 없어")
# else:
#     print("그런건 없음")



######################################################
#목요일 

# a = 11
# b = 22


# if a > 10 and b > 20:  #and , or 사용 가능 
#     print("프린트")

# 어장 관리기 
# 변수 3개 
#1번 - 키 t
#2번 - 매력 a
#3번 - 신실력 h 

#다중 if , 다중 조건을 써서 사귄다, 어장에 넣는다. 친구로 선을 긋는다. 무시한다 
# 입력값 3개 int(input)

# if t < 165 and a < 3 and h < 3:
#     print("무시한다")
# elif t >168 and t < 170 and a < 5 and h < 5:
#     print("친구로 선을 긋는다")
# elif t > 170 and t < 175 and a > 5  and a < 7 and h > 7:
#     print("어장에 넣는다.")
# elif t > 180 and t < 180 and a >= 10 and h >= 10:
#     print("사귄다.")

t= int(input("키 입력 : "))
a= int(input("매력 입력 : "))
h= int(input("신실력 입력 : "))

if t > 180 and h > 50:
    if a > 50: 
        print("사귄다")
    elif a > 30:
        print("어장에 넣는다.")
    elif a > 15: 
        print("친구로 선을 긋는다.")
    else:
        print("무시한다") 
elif t > 170 and a > 50:
    if h > 50: 
        print("사귄다")
    elif h > 30:
        print("어장에 넣는다.")
    elif h > 15: 
        print("친구로 선을 긋는다.")
    else:
        print("무시한다")


