# Game Center

## 프로젝트 구조

```text
PythonProject/
├── main.py                    # 프로그램 진입점과 전체 메뉴
├── common/                    # 로그인과 공통 설정
│   ├── __init__.py
│   ├── config.py
│   └── login_manager.py
├── games/                     # 게임 기능
│   ├── __init__.py
│   ├── baseball.py            # 숫자야구
│   ├── baskinrobins.py        # 배스킨라빈스 31
│   ├── cointoss.py            # 코인토스
│   └── rcp.py                # 가위바위보와 묵찌빠
├── player/                    # 플레이어 데이터와 코인 관리
│   ├── __init__.py
│   ├── data.py                # JSON 데이터 저장과 조회
│   └── coin_manager.py        # 코인과 아이템 관리
├── shopping/                  # 상점 기능
│   ├── __init__.py
│   └── shopping.py
└── data/
    └── player.json            # 플레이어 저장 데이터
```

## 실행

```bash
python main.py
```
