def calculate_a1_equivalent(a1=1, a2=1, a3=8, a4=5):
    total_a1 = a1
    total_a1 += a2 * 0.5
    total_a1 += a3 * 0.25
    total_a1 += a4 * 0.125
    # Можно добавить еще больше форматов, если нужно
    return total_a1


a1_count = calculate_a1_equivalent(a1=1, a2=3, a3=5, a4=10)
print(f"Эквивалентное количество листов A1: {a1_count}")
