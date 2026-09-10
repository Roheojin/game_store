import random


class BaskinRobins31:

    coin = []

    def get_user_number(self):
        while True:
            user_number = input("3개 이하의 숫자를 입력해주세요 : ")
            x = user_number.split()

            clean_number = int(x[-1])

            if "31" in x:
                print("*** YOU LOSE ***")
                print("31을 말했습니다!")
                return

            clean_number = self.get_computer_number(clean_number)

            if clean_number >= 31:
                print("*** YOU WIN ***")
                print("컴퓨터가 31을 말했습니다!")

                self.coin.append(1)

                print("코인 1개를 획득했습니다!")
                print("현재 코인 :", self.coin)

                return


    def get_computer_number(self, clean_number):
        repeat = random.randint(1, 3)

        for i in range(1, repeat + 1):
            computer_number = clean_number + i
            print(computer_number, end=" ")

            if computer_number == 31:
                return 31

        print()

        return clean_number + repeat


game = BaskinRobins31()

print("=================")
print("배스킨라빈스 31 !")
print("=================")
print("31을 말하는 사람이 패배합니다 !")
print()

game.get_user_number()
