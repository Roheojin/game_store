from player import CoinManager


SHOP_ITEMS = {
    "1": ("커피 교환권", 1000),
    "2": ("스낵바 이용권", 200),
}

class ShoppingApp:
    def __init__(self, user_id, coin_manager=None):
        self.user_id = user_id
        self.coin_manager = coin_manager or CoinManager()

    def run(self):
        while True:
            print("=" * 50)
            print("                    SHOPPING")
            print("=" * 50)
            print(f"보유 코인 : {self.coin_manager.get_coin()}개")
            print("1. 커피 교환권 - 1000코인")
            print("2. 스낵바 이용권 - 200코인")
            print("3. 보유 아이템 보기")
            print("4. 메인 메뉴")

            try:
                menu_number = int(input("선택 : "))
            except ValueError:
                print("숫자를 입력해주세요.")
                continue

            print()

            if str(menu_number) in SHOP_ITEMS:
                item_name, price = SHOP_ITEMS[str(menu_number)]
                if self.coin_manager.use_coin(price):
                    self.coin_manager.add_item(item_name)
                    print(f"{item_name}을(를) 구매했습니다.")
                    print(f"남은 코인 : {self.coin_manager.get_coin()}개")
                else:
                    print("코인이 부족합니다.")
            elif menu_number == 3:
                self.show_items()
            elif menu_number == 4:
                break
            else:
                print("올바르지 않은 번호입니다.")

    def show_items(self):
        items = self.coin_manager.get_items()
        print("보유 아이템")
        if not items:
            print("아직 구매한 아이템이 없습니다.")
            return

        for item_name, count in items.items():
            print(f"- {item_name} x{count}")

def shopping_app(user_id):
    return ShoppingApp(user_id).run()