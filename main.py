def read_cook_book(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name: # Если строка пустая, выходим из цикла
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
    return cook_book

# Пример использования
file_path = 'files/recipes.txt' # Укажите путь к вашему файлу
cook_book = read_cook_book(file_path)
print(cook_book)





