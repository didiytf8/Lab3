
class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным!")
        self.name = name
        self.quantity = quantity
        self.unit = unit 

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"


class PantryManager:
    def __init__(self):
        self.storage = {}

    def add_ingredient(self, name: str, quantity: float, unit: str):
        """Добавление продукта на склад"""
        if quantity <= 0:
            raise ValueError("Количество для добавления должно быть больше нуля!")
            
        if name in self.storage:
            self.storage[name].quantity += quantity
        else:
            self.storage[name] = Ingredient(name, quantity, unit)

    def remove_ingredient(self, name: str, quantity: float):
        """Списание продукта со склада (например, когда приготовили еду)"""
        if name not in self.storage:
            raise ValueError(f"Продукта '{name}' нет на складе!")
        
        if quantity <= 0:
            raise ValueError("Списать можно только положительное количество!")

        if self.storage[name].quantity < quantity:
            raise ValueError(f"Недостаточно продукта '{name}'! На складе только {self.storage[name].quantity} {self.storage[name].unit}")
        
        self.storage[name].quantity -= quantity
        if self.storage[name].quantity == 0:
            del self.storage[name]

    def get_inventory(self):
        """Показать всё, что есть на складе"""
        if not self.storage:
            return "Склад пуст."
        
        result = "Текущий склад:\n"
        for ingredient in self.storage.values():
            result += f"- {ingredient}\n"
        return result.strip()
