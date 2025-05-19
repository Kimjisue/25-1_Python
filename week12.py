# ## 컴퓨터가 5개의 숫자를 뽑음
# ## 내가 숫자 5개를 입력함
# ## 컴퓨터가 뽑은거랑 내가 뽑은게 몇 개가 일치하는지 확인

# import random

# list = []

# while len(list) < 5:
#     pick = random.randint(1, 45) 

#     if pick in list:
#         continue 
#     else:
#         list.append(pick) 

#     list.sort() 

# print(list) 

# ## 숫자 뽑기 게임
# ## 1~45 사이 숫자 5개 추출
# ## 단, 중복이 있으면 안됨

# ## 랜덤 값으로 숫자를 받음

# ## append해서 리스트에 추가하면 됨
# ## 조건 list의 개수가 5일 때 까지 반복함
# ## 중복 체크

# ## if 숫자 in list
# ## 정렬해서 출력
 
import random

list = [] 
user = [] 
count = 0  


while len(list) < 5:
    pick = random.randint(1, 45)  

    if pick in list:
        continue 
    else:
        list.append(pick)  

    list.sort()  


while len(user) < 5:
    a = int(input("숫자를 입력하세요! : "))  

    if a in user:
        print("이미 있는 숫자에요 다른 걸 입력하세요") 
    else:
        user.append(a) 


for c in user:
    if c in list:
        count = count + 1  


list.sort()
user.sort()


print("총", count, "개를 맞췄어요!")  
print("컴퓨터가 만든 5개", list)  
print("사용자가 만든 5개", user)  


 

 

