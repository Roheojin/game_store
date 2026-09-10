from common.config import TEST_ID, TEST_PASSWORD


class LoginManager:

    def __init__(self):
        self.current_user = None

    def login(self):
        print("=" * 50)
        print("                    LOGIN")
        print("=" * 50)

        while True:
            user_id = input("ID : ")
            password = input("Password : ")

            if user_id == TEST_ID and password == TEST_PASSWORD:
                self.current_user = user_id
                print()
                print("로그인 성공!")
                print(f"{user_id}님 환영합니다.")
                print()
                return self.current_user

            print("아이디 또는 비밀번호가 올바르지 않습니다.")
            print("다시 입력해주세요.")