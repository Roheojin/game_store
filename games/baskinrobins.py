import random

from player import CoinManager


WIN_REWARD = 100
LOSE_PENALTY = 30


class BaskinRobinsGame:
    def __init__(self, coin_manager=None):
        self.coin_manager = coin_manager or CoinManager()

    def play(self):
        print("=================")
        print("배스킨라빈스 31 !")
        print("=================")
        print("31을 말하는 사람이 패배합니다 !")
        print()

        current_number = 0
        while current_number < 31:
            try:
                user_numbers = input("3개 이하의 숫자를 입력해주세요 : ").split()
                if not user_numbers or len(user_numbers) > 3:
                    raise ValueError
                numbers = [int(number) for number in user_numbers]
            except ValueError:
                print("1부터 이어지는 숫자를 3개 이하로 입력해주세요.")
                continue

            expected = list(range(current_number + 1, current_number + len(numbers) + 1))
            if numbers != expected:
                print("현재 숫자 다음부터 순서대로 입력해주세요.")
                continue

            current_number = numbers[-1]
            if current_number == 31:
                print("*** YOU LOSE ***")
                print("31을 말했습니다!")
                return self.finish(False)

            computer_count = min(random.randint(1, 3), 31 - current_number)
            computer_numbers = list(range(current_number + 1, current_number + computer_count + 1))
            print(" ".join(map(str, computer_numbers)))
            current_number = computer_numbers[-1]

            if current_number == 31:
                print("*** YOU WIN ***")
                print("컴퓨터가 31을 말했습니다!")
                return self.finish(True)

    def finish(self, won):
        if won:
            self.coin_manager.add_coin(WIN_REWARD)
            print(f"배스킨라빈스 승리 보상: +{WIN_REWARD}코인")
        else:
            if self.coin_manager.use_coin(LOSE_PENALTY):
                print(f"배스킨라빈스 패배 차감: -{LOSE_PENALTY}코인")
            else:
                print("코인이 부족해 패배 차감은 적용되지 않았습니다.")
        print(f"현재 코인: {self.coin_manager.get_coin()}개")
        return won


def get_user_number():
    return BaskinRobinsGame().play()