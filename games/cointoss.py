import random

from player import CoinManager


WIN_REWARD = 20
LOSE_PENALTY = 10


class CoinToss:
    def __init__(self, coin_manager=None):
        self.coin_manager = coin_manager or CoinManager()
        self.result = None
        self.cointoss_win = 0
        self.cointoss_lose = 0

    def flip(self):
        while True:
            coin = self.coin_manager.get_coin()
            print("=" * 50)
            print("                    COIN TOSS")
            print("=" * 50)
            print(f"보유 코인 : {coin}개")
            print(f"맞히면 +{WIN_REWARD}코인 / 틀리면 -{LOSE_PENALTY}코인")

            if coin < LOSE_PENALTY:
                print("코인이 부족해서 더 이상 진행할 수 없습니다.")
                break

            user = input("앞, 뒤 중 하나를 선택하세요 (0 입력 시 초기 화면으로): ")
            if user == "0":
                break
            if user not in ["앞", "뒤"]:
                print("잘못된 입력입니다. '앞' 또는 '뒤'를 입력해주세요.")
                continue

            self.result = random.choice(["앞", "뒤"])
            if user == self.result:
                print(f"맞췄습니다! {self.result}")
                self.cointoss_win += 1
                self.coin_manager.add_coin(WIN_REWARD)
            else:
                print(f"틀렸습니다. 정답은 {self.result}입니다.")
                self.cointoss_lose += 1
                self.coin_manager.use_coin(LOSE_PENALTY)

            print(f"현재 기록: {self.cointoss_win}승 {self.cointoss_lose}패")
            print(f"보유 코인 : {self.coin_manager.get_coin()}개")
            print()
