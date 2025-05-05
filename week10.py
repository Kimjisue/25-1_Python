# # ##############################################
# # ##############################################
# # ##############################################
# # ######### 영상강의

# #파이썬 기준 
# # while --> 조건에 의해서 반복 
# # for --> 데이터 집합을 반복시킴 (리스트- 하나씩 꺼내서 반복함)

# list = ["세이코","카시오","시티즌","오리엔트","태그호이어"]

# for item in list:  #5번 반복 1-세이코, 2-카시오 3-시티즌 4-오리엔트 5-태그홍이어
#     print(item)

# list11 = [1,2,3,4,5,6,7,8,9]

# for abc in list11:
#     print(abc,"*","2=",abc*2)


# # ##############################################

# jp = ["세이코","카시오","시티즌","오리엔트"]
# usa = ["태그호이어","인빅타","타이맥스"]
# user=input("가지고 있는 시계: ")

# for item in jp: 
#     if user == item:
#         print("일본 시계 브랜드에요")
#     else:
#         print("일본 브랜드가 아니에요")

# ###사실은 이렇게도 가능 
# if user in jp:
#      print("일본 시계 브랜드에요")


# jp = ["세이코","카시오","시티즌","오리엔트"]
# color = ["빨강","파랑","노랑"]

# for a in jp:
#     for b in color:
#         print(b,a)


# # ##############################################
# jp = [1,2,3,4,5,6,7,8,9] #리스트 - 추가하거나 삭제할 수 있어요 
# color = [1,2,3,4,5,6,7,8,9]
# kr = [1,2,3,4,5,6,7,8,9]

# for num1 in jp:
#     for num2 in color:
#         print(num1,"X",num2,"=",num1*num2)

# for num1 in jp:
#     for num2 in color:
#         for num3 in kr:
#             print(num1,"X",num2,"X",num3,"=",num1*num2*num3)

# # ##############################################

# a=1
# b=1
# while a <10:
#     b=1
#     while b<10:
#         print(a,"X",b,"=",a*b)
#         b=b+1
#     a=a+1


# # ##############################################
# ####### range()

# for num1 in range(1,10):
#     print(num1,"X 2","=",num1*2)

# for num1 in range(1,10):
#     for num2 in range(1,10):
#         print(num1,"X",num2,"=",num1*num2) 


# one= int(input("첫번째 숫자: "))
# two = int(input("두번째 숫자: "))

# for num1 in range(1,one+1):
#     for num2 in range(1,two+1):
#         print(num1,"X",num2,"=",num1*num2) 


# for num1 in range(1,10,2):
#     for num2 in range(1,5,3):
#         print(num1,"X",num2,"=",num1*num2) 


# #######################################################
# one= int(input("첫번째 숫자: "))
# two = int(input("두번째 숫자: "))

# for num1 in range(1,one+1,two):
#     total = num1+total
#     print(num1,"누적",total) 

# ###거꾸로 가능 
# for num1 in range(10,1,-1):
#     total = num1+total
#     print(num1,"누적",total) 


#######################################################
#######################################################
#######################################################
###랜덤값 생성 
# import random 
# #random.seed("401")
# random.seed("닥또리")
# a=random.random() # --> 0.0~1.0 사이 랜덤값 컴퓨터는 랜덤값이라는걸 생성 못함 초기값을 이용해서 랜덤값 생성하는것임 
# b=random.random()
# print(a)    #int형 랜덤밗을 많이 씀 
# print(b)


#######################################################
# import random 
# c=random.randint(1,10)

# #c=random.randint(1,10,2) -> 이렇게도 사용 가능 
# print(c)

# #######################################################

# import random 
# c=random.randrange(1,4)
# print(c)

# if c==1:
#     print("묵")
# if c==2:
#     print("찌")
# if c==3:
#     print("빠")

import random 

win_user=0
win_comp=0

while True: 
   c=random.randrange(1,4)
   user=input("묵찌빠 하나 내세영: ")

   if user =="끝":
      print("프로그램을 종료합니다.")
      print("사람이 이긴 수 : ",win_user,"// 컴퓨터가 이긴 수 : ",win_comp)
      break

   if c==1:
      c="묵"
   if c==2:
      c="찌"
   if c==3:
      c="빠"

   print("사람: ",user, " // 컴퓨터: ",c)

   if user == c: 
      print("비겼어요")

   elif user == "묵":
      if c=="찌":
         print("사람이 이김")
         win_user = win_user+1
      if c=="빠":
         print("컴퓨터가 이김")
         win_comp = win_comp+1

   elif user == "빠":
      if c=="묵":
         print("사람이 이김")
         win_user = win_user+1
      if c=="찌":
         print("컴퓨터가 이김")
         win_comp = win_comp+1

   elif user == "찌":
      if c=="빠":
         print("사람이 이김")
         win_user = win_user+1
      if c=="묵":
         print("컴퓨터가 이김")
         win_comp = win_comp+1
   else:
      print("묵찌빠 중 하나만 입력하세요.")