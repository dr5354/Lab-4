def optimize_backpack(items, capacity, required_items, ground_score):

    items_copy = items.copy()

    backpack = []
    for item in required_items:
        if item in items_copy:
            weight, value = items_copy[item]
            if capacity >= weight:
                backpack.append(item)
                capacity -= weight
                del items_copy[item]
            else:

                return None


    items_copy = sorted(items_copy.items(), key=lambda x: x[1][1] / x[1][0], reverse=True)

    for item, (weight, value) in items_copy:
        if capacity >= weight:
            backpack.append(item)
            capacity -= weight
    total_value = ground_score
    total_value += sum(items[item][1] for item in backpack)
    total_value -= sum(items[item][1] for item in items if item not in backpack and item not in required_items)

    backpack_array = [[''] * columns for _ in range(rows)]
    row = 0
    col = 0
    for item in backpack:
        for i in range(items[item][0]):
            backpack_array[row][col] = item
            col += 1
            if col == columns:
                col = 0
                row += 1

    return backpack_array, total_value

columns = 2
rows = 4
ground_score = 10
items = {'r': [3, 25],
         'p': [2, 15],
         'a': [2, 15],
         'm': [2, 20],
         'i': [1, 5],
         'k': [1, 15],
         'x': [3, 20],
         't': [1, 25],
         'f': [1, 15],
         'd': [1, 10],
         's': [2, 20],
         'c': [2, 20]

}
capacity = columns * rows
required_items = ['d']
additional_capacity = 7

if __name__=='__main__':
    backpack, total_value = optimize_backpack(items, capacity, required_items, ground_score)
    print("Задание1")
    print("Итоговые очки выживания:", total_value)
    for row in backpack:
        print(", ".join(str(item) for item in row))

    backpack2, total_value = optimize_backpack(items, additional_capacity, required_items, ground_score)
    print("Задание2")
    print("Итоговые очки выживания:", total_value)
    for row in backpack2:
        print(", ".join(str(item) for item in row))
