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


# inf = open('poem.txt', 'r')
# tts = inf.readlines()
# a = 0
# print(len(tts))
# while a < len(tts):
#     print(tts[a])
#     a=a+1



# #파일 입력 
# # w를 사용하면 기존 파일에 덮어쓰기 
# tt = open('test.txt','w')
# tts=tt.write("hi")
# tt.close()


# # ##############################################
# # ##############################################
# # ##############################################
# # ######### 목 

#일기장 
# 프로그램을 실행하면 두가지 옵션이 뜸 
# 1 읽기 
# 2. 쓰기 
# 1번을 누르면 일기장을 출력 
# 2번 누르면 쓸 수 있음 ( 한번에 한줄씩 쓴다 )

# 다 쓰고, 엔터 누르면 다시 초기화면으로 돌아가서 1번 쓰기 선택화면 

def read_diary(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            if content:
                print("\n--- 일기장 내용 ---")
                print(content)
            else:
                print("\n일기장이 비어 있습니다.")
    except FileNotFoundError:
        print("\n아직 일기장이 없습니다. 먼저 글을 작성해보세요.")

def write_diary(filename):
    line = input("\n일기 내용을 입력하세요 (한 줄씩 작성 후 Enter):\n")
    with open(filename, 'a') as f:
        f.write(line + '\n')
    print("작성 완료! 메인 메뉴로 돌아갑니다.")

def main():
    while True:
        diary_file = 'diary.txt'

        option = input("번호를 선택하세요(1:읽기, 2:쓰기, 3:종료): ")

        if option == '1':
            read_diary(diary_file)
        elif option == '2':
            write_diary(diary_file)
        elif option == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()