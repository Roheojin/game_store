from player.data import PlayerData


class CoinManager:
    """코인과 아이템 변경 규칙을 담당한다."""

    def __init__(self, player_data=None):
        self.player_data = player_data or PlayerData()

    def get_coin(self):
        return self.player_data.load()["coin"]

    def add_coin(self, amount):
        data = self.player_data.load()
        data["coin"] += amount
        self.player_data.save(data)

    def set_coin(self, amount):
        data = self.player_data.load()
        data["coin"] = max(0, amount)
        self.player_data.save(data)

    def use_coin(self, amount):
        data = self.player_data.load()
        if data["coin"] < amount:
            return False

        data["coin"] -= amount
        self.player_data.save(data)
        return True

    def add_item(self, item_name):
        data = self.player_data.load()
        data["items"][item_name] = data["items"].get(item_name, 0) + 1
        self.player_data.save(data)

    def get_items(self):
        return self.player_data.load()["items"]
