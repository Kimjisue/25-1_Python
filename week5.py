#######################
####월요일

#숫자 입력 
# score = int(input("숫자를 입력하세요 : "))

# if score <= 90 and score >= 100:
#     print("A")
# elif score <= 89 and score >= 80:
#     print("B")
# elif score <= 79 and score >= 70:
#     print("C")
# elif score <= 69 and score >= 60:
#     print("D")
# elif score <=59:
#     print("F")


#양의 정수를 입력 받아 아래와 같이 출력 
#0보다 작거나 같으면 : 입력 오류 
#2의 배수이면 2의 배수 
#5의 배수이면 5의 배수 
#2의 배수이면서 5의 배수이면 2,5의 공배수 

num = int(input("양의 정수를 입력하세요 : "))
if num <= 0:
    print("입력오류")
elif num % 2 == 0 and num % 5 == 0:
    print("2와 5의 공배수")
elif num % 2 == 0:
    print("2의 배수")
elif num % 5 == 0:
    print("5의 배수")
