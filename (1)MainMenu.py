class MainMenu():
    def __init__(self):
        pass
    def main_menu(self):
        while True:
            print()
            print("1. 게임 선택")
            print("2. 랭킹 보기")
            print("3. 게임 종료")
            print()

            menu = int(input("숫자를 입력하세요 : "))
            print()

            if menu == 1:
                app.select_game()
            elif menu == 2:
                app.show_ranking(gamers)
            elif menu == 3:
                print("게임을 종료합니다.")
                break
