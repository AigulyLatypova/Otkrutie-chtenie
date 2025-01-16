def read_recipes_from_file(file_path):
    """Читает рецепты из файла и возвращает словарь с рецептами."""
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            # Читаем название блюда
            recipe_name = lines[i].strip()
            if not recipe_name:  # Пропускаем пустые строки
                i += 1
                continue
            i += 1

            # Читаем количество ингредиентов
            if i < len(lines):
                num_ingredients_line = lines[i].strip()
                if num_ingredients_line.isdigit():
                    num_ingredients = int(num_ingredients_line)
                else:
                    print(f"Ошибка: количество ингредиентов для '{recipe_name}' не является числом.")
                    break  # Если количество ингредиентов не является числом, выходим
                i += 1

            # Читаем ингредиенты
            ingredients = []
            for _ in range(num_ingredients):
                if i < len(lines):
                    ingredient_line = lines[i].strip()
                    if ingredient_line:  # Проверка на пустую строку
                        ingredient_parts = ingredient_line.split('|')
                        if len(ingredient_parts) == 3:  # Проверка на корректное количество частей
                            ingredient_name = ingredient_parts[0].strip()
                            quantity = ingredient_parts[1].strip()
                            measure = ingredient_parts[2].strip()
                            ingredients.append({
                                'ingredient_name': ingredient_name,
                                'quantity': quantity,
                                'measure': measure
                            })
                        else:
                            print(f"Ошибка: некорректный формат ингредиента '{ingredient_line}' для '{recipe_name}'.")
                i += 1

            # Добавляем рецепт в словарь
            cook_book[recipe_name] = ingredients

    return cook_book


def print_cook_book(cook_book):
    """Выводит содержимое кулинарной книги в требуемом формате."""
    print("cook_book = {")
    for dish, ingredients in cook_book.items():
        print(f"  '{dish}': [")
        for ingredient in ingredients:
            print(
                f"    {{'ingredient_name': '{ingredient['ingredient_name']}', 'quantity': {ingredient['quantity']}, 'measure': '{ingredient['measure']}'}}{',' if ingredient != ingredients[-1] else ''}")
        print("    ],")
    print("}")


def main():
    file_path = 'C:\\Users\\Pc\\OneDrive\\Desktop\\PycharmProjects\\PythonProject\\files\\recipes.txt'  # Укажите путь к вашему файлу с рецептами
    cook_book = read_recipes_from_file(file_path)
    print_cook_book(cook_book)


if __name__ == "__main__":
    main()





