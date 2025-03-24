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

country = input("나라를 입력하세요 : ")
city = input("도시를 입력하세요 : ")

if country == "일본":
    if city == "오사카":
        print("타코야끼")
    elif city == "삿포로":
        print("눈")
    else:
        print("그런건 없어")
elif country == "한국":
    if city == "대전":
        print("성심당")
    elif city == "포항":
        print("과메기")
    else:
        print("그런건 없어")
else:
    print("그런건 없음")