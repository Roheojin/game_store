from common import LoginManager
from games import BaseballGame, BaskinRobinsGame, RCPApp
from player import CoinManager
from shopping import ShoppingApp


class GameCenter:
    def __init__(self):
        self.login_manager = LoginManager()
        self.coin_manager = CoinManager()
        self.rcp_app = RCPApp()
        self.user_id = None

    def run(self):
        self.user_id = self.login_manager.login()

        while True:
            self.show_menu()
            menu_number = self.read_menu_number()
            if menu_number is None:
                continue

            print()
            if menu_number == 1:
                baseball_game = BaseballGame(self.coin_manager.get_coin())
                baseball_game.play_game()
                self.coin_manager.set_coin(baseball_game.coin)
            elif menu_number == 2:
                BaskinRobinsGame().play()
            elif menu_number == 3:
                self.play_rcp()
            elif menu_number == 4:
                ShoppingApp(self.user_id, self.coin_manager).run()
            elif menu_number == 5:
                print("로그아웃합니다.")
                break
            else:
                print("준비 중인 메뉴이거나 올바르지 않은 번호입니다.")

    def show_menu(self):
        print("="*50)
        print("                    GAME CENTER")
        print("="*50)
        print("1. 야구게임")
        print("2. 베스킨라빈스")
        print("3. 묵찌빠")
        print("4. 상점")
        print("5. 게임종료")

    @staticmethod
    def read_menu_number():
        try:
            return int(input("선택 : "))
        except ValueError:
            print("숫자를 입력해주세요.")
            return None

    def play_rcp(self):
        self.rcp_app.coin = self.coin_manager.get_coin()
        self.rcp_app.main_menu()
        self.coin_manager.set_coin(self.rcp_app.coin)


def main():
    GameCenter().run()


if __name__ == "__main__":
    main()