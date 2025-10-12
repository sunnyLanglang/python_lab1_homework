with open('sequence.txt', 'r') as file:
    data = [float(line.strip()) for line in file if line.strip()]
filtered_data = [x for x in data if (5 <= x <= 10) or (-10 <= x <= -5)]
if not filtered_data:
    print("Нет данных в указанных диапазонах.")
    exit()
count_positive = len([x for x in filtered_data if 5 <= x <= 10])
count_negative = len([x for x in filtered_data if -10 <= x <= -5])
total = len(filtered_data)
percent_positive = (count_positive / total) * 100
percent_negative = (count_negative / total) * 100
print("=" * 50)
print("ПРОЦЕНТНОЕ СООТНОШЕНИЕ ЧИСЕЛ")
print("=" * 50)
print(f"Всего чисел в анализе: {total}")
print(f"Чисел от 5 до 10: {count_positive} ({percent_positive:.1f}%)")
print(f"Чисел от -5 до -10: {count_negative} ({percent_negative:.1f}%)")
print()
print("ТЕКСТОВАЯ ДИАГРАММА:")
print("Числа от 5 до 10:    ", "█" * int(percent_positive / 2), f"{percent_positive:.1f}%")
print("Числа от -5 до -10:  ", "█" * int(percent_negative / 2), f"{percent_negative:.1f}%")