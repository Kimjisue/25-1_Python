# ### 월

# print("Hello World")

# ### 목 
# a = "a"
# b = "b"

# print(a, "+",b)

# #변수는 숫자, 문자, 소숫점 모두 다 넣을 수 있음 
# #연산 가능 
# print(10*10)

# #변수 2개에 정수를 각각 넣는다. 변수를 써서 사칙연산을 하고 그 결과를 출력하시오 
# x = 10
# y = 20

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# ## %는 나머지 값을 반환하는 것 
# # /는 나누기 
# # //는 몫 

# # 문자열 +는 가능 , 나머지는 다 불가능 
# # 문자열 * 정수는 가능 정수만큼 문자열 돌아감 
# # text*3 == text 3번 출력 


# text = "한동대학교"
# print(text)
# #"한" 출력 
# print(text[0])

# text = input("이름을 넣으세요: ") #input (사용자 입력 기다림)
# text2 = input("이름을 넣으세요: ") #input (사용자 입력 기다림)
# print(text,"랑", text2, "랑 사겨요")

#오류가 난다 안난다 ? 
#난다 
#a는 string 이기 때문에 "" 필요함 
#text = a
#print(text)


#input을 이용해서 나이랑 이름을 입력받으세요 
#누구누구님 몇살이군요 

text = input("이름을 넣으세요: ")
text2 = input("나이를 넣으세요: ")
print(text,"님", text2, "살 이군요")
print(text+"님"+text2+"살 이군요")

#input 으로 받은 값은 전부 문자로 인식됨 
text2 = int(input("나이를 넣으세요: "))
# -> 이렇게 int로 input을 감싸주면 문자에서 숫자로 바뀜 