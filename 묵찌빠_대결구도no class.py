import random as rand

HAND_ART = {
    "묵": [
        "    _______   ",
        "---'   ____)  ",
        "      (_____) ",
        "      (_____) ",
        "      (____)  ",
        "---.__(___)   ",
    ],
    "찌": [
        "    _______     ",
        "---'   ____)____",
        "          ______)",
        "       __________)",
        "      (____)     ",
        "---.__(___)      ",
    ],
    "빠": [
        "     _______    ",
        "---'    ____)___",
        "           ______)",
        "          _______)",
        "         _______)",
        "---.__________)  ",
    ],
}

# 가위바위보 <-> 묵찌빠 이름 통일
HAND_ALIAS = {"바위": "묵", "가위": "찌", "보": "빠", "묵": "묵", "찌": "찌", "빠": "빠"}

MIRROR = str.maketrans("()<>/\\", ")(><\\/")


def _dw(s):
    # 한글은 두 칸으로 계산
    return sum(2 if "가" <= c <= "힣" or "ㄱ" <= c <= "ㆎ" else 1 for c in s)


def _center(s, width):
    space = max(0, width - _dw(s))
    left = space // 2
    return " " * left + s + " " * (space - left)


def show_vs(user, computer, attacker=""):
    """도전자 vs 컴퓨터 대결 구도를 그림으로 출력"""
    u = HAND_ALIAS.get(user)
    c = HAND_ALIAS.get(computer)
    if u is None or c is None:
        return

    left = [row[::-1].translate(MIRROR) for row in HAND_ART[c]]   # 컴퓨터는 좌우 반전
    right = HAND_ART[u]
    w = 18

    print()
    print("  " + "-" * 48)
    print("  " + _center("COMPUTER", w) + "    VS    " + _center("CHALLENGER", w))
    if attacker:
        print("  " + _center(attacker, 48))
    print("  " + "-" * 48)
    for l, r in zip(left, right):
        print("  " + l.rjust(w) + " " * 10 + r.ljust(w))
    print("  " + _center(c, w) + " " * 10 + _center(u, w))
    print("  " + "-" * 48)
    print()


# ============================================================

# 팀 비즈니스 - 가위바위보
choices = ["가위", "바위", "보"]
win = 0
lose = 0

def result(me, you):
    print()
    print(f"나 : {me} / 상대 : {you}")
    show_vs(me, you)
def rcp():
    global win, lose

    print()
    print("안 내면 진 거 가위바위보!")

    while True:

        me = input("뭘 낼까? : ")

        if me not in choices:
            print("가위/바위/보 중에서 입력하세요.")
            continue

        you = rand.choice(choices)

        if me == you:
            result(me, you)
            print("비겼습니다!")
            print("다시 선택하세요.")
            continue

        elif me == "가위" and you == "보":
            result(me, you)
            print("이겼다!")
            win += 1
            break

        elif me == "바위" and you == "가위":
            result(me, you)
            print("이겼다!")
            win += 1
            break

        elif me == "보" and you == "바위":
            result(me, you)
            print("이겼다!")
            win += 1
            break

        else:
            result(me, you)
            print("졌어...")
            lose += 1
            break

def main_menu():
    while True:
        main_menu_print()
        menu = input("Press Key : ")
        if menu == "1":
            print()
            game_menu()
        elif menu == "2":
            print()
            hist_menu()
        elif menu=="3":
            print("게임을 종료합니다")
            break
        else:
            print("정해진 메뉴를 입력하세요")
            

def main_menu_print():
    print("=======================메인 메뉴=======================")
    print("1. 게임 시작!")
    print("2. 기록 보기")
    print("3. 게임 종료")

def game_menu():
    while True:
        game_menu_print()
        menu = input("Press Key : ")
        if menu == "1":
            return rcp()
        elif menu == "2":
            return first_choice()
        else:
            break
        
def game_menu_print():
    print("=======================모드 선택=======================")
    print("1. 가위바위보")
    print("2. 묵찌빠")
    print("메인 화면으로 나가려면 1, 2 제외 아무 키나 입력하세요")

def hist_menu():
    while True:
        hist_menu_print()
        menu = input("Press Key : ")
        if menu == "1":
            return hist_rcp()
        elif menu == "2":
            return hist_rsp(win_hist,lose_hist)
        else:
            break

        
def hist_menu_print():
    print("====================================================")
    print("1. 가위바위보 기록 보기")
    print("2. 묵찌빠 기록 보기")
    print("메인 화면으로 나가려면 1, 2 제외 아무 키나 입력하세요")

def first_choice():
    list = ['가위', '바위', '보']
    while True:
        computer = rand.choice(list)
        user = input("안 내면 진 거 가위 바위 보!!(가위 바위 보 만 내세요) : ")
        print(f"도전자 : {user} / 컴퓨터 : {computer}")
        show_vs(user, computer, "[ 공격권 결정전 ]")
        print()
        if user not in list:
            print("패배!!!")
            break
        if user == computer:
            continue
        elif user == "가위" and computer=="보":
            return user_win_s()
        elif user == "가위" and computer=="바위":
            return user_lose_s()
        elif user == "바위" and computer=="보":
            return user_lose_r()
        elif user == "바위" and computer=="가위":
            return user_win_r()
        elif user == "보" and computer=="바위":
            return user_win_p()
        elif user == "보" and computer=="가위":
            return user_lose_p()

def user_win_s():
    count=0
    list = ["묵","찌","빠"]
    while True:
        computer = rand.choice(list)
        print("묵찌빠 중에 하나 입력")
        user = input("도전자 공격 : 찌 찌 ")
        print(computer)
        show_vs(user, computer, ">>> 도전자 공격 중 <<<")
        print()
        if user not in list:
            print("묵 찌 빠 중에 고르세요")
            continue
        count+=1
        if user == computer:
            win_hist.append((count,user))
            print("승리!!!")
            break
        elif user == "찌" and computer=="빠":
            continue
        elif user == "찌" and computer=="묵":
            return user_lose_s()
        elif user == "묵" and computer=="빠":
            return user_lose_r()
        elif user == "묵" and computer=="찌":
            return user_win_r()
        elif user == "빠" and computer=="묵":
            return user_win_p()
        elif user == "빠" and computer=="찌":
            return user_lose_p()


def user_win_p():
    count=0
    list = ["묵","찌","빠"]
    while True:
        computer = rand.choice(list)
        print("묵찌빠 중에 하나 입력")
        user = input("도전자 공격 : 빠 빠 ")
        print(computer)
        show_vs(user, computer, ">>> 도전자 공격 중 <<<")
        print()
        if user not in list:
            print("묵 찌 빠 중에 고르세요")
            continue
        count+=1
        if user == computer:
            win_hist.append((count,user))
            print("승리!!!")
            break
        elif user == "찌" and computer=="빠":
            return user_win_s()
        elif user == "찌" and computer=="묵":
            return user_lose_s()
        elif user == "묵" and computer=="빠":
            return user_lose_r()
        elif user == "묵" and computer=="찌":
            return user_win_r()
        elif user == "빠" and computer=="묵":
            continue
        elif user == "빠" and computer=="찌":
            return user_lose_p()



def user_win_r():
    count=0
    list = ["묵","찌","빠"]
    while True:
        computer = rand.choice(list)
        print("도전자 공격 : 묵찌빠 중에 하나 입력")
        user = input("묵 묵 ")
        print(computer)
        show_vs(user, computer, ">>> 도전자 공격 중 <<<")
        print()
        if user not in list:
            print("묵 찌 빠 중에 고르세요")
            continue
        count+=1
        if user == computer:
            win_hist.append((count,user))
            print("승리!!!")
            break
        elif user == "찌" and computer=="빠":
            return user_win_s()
        elif user == "찌" and computer=="묵":
            return user_lose_s()
        elif user == "묵" and computer=="빠":
            return user_lose_r()
        elif user == "묵" and computer=="찌":
            continue
        elif user == "빠" and computer=="묵":
            return user_win_p()
        elif user == "빠" and computer=="찌":
            return user_lose_p()

def user_lose_s():
    count=0
    list = ["묵","찌","빠"]
    while True:
        computer = rand.choice(list)
        print("묵찌빠 중에 하나 입력")
        user = input("컴퓨터 공격 : ")
        print("묵 묵",computer)
        show_vs(user, computer, "<<< 컴퓨터 공격 중 >>>")
        print()
        if user not in list:
            print("묵 찌 빠 중에 고르세요")
            continue
        count+=1
        if user == computer:
            lose_hist.append((count,user))
            print("패배...")
            break
        elif user == "찌" and computer=="빠":
            return user_win_s()
        elif user == "찌" and computer=="묵":
            continue
        elif user == "묵" and computer=="빠":
            return user_lose_r()
        elif user == "묵" and computer=="찌":
            return user_win_r()
        elif user == "빠" and computer=="묵":
            return user_win_p()
        elif user == "빠" and computer=="찌":
            return user_lose_p()


def user_lose_p():
    count=0
    list = ["묵","찌","빠"]
    while True:
        computer = rand.choice(list)
        print("묵찌빠 중에 하나 입력")
        user = input("컴퓨터 공격 : ")
        print("찌 찌",computer)
        show_vs(user, computer, "<<< 컴퓨터 공격 중 >>>")
        print()
        if user not in list:
            print("묵 찌 빠 중에 고르세요")
            continue
        count+=1
        if user == computer:
            lose_hist.append((count,user))
            print("패배...")
            break
        elif user == "찌" and computer=="빠":
            return user_win_s()
        elif user == "찌" and computer=="묵":
            return user_lose_s()
        elif user == "묵" and computer=="빠":
            return user_lose_r()
        elif user == "묵" and computer=="찌":
            return user_win_r()
        elif user == "빠" and computer=="묵":
            return user_win_p()
        elif user == "빠" and computer=="찌":
            continue



def user_lose_r():
    count=0
    list = ["묵","찌","빠"]
    while True:
        computer = rand.choice(list)
        print("묵찌빠 중에 하나 입력")
        user = input("컴퓨터 공격 : ")
        print("빠 빠",computer)
        show_vs(user, computer, "<<< 컴퓨터 공격 중 >>>")
        print()
        if user not in list:
            print("묵 찌 빠 중에 고르세요")
            continue
        count+=1
        if user == computer:
            lose_hist.append((count,user))
            print("패배...")
            break
        elif user == "찌" and computer=="빠":
            return user_win_s()
        elif user == "찌" and computer=="묵":
            return user_lose_s()
        elif user == "묵" and computer=="빠":
            continue
        elif user == "묵" and computer=="찌":
            return user_win_r()
        elif user == "빠" and computer=="묵":
            return user_win_p()
        elif user == "빠" and computer=="찌":
            return user_lose_p()


def hist_rsp(win_hist,lose_hist):
    print("===================묵찌빠 플레이 이력===================")
    print("승리 이력")
    for i in range(len(win_hist)):
        print(f"{win_hist[i][0]}번만에 {win_hist[i][1]} 내고 승리")
    print()
    print("패배 이력")
    for i in range(len(lose_hist)):
        print(f"{lose_hist[i][0]}번만에 {lose_hist[i][1]} 내고 패배")
    print()
    if len(lose_hist)==0 and len(win_hist)==0:
        return
    else:
        print(f"승률 : {len(win_hist)/(len(win_hist)+len(lose_hist))*100}%")
        if (len(win_hist)/(len(win_hist)+len(lose_hist)))*100 < 50:
            print("승률 50% 미만입니다. 컴퓨터에게 지다니 분발하세요.")



def hist_rcp():
    print()
    print("===================가위바위보 전적===================")
    print(f"현재 전적 : {win}승 {lose}패")

win_hist=[]
lose_hist=[]
main_menu()
