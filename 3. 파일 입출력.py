import random
gamers = []
last = []
max_count = []

# 기존 파일 읽기 "r"
def read_file(gamers):
    

    with open("gamers.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(",")

    print_menu(gamers)
    

# 0. 메뉴 선택
def print_menu(gamers):
    while True:
        print("****** 메뉴 ******")
        print("1. 게임 선택")
        print("2. 랭킹 보기")
        print("3. 게임 종료")
        print()

        with open("gamers.txt","r",encoding="utf-8") as file:
            content = file.read()

        print(content)


        menu = int(input("숫자를 입력하세요 : "))
        if menu == 1:
            print_game()
        elif menu == 2:
            print_ranking()
        elif menu == 3:
            print_finish()
            return  

    
# 1. 게임 선택
def print_game():
    print()
    print("1. 로또")
    print("2. 업앤다운")

    game_choice = int(input("원하는 게임을 입력하세요 : "))
    if game_choice == 1:
        print_lotto_menu()
    elif game_choice == 2:
        print_level()


# 1-1. 로또
def print_lotto_menu():
    print("메뉴를 입력하세요")
    print("1. 추첨")
    print("2. 이력 보기")
    print("3. 종료")

    lotto_menu = int(input("숫자를 입력하세요 : "))
    if lotto_menu == 1:
        lotto_start()
    elif lotto_menu == 2:
        lotto_history()
    elif lotto_menu == 3:
        lotto_finish()

def lotto_start():
    print("추첨이 진행됩니다.")
    lotto_random()

def lotto_random():
    nums = []
    while len(nums) < 6:
        target = random.randint(1,45)
        if target not in nums:
            nums.append(target)
        else:
            continue
    nums.sort()
    print(nums)
    last.extend(nums)

def lotto_history():
    print("이력을 보여드립니다.")
    for i in range(30):
        if i % 6 == 0:
            print(*last[i:i+6 ])

def lotto_finish():
    print("종료되었습니다.")
    return


# 1-2. 업앤다운
def print_level():
    while True:
        print("난이도 선택 1.상 2.중 3.하")
        level = int(input("난이도를 선택하세요 : "))
        print()

        count = {1:5, 2:10, 3:15}
        max_count = count[level]        # 맥스카운트 = 레벨의 밸류값  ex. 5 = count[1]

        win_count = 0
        win = False         # 사용자 숫자 입력 전 : win = False 라고 가정한 상태
        random_num = random.randint(1, 100)
        print(max_count,"회 안에 맞춰보세요!")
        print(random_num)
        updown_start(max_count, random_num, win_count, win)
        return max_count, random_num

def print_count(win_count):
    print("누적 횟수 : ", win_count)
    print()

def updown_start(max_count, random_num, win_count, win):
        user_name = str(input("닉네임을 입력하세요 : "))
        while win_count < max_count:
            user_num = int(input("1부터 100까지 숫자를 입력하세요 : "))
            win_count += 1
            print(random_num)

            if user_num < random_num:
                print("UP !")
                print_count(win_count)

            elif user_num > random_num:
                print("DOWN !")
                print_count(win_count)

            else:
                win = True      # 사용자가 정답을 맞춘 후, 성공 상태로 변경
                print(win_count,"회 시도했습니다. 정답입니다!")
                update_ranking(user_name, win_count)
                print()
                return

        if win == False:        # 정답 맞추지 못하면, 그대로 실패 상태 
                                # if not win: 으로 작성해도 O
            print(win_count,"회 시도했습니다. 다시 도전하세요!")
            print()

        return user_name


def update_ranking(user_name, win_count):
    gamer = {"name":user_name, "count":win_count}   # 한 명을 저장하는 딕셔너리 생성
    gamers.append(gamer)

    with open("gamers.txt","a",encoding="utf-8")as file:
        file.write(f"{gamer["name"]},{gamer["count"]}\n")
    print(gamers)


# 2. 랭킹 보기
def print_ranking():
    print("------ 명예의 전당 ------")

    if len(gamers) == 0:
        print("아직 사용자 기록이 없습니다.")
        print()

    else:
        ranking_compare()

def ranking_compare():
    for i in range(len(gamers)):
        for j in range(i+1, len(gamers)):       # i=1이라면 j에서는 2부터 비교하겠다는 뜻
            if gamers[i]["count"] > gamers[j]["count"]:
                gamers[i], gamers[j] = gamers[j], gamers[i]     # 언패킹(자리 바꾸기)

        if len(gamers) > 3:
            for i in range(3):
                print(i+1,"등", gamer["name"]," ", gamer["count"],"회")

        else:
            for gamer in gamers:
                print("닉네임:", gamer["name"]," ", gamer["count"],"회")


# 3. 게임 종료
def print_finish():
    print("게임을 종료합니다.")

read_file(gamers)



