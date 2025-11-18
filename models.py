from typing import List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация класса Product.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: List[Product] = None):
        """
        Инициализация класса Category.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов
        """
        self.name = name
        self.description = description
        self.products = products if products else []

        # Увеличиваем атрибуты класса
        Category.total_categories += 1
        Category.total_products += len(self.products)
