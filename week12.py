# # ## 컴퓨터가 5개의 숫자를 뽑음
# # ## 내가 숫자 5개를 입력함
# # ## 컴퓨터가 뽑은거랑 내가 뽑은게 몇 개가 일치하는지 확인

# # import random

# # list = []

# # while len(list) < 5:
# #     pick = random.randint(1, 45) 

# #     if pick in list:
# #         continue 
# #     else:
# #         list.append(pick) 

# #     list.sort() 

# # print(list) 

# # ## 숫자 뽑기 게임
# # ## 1~45 사이 숫자 5개 추출
# # ## 단, 중복이 있으면 안됨

# # ## 랜덤 값으로 숫자를 받음

# # ## append해서 리스트에 추가하면 됨
# # ## 조건 list의 개수가 5일 때 까지 반복함
# # ## 중복 체크

# # ## if 숫자 in list
# # ## 정렬해서 출력
 
# import random

# list = [] 
# user = [] 
# count = 0  


# while len(list) < 5:
#     pick = random.randint(1, 45)  

#     if pick in list:
#         continue 
#     else:
#         list.append(pick)  

#     list.sort()  


# while len(user) < 5:
#     a = int(input("숫자를 입력하세요! : "))  

#     if a in user:
#         print("이미 있는 숫자에요 다른 걸 입력하세요") 
#     else:
#         user.append(a) 


# for c in user:
#     if c in list:
#         count = count + 1  


# list.sort()
# user.sort()


# print("총", count, "개를 맞췄어요!")  
# print("컴퓨터가 만든 5개", list)  
# print("사용자가 만든 5개", user)  


# # ##############################################
# # ##############################################
# # ##############################################

 #리스트 3개를 만든다 
# 1-[과일]
# 2-[동물]
# 3-[숫자]

#각 리스트별로 넣고 싶은 것 넣으면 됨 
# 777 만들거임 
# 함수를 만들어서 777을 돌림
# 함수 안에서 리스트에 있는 것 각각 3개를 랜덤ㅁ으로 가져옴
# 함수 안에서 몇개를 맞췄는지 반환(return) 시킴
# 합수의 입력값은 아이콘이 들어있는 리스트


# import random 

# def game(sym):
#     sy1 = random.sample(sym,1)
#     sy2 = random.sample(sym,1)
#     sy3 = random.sample(sym,31)

#     print("|",sy1,sy2,sy3,"|")


# l1 = ["🍎","🍇","🍑","🍋"] 
# l2 = ["🐶","🐰","🐹","🐼"] 
# l3 = ["1️⃣","2️⃣","3️⃣","4️⃣"]


# while True:
#     input("땡길려면 엔터키")
#     game(l1)



## 주보 과제

def print_bulletin(date_str, title, hymns, order, announcements):
    print(f"=== 주보 ({date_str}) ===")
    print(f"예배 제목: {title}\n")
    print(">> 찬송가")
    for h in hymns:
        print("-", h)
    print("\n>> 예배 순서")
    for i, item in enumerate(order, 1):
        print(f"{i}. {item}")
    print("\n>> 공지사항")
    for a in announcements:
        print("-", a)

# 사용 예시
if __name__ == "__main__":
    print_bulletin(
        "2025년 5월 22일",
        "부활절 감사 예배",
        ["1장", "273장", "345장"],
        ["경배와 찬양", "기도", "성경봉독", "설교", "봉헌", "축도"],
        ["다음 주 청년부 수련회", "금요기도회 온라인 진행", "헌금 계좌 안내"]
    )
