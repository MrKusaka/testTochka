import sys

import collections


# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]


def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]


def min_steps_to_collect_all_keys(grid):
    """Определяет минимальное количество шагов для сбора всех ключей."""
    start_positions = []
    all_keys = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                start_positions.append((i, j))
            elif grid[i][j] in keys_char:
                all_keys.add(grid[i][j])

    total_keys = len(all_keys)

    # Направление движения роботов: вверх, вниз, влево, вправо
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = set()
    queue = collections.deque()

    initial_pos = tuple(start_positions)
    initial_keys = frozenset()
    queue.append((initial_pos, initial_keys, 0))
    visited.add((initial_pos, initial_keys))

    while queue:
        positions, keys, steps = queue.popleft()

        if len(keys) == total_keys:
            return steps

        for i in range(len(positions)):
            x0, y0 = positions[i] # текущие координаты

            for x, y in directions:
                xn, yn = x0 + x, y0 + y # координаты после шага

                if 0 <= xn < len(grid) and 0 <= yn < len(grid[0]) and grid[xn][yn] != '#':
                    cell = grid[xn][yn]

                    if cell in doors_char and cell.lower() not in keys:
                        continue

                    # новая позиция робота
                    new_positions = list(positions)
                    new_positions[i] = (xn, yn)
                    new_positions = tuple(new_positions)

                    new_keys = set(keys)

                    if cell.islower():
                        new_keys.add(cell)

                    new_keys = frozenset(new_keys)

                    state = (new_positions, new_keys)
                    if state not in visited:
                        visited.add(state)
                        queue.append((new_positions, new_keys, steps + 1))
    return -1


def solve(data):
    return min_steps_to_collect_all_keys(data)


def main():
    data = get_input()
    result = solve(data)
    print(result)


if __name__ == '__main__':
    main()

