''' Лабораторная работа №6
Задание состоит из двух частей.  
1 часть – написать программу в соответствии со своим вариантом задания. 
Вариант 24.
У няни неограниченное количество  фруктов К разных названий (ф1,…фК).
Сформировать (вывести) все возможные варианты меню полдника (1 фрукт) для ребенка на неделю.
'''

num_fruits = int(input("Введите количество доступных фруктов: "))

if num_fruits == 0:
    print("Фруктов нет в наличии")
else:
    # Генерируем список всех доступных фруктов
    fruits = [f"ф{i+1}" for i in range(num_fruits)]

    # Создаем список списков для каждого дня недели
    week_fruits = [fruits] * 7

    def get_combinations(week_fruits, size, combination):
        if size == 0:
            yield combination
            return
        for fruit in week_fruits[0]:
            new_combination = combination + [fruit]
            yield from get_combinations(week_fruits[1:], size-1, new_combination)

    # Получаем все возможные комбинации фруктов заданного размера для каждого дня недели
    fruit_combinations = list(get_combinations(week_fruits, 7, []))
    
    for combination in fruit_combinations:
        print(combination)

