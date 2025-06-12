# import tkinter as tk

# def click():
#     button.config(text="클릭됬어요!")
#     label.config(text="클릭완료")

# window = tk.Tk()
# window.title("닥또리")
# window.geometry("500x500+500+150")
# window.resizable(False,False)
# label=tk.Label(window,text="테스트",width=10,height=5)
# label.pack()
# button=tk.Button(window,text="버튼",width=10,height=3,command=click)
# button.pack()
# entry=tk.Entry(window)
# entry.pack()
# window.mainloop()

# import tkinter as tk

# def button_click():
#     label3.config(text=entry.get()+"님, "+entry2.get()+"세 시군요")

# window = tk.Tk()
# window.title("닥또리")
# window.geometry("500x300+500+150")
# label=tk.Label(window,text="이름을 입력하세요")
# label.place(x=10, y=10)
# label.grid(row=0,column=0)
# entry=tk.Entry(window)
# entry.place(x=10, y=30)
# label2=tk.Label(window,text="이름을 입력하세요")
# label2.place(x=10,y=50)
# entry2=tk.Entry(window)
# entry2.place(x=10, y=80)
# label3=tk.Label(window,text="")
# label3.place(x=150, y=110)
# button=tk.Button(window,text="버튼",padx=30,pady=15,command=button_click)
# button.place(x=250, y=10)
# window.mainloop()


# import tkinter as tk

# def button_click():
#     name1 = entry1.get()
#     name2 = entry2.get()
#     label3.config(text=f"{name1}랑 {name2}랑 사귄다 !")

# window = tk.Tk()
# window.title("닥또리")
# window.geometry("400x200+500+150")

# # 첫 번째 이름 입력
# label1 = tk.Label(window, text="이름1")
# label1.grid(row=0, column=0, padx=10, pady=5)
# entry1 = tk.Entry(window)
# entry1.grid(row=1, column=0, padx=10, pady=5)

# # 두 번째 이름 입력 (테스트)
# label2 = tk.Label(window, text="이름2")
# label2.grid(row=0, column=1, padx=10, pady=5)
# entry2 = tk.Entry(window)
# entry2.grid(row=1, column=1, padx=10, pady=5)

# # 버튼
# button = tk.Button(window, text="버튼", width=20, command=button_click)
# button.grid(row=2, column=0, columnspan=2, pady=10)

# # 결과 라벨
# label3 = tk.Label(window, text="")
# label3.grid(row=3, column=0, columnspan=2, pady=5)

# window.mainloop()


# # ##############################################
# # ##############################################
# # ##############################################
# # ######### 목 


a = [["a","b","멜론"],"오이","가지"]
len(a[0]) #(a,b,멜론)

print(len(a)) #a를 출력 