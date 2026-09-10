# 31이 나오면 꽝
# 컴퓨터가 1~3개의 수를 말하고, 내가 1~3개의 수

import random
repeat = random.randint(1,3)
bomb = "31"

user_number = input("3개 이하의 숫자를 입력해주세요 : ")
x = user_number.split()

clean_number = int(x[-1])


for i in range(1, repeat + 1):
    print(clean_number + i, end="")


# def get_user_number():
#     while True:
#         user_number = input("3개 이하의 숫자를 입력해주세요 : ")
#         x = user_number.split()

#         clean_number = int(x[-1])
#         print(clean_number)

#         get_computer_number(clean_number)


# # def get_computer_number(clean_number):
# #     if repeat == 1:
# #         print(clean_number+1)

# #     if repeat == 2:
# #         print(clean_number+1, clean_number+2)

# #     if repeat == 3:
# #         print(clean_number+1, clean_number+2, clean_number+3)

# def get_computer_number(clean_number):
#     for i in range(1, repeat + 1):
#         print(clean_number + i)


# # def game_end():
# #     if "31" in user_number:
# #         print("*** YOU LOSE ***")
# #         print(" 31을 말했습니다!")

# #     elif "31" in compu



#     # for i in range(3):
#     #      if repeat == i:
#     #           print("나는 ")
#     #           print(clean_number+i, end="")






# print("배스킨라빈스 31 !")
# get_user_number()


    



#     # if len(x) == 1:
#     #     computer()

#     # elif len(raw_number) == 2:
#     #     print(int(raw_number[-1])+1)

#     # elif len(raw_number) == 3:
#     #     print(int(raw_number[-1])+1,)



# # x = "21 22"
# # raw_number = x.split()
# # if len(raw_number) == 2:
# #     print(int(raw_number[-1])+1)
