class Address:
    def __init__(self, postal_code, city, street, house, apartment):
        """Конструктор принимает индекс, город, улицу, дом и квартиру."""
        self.postal_code = postal_code
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
