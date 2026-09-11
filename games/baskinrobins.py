import random


class BaskinRobinsGame:
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
                return

            computer_count = min(random.randint(1, 3), 31 - current_number)
            computer_numbers = list(range(current_number + 1, current_number + computer_count + 1))
            print(" ".join(map(str, computer_numbers)))
            current_number = computer_numbers[-1]

            if current_number == 31:
                print("*** YOU WIN ***")
                print("컴퓨터가 31을 말했습니다!")
                return


def get_user_number():
    return BaskinRobinsGame().play()
