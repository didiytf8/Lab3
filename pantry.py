class Ingredient:
    """Класс для хранения данных об одном продукте"""
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit  
        
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

class PantryManager:
    """Класс для управления всеми продуктами на складе"""
    def __init__(self):
        self.inventory = {} 

    def add_ingredient(self, name, quantity, unit):
        """Добавление продукта или увеличение его количества"""
        if quantity <= 0:
            raise ValueError("Количество для добавления должно быть больше нуля!")
            
        if name in self.inventory:
            
            if self.inventory[name].unit != unit:
                raise ValueError(f"Ошибка! {name} уже есть на складе в {self.inventory[name].unit}, а вы пытаетесь добавить в {unit}")
            self.inventory[name].quantity += quantity
        else:
           
            self.inventory[name] = Ingredient(name, quantity, unit)

    def remove_ingredient(self, name, quantity):
        """Списание продуктов (например, когда вы приготовили еду)"""
        if quantity <= 0:
            raise ValueError("Количество для списания должно быть больше нуля!")
            
        if name not in self.inventory:
            raise KeyError(f"Продукта '{name}' нет на складе!")
            
        if self.inventory[name].quantity < quantity:
            raise ValueError(f"Недостаточно {name}! На складе: {self.inventory[name].quantity}, просят списать: {quantity}")
            
        self.inventory[name].quantity -= quantity
        
    
        if self.inventory[name].quantity == 0:
            del self.inventory[name]

    def get_all_inventory(self):
        """Вывод всего списка продуктов"""
        return [str(item) for item in self.inventory.values()]
