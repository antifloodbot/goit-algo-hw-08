import heapq
from typing import List

def minimize_cable_connection_cost(cable_lengths: List[int]) -> int:
    """
    Обчислює мінімальну загальну вартість з'єднання мережевих кабелів.
    Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин.

    :param cable_lengths: Список довжин мережевих кабелів.
    :return: Мінімальна загальна вартість з'єднання.
    """
    if not cable_lengths:
        return 0
    if len(cable_lengths) == 1:
        return 0 # Або cable_lengths[0] якщо вважати вартістю один кабель, але зазвичай 0

    # 1. Створюємо мінімальну купу з усіх довжин кабелів.
    # heapq.heapify перетворює список на купу "in-place".
    heapq.heapify(cable_lengths)

    total_cost = 0

    # 2. Повторюємо, доки в купі не залишиться один кабель
    while len(cable_lengths) > 1:
        # 3. Вилучаємо два найкоротші кабелі з купи.
        # heapq.heappop завжди вилучає найменший елемент у мін-купі.
        shortest1 = heapq.heappop(cable_lengths)
        shortest2 = heapq.heappop(cable_lengths)

        # 4. Обчислюємо вартість з'єднання цих двох кабелів.
        # Це сума їхніх довжин.
        connection_cost = shortest1 + shortest2
        total_cost += connection_cost

        # 5. Додаємо новий об'єднаний кабель (їхню суму) назад у купу.
        heapq.heappush(cable_lengths, connection_cost)

        print(f"Об'єднано кабелі довжиною {shortest1} і {shortest2}. Новий кабель: {connection_cost}. Поточна загальна вартість: {total_cost}")

    return total_cost

# Приклади використання:
# Example 1
cables1 = [4, 3, 2, 6]
min_cost1 = minimize_cable_connection_cost(cables1)
print(f"\nМінімальна загальна вартість з'єднання кабелів {cables1}: {min_cost1}")

# Example 2
cables2 = [1, 2, 3, 4, 5]
min_cost2 = minimize_cable_connection_cost(cables2)
print(f"\nМінімальна загальна вартість з'єднання кабелів {cables2}: {min_cost2}")

# Example 3 (відповідно до необов'язкового завдання, щоб показати що воно окреме)
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

# злиття K відсортованих списків
def merge_k_lists_optional(lists: List[List[int]]) -> List[int]:
    heap = []
    result = []

    for i, lst in enumerate(lists):
        if lst:
            # (value, list_index, element_index_in_list)
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        next_idx = element_idx + 1
        if next_idx < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][next_idx], list_idx, next_idx))
    return result

print(f"\n--- злиття K відсортованих списків ---")
merged_list = merge_k_lists_optional(lists)
print("Відсортований список:", merged_list)