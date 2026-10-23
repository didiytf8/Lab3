
from main import Ingredient, PantryManager

def run_tests():
    print("=== ЗАПУСК ТЕСТОВОГО ДРАЙВЕРА ===")
    
    # --- (Happy Path) ---
    print("\n[1] Тестирование нормальной работы (Happy Path):")
    pantry = PantryManager()
    
    pantry.add_ingredient("Мука", 500.0, "г")
    pantry.add_ingredient("Яйца", 3.0, "шт")
    print(pantry.get_inventory())
    
    assert pantry.storage["Мука"].quantity == 500.0
    assert pantry.storage["Яйца"].quantity == 3.0
    print("-> Проверка добавления: УСПЕШНО")

    pantry.add_ingredient("Мука", 200.0, "г")
    assert pantry.storage["Мука"].quantity == 700.0
    print("-> Проверка суммирования: УСПЕШНО")

    pantry.remove_ingredient("Яйца", 1.0)
    assert pantry.storage["Яйца"].quantity == 2.0
    print("-> Проверка списания: УСПЕШНО")

    pantry.remove_ingredient("Яйца", 2.0)
    assert "Яйца" not in pantry.storage
    print("-> Проверка удаления при нуле: УСПЕШНО")

    # --- НЕГАТИВНЫЕ ТЕСТЫ ---
    print("\n[2] Негативное тестирование (Поиск багов):")

    try:
        print("Попытка списать 'Сахар' (которого нет)...")
        pantry.remove_ingredient("Сахар", 100)
    except ValueError as e:
        print(f"НАЙДЕН БАГ 1! Программа упала с ошибкой: {e}")

    try:
        print("\nПопытка списать 1000г Муки (а есть только 700г)...")
        pantry.remove_ingredient("Мука", 1000)
    except ValueError as e:
        print(f"НАЙДЕН БАГ 2! Программа упала с ошибкой: {e}")

    try:
        print("\nПопытка добавить -5г Соли...")
        pantry.add_ingredient("Соль", -5, "г")
    except ValueError as e:
        print(f"НАЙДЕН БАГ 3! Программа упала с ошибкой: {e}")

    try:
        print("\nПопытка добавить 'Много' грамм Соли...")
        pantry.add_ingredient("Соль", "Много", "г")
    except Exception as e:
        print(f"НАЙДЕН БАГ 4! Программа упала с системной ошибкой: {type(e).__name__} - {e}")

    print("\n=== ТЕСТИРОВАНИЕ ЗАВЕРШЕНО ===")

if __name__ == "__main__":
    run_tests()
