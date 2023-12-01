import threading

# Функция для вычисления факториала числа
def calculate_factorial(number, result_dict):
    result = 1
    for i in range(1, number + 1):
        result *= i
    result_dict[number] = result

# Число, для которого вы хотите вычислить факториал
number_to_calculate = 5

results = {}

threads = []

for i in range(number_to_calculate):
    thread = threading.Thread(target=calculate_factorial, args=(i + 1, results))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for number, factorial in results.items():
    print(f"Факториал {number} равен {factorial}")
