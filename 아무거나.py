gamers = []

with open("gamers.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    data = line.strip().split(",")

    gamer = {"name": data[0], "wrong_count": int(data[1])
    }

    gamers.append(gamer)
print(gamers)

# total = 0

# for gamer in gamers:
#     total += gamer["score"]

# average = total / len(gamers)

# print(f"평균 점수: {average:.1f}점")