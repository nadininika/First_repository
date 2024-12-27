from address import Address
from mailing import Mailing

# Создаём адреса
from_address = Address(
    "123456",
    "Москва",
    "Ленинский проспект",
    "10",
    "15"
)
to_address = Address(
    "654321",
    "Санкт-Петербург",
    "Невский проспект",
    "20",
    "25"
)

# Создаём почтовое отправление
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350.75,
    track="AB123456789RU"
)

print(
    f"Отправление {mailing.track} из {mailing.from_address.postal_code}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.postal_code}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
