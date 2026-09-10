import json
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent / "data" / "player.json"
DEFAULT_DATA = {"coin": 500, "items": {}}


def _load_data():
    FILE_PATH.parent.mkdir(exist_ok=True)
    if not FILE_PATH.exists():
        _save_data(DEFAULT_DATA.copy())

    with FILE_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    data.setdefault("coin", 500)
    data.setdefault("items", {})
    return data


def _save_data(data):
    FILE_PATH.parent.mkdir(exist_ok=True)
    with FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_coin():
    return _load_data()["coin"]


def add_coin(amount):
    data = _load_data()
    data["coin"] += amount
    _save_data(data)


def set_coin(amount):
    data = _load_data()
    data["coin"] = max(0, amount)
    _save_data(data)


def use_coin(amount):
    data = _load_data()
    if data["coin"] < amount:
        return False

    data["coin"] -= amount
    _save_data(data)
    return True


def add_item(item_name):
    data = _load_data()
    data["items"][item_name] = data["items"].get(item_name, 0) + 1
    _save_data(data)


def get_items():
    return _load_data()["items"]