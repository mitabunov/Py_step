from product import IProduct


class AlfredoSauce(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 90

    def __str__(self):
        return 'соус горчица'


class TomatoSauce(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 75

    def __str__(self):
        return 'соус кетчуп'


class MayoSauce(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 80

    def __str__(self):
        return 'соус майонезный'
