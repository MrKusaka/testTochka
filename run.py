import json


def check_capacity(max_capacity: int, guests: list) -> bool:
    events = []

    # Собираем события въезда(1) и выезда(-1) в один список
    for guest in guests:
        events.append((guest['check-in'], 1))
        events.append((guest['check-out'], -1))

    # Сортируем события сначала по дате, затем по типу события (выезд перед заездом)
    events.sort(key=lambda x: (x[0], x[1]))
    print(events)

    current_guests = 0

    # Обрабатываем события
    for event in events:
        current_guests += event[1]  # Увеличиваем или уменьшаем количество гостей
        print(current_guests)
        if current_guests > max_capacity:  # Проверяем превышение вместимости
            return False

    return True


if __name__ == "__main__":
    # Чтение входных данных
    # Первая строка - вместимость гостиницы
    max_capacity = int(input())
    # Вторая строка - количество записей о гостях
    n = int(input())

    guests = []
    # Читаем n строк, json-данные о посещении.
    for _ in range(n):
        guest = json.loads(input())
        guests.append(guest)

    # Вызов функции
    result = check_capacity(max_capacity, guests)
    # Вывод результата
    print(result)