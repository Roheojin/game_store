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

    left = [row[::-1].translate(MIRROR) for row in HAND_ART[c]]  # 컴퓨터는 좌우 반전
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

# 가위바위보
class RCP:
    def __init__(self):
        self.choices = ["가위", "바위", "보"]
        self.win = 0
        self.lose = 0

    def result(self, me, you):
        print()
        print(f"나 : {me} / 상대 : {you}")
        show_vs(me, you)

    def rcp(self):
        print()
        print("안 내면 진 거 가위바위보!")

        while True:

            me = input("가위 바위 보 중에서 입력하세요 : ")

            if me not in self.choices:
                print("가위/바위/보 중에서 입력하세요.")
                continue

            you = rand.choice(self.choices)

            if me == you:
                self.result(me, you)
                print("비겼습니다!")
                print("다시 선택하세요.")
                continue

            elif me == "가위" and you == "보":
                self.result(me, you)
                print("이겼다!")
                self.win += 1
                break

            elif me == "바위" and you == "가위":
                self.result(me, you)
                print("이겼다!")
                self.win += 1
                break

            elif me == "보" and you == "바위":
                self.result(me, you)
                print("이겼다!")
                self.win += 1
                break

            else:
                self.result(me, you)
                print("졌다...")
                self.lose += 1
                break

    def hist_rcp(self):
        print()
        print("===================가위바위보 전적===================")
        print(f"현재 전적 : {self.win}승 {self.lose}패")


class App:
    def __init__(self, coin=500):
        self.rcp_game = RCP()
        self.mzb_game = RockPaperScissors()
        self.coin = coin

    def main_menu(self):
        while True:
            self.main_menu_print()
            menu = input("Press Key : ")
            if menu == "1":
                print()
                self.game_menu()
            elif menu == "2":
                print()
                self.hist_menu()
            elif menu == "3":
                print("게임을 종료합니다")
                break
            else:
                print("정해진 메뉴를 입력하세요")

    def main_menu_print(self):
        print("=======================메인 메뉴=======================")
        print(f"보유 코인 : {self.coin}개")
        print("1. 게임 시작!")
        print("2. 기록 보기")
        print("3. 게임 종료")

    def game_menu(self):
        while True:
            self.game_menu_print()
            menu = input("Press Key : ")
            if menu == "1":
                previous_win = self.rcp_game.win
                previous_lose = self.rcp_game.lose
                result = self.rcp_game.rcp()
                self.coin += (self.rcp_game.win - previous_win) * 50
                self.coin -= (self.rcp_game.lose - previous_lose) * 20
                self.coin = max(50, self.coin)
                return result
            elif menu == "2":
                previous_wins = len(self.mzb_game.win_hist)
                previous_losses = len(self.mzb_game.lose_hist)
                result = self.mzb_game.first_choice()
                self.coin += (len(self.mzb_game.win_hist) - previous_wins) * 100
                self.coin -= (len(self.mzb_game.lose_hist) - previous_losses) * 30
                self.coin = max(50, self.coin)
                return result
            else:
                break

    def game_menu_print(self):
        print("=======================모드 선택=======================")
        print("1. 가위바위보")
        print("2. 묵찌빠")
        print("메인 화면으로 나가려면 1, 2 제외 아무 키나 입력하세요")

    def hist_menu(self):
        while True:
            self.hist_menu_print()
            menu = input("Press Key : ")
            if menu == "1":
                return self.rcp_game.hist_rcp()
            elif menu == "2":
                return self.mzb_game.hist_rsp(self.mzb_game.win_hist, self.mzb_game.lose_hist)
            else:
                break

    def hist_menu_print(self):
        print("====================================================")
        print("1. 가위바위보 기록 보기")
        print("2. 묵찌빠 기록 보기")
        print("메인 화면으로 나가려면 1, 2 제외 아무 키나 입력하세요")


class RockPaperScissors:
    def __init__(self):
        self.win_hist = []
        self.lose_hist = []

    def first_choice(self):
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
            elif user == "가위" and computer == "보":
                return self.user_win_s()
            elif user == "가위" and computer == "바위":
                return self.user_lose_s()
            elif user == "바위" and computer == "보":
                return self.user_lose_r()
            elif user == "바위" and computer == "가위":
                return self.user_win_r()
            elif user == "보" and computer == "바위":
                return self.user_win_p()
            elif user == "보" and computer == "가위":
                return self.user_lose_p()

    def user_win_s(self):
        count = 0
        list = ["묵", "찌", "빠"]
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
            count += 1
            if user == computer:
                self.win_hist.append((count, user))
                print("승리!!!")
                break
            elif user == "찌" and computer == "빠":
                continue
            elif user == "찌" and computer == "묵":
                return self.user_lose_s()
            elif user == "묵" and computer == "빠":
                return self.user_lose_r()
            elif user == "묵" and computer == "찌":
                return self.user_win_r()
            elif user == "빠" and computer == "묵":
                return self.user_win_p()
            elif user == "빠" and computer == "찌":
                return self.user_lose_p()

    def user_win_p(self):
        count = 0
        list = ["묵", "찌", "빠"]
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
            count += 1
            if user == computer:
                self.win_hist.append((count, user))
                print("승리!!!")
                break
            elif user == "찌" and computer == "빠":
                return self.user_win_s()
            elif user == "찌" and computer == "묵":
                return self.user_lose_s()
            elif user == "묵" and computer == "빠":
                return self.user_lose_r()
            elif user == "묵" and computer == "찌":
                return self.user_win_r()
            elif user == "빠" and computer == "묵":
                continue
            elif user == "빠" and computer == "찌":
                return self.user_lose_p()

    def user_win_r(self):
        count = 0
        list = ["묵", "찌", "빠"]
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
            count += 1
            if user == computer:
                self.win_hist.append((count, user))
                print("승리!!!")
                break
            elif user == "찌" and computer == "빠":
                return self.user_win_s()
            elif user == "찌" and computer == "묵":
                return self.user_lose_s()
            elif user == "묵" and computer == "빠":
                return self.user_lose_r()
            elif user == "묵" and computer == "찌":
                continue
            elif user == "빠" and computer == "묵":
                return self.user_win_p()
            elif user == "빠" and computer == "찌":
                return self.user_lose_p()

    def user_lose_s(self):
        count = 0
        list = ["묵", "찌", "빠"]
        while True:
            computer = rand.choice(list)
            print("묵찌빠 중에 하나 입력")
            user = input("컴퓨터 공격 : ")
            print("묵 묵", computer)
            show_vs(user, computer, "<<< 컴퓨터 공격 중 >>>")
            print()
            if user not in list:
                print("묵 찌 빠 중에 고르세요")
                continue
            count += 1
            if user == computer:
                self.lose_hist.append((count, user))
                print("패배...")
                break
            elif user == "찌" and computer == "빠":
                return self.user_win_s()
            elif user == "찌" and computer == "묵":
                continue
            elif user == "묵" and computer == "빠":
                return self.user_lose_r()
            elif user == "묵" and computer == "찌":
                return self.user_win_r()
            elif user == "빠" and computer == "묵":
                return self.user_win_p()
            elif user == "빠" and computer == "찌":
                return self.user_lose_p()

    def user_lose_p(self):
        count = 0
        list = ["묵", "찌", "빠"]
        while True:
            computer = rand.choice(list)
            print("묵찌빠 중에 하나 입력")
            user = input("컴퓨터 공격 : ")
            print("찌 찌", computer)
            show_vs(user, computer, "<<< 컴퓨터 공격 중 >>>")
            print()
            if user not in list:
                print("묵 찌 빠 중에 고르세요")
                continue
            count += 1
            if user == computer:
                self.lose_hist.append((count, user))
                print("패배...")
                break
            elif user == "찌" and computer == "빠":
                return self.user_win_s()
            elif user == "찌" and computer == "묵":
                return self.user_lose_s()
            elif user == "묵" and computer == "빠":
                return self.user_lose_r()
            elif user == "묵" and computer == "찌":
                return self.user_win_r()
            elif user == "빠" and computer == "묵":
                return self.user_win_p()
            elif user == "빠" and computer == "찌":
                continue

    def user_lose_r(self):
        count = 0
        list = ["묵", "찌", "빠"]
        while True:
            computer = rand.choice(list)
            print("묵찌빠 중에 하나 입력")
            user = input("컴퓨터 공격 : ")
            print("빠 빠", computer)
            show_vs(user, computer, "<<< 컴퓨터 공격 중 >>>")
            print()
            if user not in list:
                print("묵 찌 빠 중에 고르세요")
                continue
            count += 1
            if user == computer:
                self.lose_hist.append((count, user))
                print("패배...")
                break
            elif user == "찌" and computer == "빠":
                return self.user_win_s()
            elif user == "찌" and computer == "묵":
                return self.user_lose_s()
            elif user == "묵" and computer == "빠":
                continue
            elif user == "묵" and computer == "찌":
                return self.user_win_r()
            elif user == "빠" and computer == "묵":
                return self.user_win_p()
            elif user == "빠" and computer == "찌":
                return self.user_lose_p()

    def hist_rsp(self, win_hist, lose_hist):
        print("===================묵찌빠 플레이 이력===================")
        print("승리 이력")
        for i in range(len(win_hist)):
            print(f"{win_hist[i][0]}번만에 {win_hist[i][1]} 내고 승리")
        print()
        print("패배 이력")
        for i in range(len(lose_hist)):
            print(f"{lose_hist[i][0]}번만에 {lose_hist[i][1]} 내고 패배")
        print()
        if len(lose_hist) == 0 and len(win_hist) == 0:
            return
        else:
            print(f"승률 : {len(win_hist) / (len(win_hist) + len(lose_hist)) * 100}%")

    def calcul_coin(self, win, lose, coin=500):
        coin = coin + len(self.win_hist) * 100 - len(self.lose_hist) * 30 + win * 50 - lose * 20
        if coin <= 0:
            coin = 50
        return coin


if __name__ == "__main__":
    App().main_menu()