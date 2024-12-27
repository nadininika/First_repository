from address import Address


class Mailing:
    def __init__(
        self,
        to_address: Address,
        from_address: Address,
        cost: float,
        track: str,
    ):
        """Конструктор принимает адрес получателя, адрес отправителя,
        стоимость и трек-номер."""
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
