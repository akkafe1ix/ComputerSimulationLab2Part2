import numpy as np

# Метод Генератора
def generate_random_numbers(n, x0):
    random_numbers = []
    x = x0
    for i in range(n):
        x = (1 / np.pi) * np.arccos(np.cos((i + 100) * x))
        random_numbers.append(x)
    return random_numbers


# Параметры
n_small = 20
n_medium = 100
n_large = 1000
x0 = np.random.rand()  # Начальное значение

# Генерация случайных чисел
random_numbers_small = generate_random_numbers(n_small, x0)
random_numbers_medium = generate_random_numbers(n_medium, x0)
random_numbers_large = generate_random_numbers(n_large, x0)

# Статистическое исследование
def statistical_analysis(random_numbers):
    mean = np.mean(random_numbers)
    variance = np.var(random_numbers)
    std_dev = np.sqrt(variance)
    median=np.median(random_numbers)
    
    print(f"Среднее значение: {mean}, Дисперсия: {variance}, Стандартное отклонение: {std_dev}, Медиана: {median}")

    
#Вывод оценки 
print("ТРИГОНОМЕТРИЧЕСКИЙ ГЕНЕРАТОР СЧ:")
print("Малая выборка:")
statistical_analysis(random_numbers_small)
print("Средняя выборка:")
statistical_analysis(random_numbers_medium)
print("Большая выборка:")
statistical_analysis(random_numbers_large)
print("")
print("-----------------------------------------------------------------------------------------------")
print("")

# Метод рандомайза
def generate_random_numbers_geometric(n):
    random_numbers = []
    for i in range(n):
        x=np.random.geometric(0.5)/10
        random_numbers.append(x)
    return random_numbers

#Рандомайз случайных чисел
random_numbers_small = generate_random_numbers_geometric(n_small)
random_numbers_medium = generate_random_numbers_geometric(n_medium)
random_numbers_large = generate_random_numbers_geometric(n_large)

# Вывод оценки
print("ГЕОМЕТРИЧЕСКИЙ РАНДОМАЙЗЕР СЧ:")
print("Малая выборка:")
statistical_analysis(random_numbers_small)
print("Средняя выборка:")
statistical_analysis(random_numbers_medium)
print("Большая выборка:")
statistical_analysis(random_numbers_large)

