import json
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent.parent / "data" / "player.json"
DEFAULT_DATA = {"coin": 500, "items": {}}


class PlayerData:
    """플레이어 데이터를 JSON 파일에 저장하고 읽는다."""

    def __init__(self, file_path=FILE_PATH):
        self.file_path = file_path

    def load(self):
        self.file_path.parent.mkdir(exist_ok=True)
        if not self.file_path.exists():
            self.save(DEFAULT_DATA.copy())

        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        data.setdefault("coin", 500)
        data.setdefault("items", {})
        return data

    def save(self, data):
        self.file_path.parent.mkdir(exist_ok=True)
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
