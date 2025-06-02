# # ##############################################
# # ##############################################
# # ##############################################
# # ######### 월 

# 파일 입출력

# # n개의 글자 읽기
# inf = open('poem.txt', 'r')
# s = inf.read(7)
# print('read(7) = ', s)


# #줄에 있는 문장불러오기 
# inf = open('poem.txt', 'r')
# tts = inf.readlines()
# print(tts[4])


inf = open('poem.txt', 'r')
tts = inf.readlines()
a = 0
print(len(tts))
while a < len(tts):
    print(tts[a])
    a=a+1



#파일 입력 
# w를 사용하면 기존 파일에 덮어쓰기 
tt = open('test.txt','w')
tts=tt.write("hi")
tt.close()
