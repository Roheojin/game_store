import random


class BaseballGame:
    def __init__(self):
        print("숫자야구 게임을 시작합니다! ")
        self.answer = random.sample(range(1, 10), 3)

    def user_guess(self):
        while True:
            value = input("3자리 숫자를 입력해 주세요: ")
            if len(value) == 3 and value.isdigit() and len(set(value)) == 3 and "0" not in value:
                return [int(number) for number in value]
            print("중복 없이 1부터 9까지의 숫자 3자리를 입력해주세요.")

    def compare(self):
        guess = self.user_guess()
        strikes = sum(user == answer for user, answer in zip(guess, self.answer))
        balls = sum(number in self.answer for number in guess) - strikes
        print(f"스트라이크: {strikes}, 볼: {balls}")
        return strikes, balls

    def play_game(self):
        while True:
            strikes, _ = self.compare()
            if strikes == 3:
                print("정답입니다.")
                break


baseball_game = BaseballGame
