from common import LoginManager
from coin_manager import get_coin, set_coin
from rcp import App as RCPApp
from shopping import shopping_app


def main():

    login_manager = LoginManager()

    user_id = login_manager.login()
    rcp_app = RCPApp()

    while True:

        print("="*50)
        print("                    GAME CENTER")
        print("="*50)
        print("1. 야구게임")
        print("2. 베스킨라빈스")
        print("3. 묵찌빠")
        print("4. 상점")
        print("5. 게임종료")

        try:
            menu_number = int(input("선택 : "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        print()

        if menu_number == 3:
            rcp_app.coin = get_coin()
            rcp_app.main_menu()
            set_coin(rcp_app.coin)
        elif menu_number == 4:
            shopping_app(user_id)
        elif menu_number == 5:
            print("로그아웃합니다.")
            break
        else:
            print("준비 중인 메뉴이거나 올바르지 않은 번호입니다.")


if __name__ == "__main__":
    main()