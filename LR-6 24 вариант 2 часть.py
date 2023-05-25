''' Лабораторная работа №6
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения. 
Вариант 24.
У няни неограниченное количество  фруктов К разных названий (ф1,…фК).
Сформировать (вывести) все возможные варианты меню полдника (1 фрукт) для ребенка на неделю
'''
# Ограничения на калорийность
# Программа выводит все возможные комбинации из 3 фруктов списка с их калорийностью 
# и находит комбинацию с самым большим количеством калорий.

fruits = {'ф1': 57, 'ф2': 89, 'ф3': 47, 'ф4': 40, 'ф5': 34, 'ф6': 52, 'ф7': 67, 'ф8': 85}

def get_combinations(fruits, size, combination, start):
    if size == 0:
        yield combination
        return
    for index in range(start, len(fruits)):
        fruit = list(fruits.keys())[index]
        new_combination = combination + [fruit]
        yield from get_combinations(fruits, size-1, new_combination, index+1)

# Получаем все возможные комбинации из 3 фруктов
combs = list(get_combinations(fruits, 3, [], 0))

# Создаем список с комбинациями и их калорийностью
calories_list = [(comb, sum([fruits[fruit] for fruit in comb])) for comb in combs]

# Сортируем список по убыванию калорийности
sorted_calories_list = sorted(calories_list, reverse=True, key=lambda x: x[1])  

# Выводим все комбинации и их калорийность
print("Все возможные комбинации и их калорийность:")
for comb, calories in sorted_calories_list:
    print(f"{', '.join(comb)} - {calories} калорий")

# Находим самую калорийную комбинацию
max_combination, max_calories = sorted_calories_list[0] 

print(f"\nСамая калорийная комбинация из 3 фруктов - {', '.join(max_combination)} с общей калорийностью {max_calories} калорий")
