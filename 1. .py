file=open("test.txt","w",encoding="utf-8")  # 열고 # w = 쓰기 모드
file.write("안녕하세요")    # 파일 안에 적는 것
file.close()    # 닫고(필수는 아님)

# open()은 파일을 여는 함수.
# "test.txt"는 파일 이름.
# "w"는 쓰기 모드 : 기존 파일을 덮어씀, 초기값
# encoding="utf-8"은 한글이 깨지지 않도록 설정.
# with를 사용하면 파일을 자동으로 닫아줍니다.

# 줄바꿈 = /n : file.write("/n안녕하세요")
# 데이터를 온전하게 뽑고싶으면 strip() 이용

with open("test.txt","w",encoding="utf-8")as file:
	file.write("1일차 학습\n")
	file.write("2일차 학습\n")
	file.write("3일차 학습\n")

# read : 터미널에 저장된 값이 보이는 것
with open("test.txt","r",encoding="utf-8")as file:
	content=file.read()
                        # 출력된 마지막 한 줄 빈 곳은 이스케이프 문자를 써서 그런 것
print(content)

# readline()
with open("test.txt","r",encoding="utf-8")as file:
	line1=file.readline()
	line2=file.readline()

print(line1)
print(line2)

# for문 사용해서 여러줄 뽑기
with open("test.txt","r",encoding="utf-8")as file:
	lines=file.readlines()     # 여기까지는 리스트가 나옴

print(lines)

for line in lines:  # 리스트 반복문
	print(line.strip()) # 띄어쓰기, 특수기호 없이 나옴

# 파일에 내용 추가 : for문을 돌리면 4일차도 보이지 않을까???
with open("test.txt","a",encoding="utf-8")as file:
	file.write("4일차 학습\n")

# 12. 여러 메모 계속 추가
while True:
	memo=input("메모를 입력하세요. 종료하려면 q 입력: ").strip()

	if memo.lower()=="q":   # while문 나가기
		break
	
	with open("memo.txt","a",encoding="utf-8")as file:
		file.write(memo+"\n")
	
	print("메모 저장이 완료되었습니다.")

# 13.
students= [
    {"name":"민수","score":85},
    {"name":"지수","score":92},
    {"name":"영희","score":55}
]

with open("students.txt","w",encoding="utf-8")as file:
	for student in students:
		file.write(f"{student['name']},{student['score']}\n")
		# 메모장에 저장되는건 문자로 저장됨
		# 숫자가 필요하면 int로 묶어야함
		
# 14.    
students = []

with open("students.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()    # 기존 데이터를 lines에 담는 (뽑기 위한 것)

for line in lines:
    data = line.strip().split(",") # 공백제거한 ["민수", "85"] 걸 data에 담는

    student = {
        "name": data[0],  # data에 있는걸 빼오는 것 -> {"name":"민수", "score":85}
        "score": int(data[1])}  # int로 숫자 변환

    students.append(student)

print(students)
# -> while문 안에 사용 가능

# 15.
def save_students(students, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for student in students:
            line = f"{student['name']},{student['score']}\n"
            file.write(line)

save_students(students, "test.txt")

# 19.
import os

d = os.getcwd() # 1번 방법
print(d)

print(os.getcwd())  # 2번 방법

# try-except 을 사용하면 있으면 있다, 없으면 하나 새로 만들까? 라고 해도 됨

# 누적 저장하는 부분에서는 a를 사용