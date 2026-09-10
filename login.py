def login():
    user_id = input("아이디 : ")
    password = input("비밀번호 : ")

    if user_id == "admin" and password == "1234":
        print("로그인 성공!")
        return user_id

    print("로그인 실패")
    return None

import login

user_id = login.login()