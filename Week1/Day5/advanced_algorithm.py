# Daily Challenge: Advanced Algorithm - Week 1, Day 5

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728


def find_pairs(numbers, target):
    seen = set()
    pairs = set()

    for number in numbers:
        partner = target - number
        if partner in seen:
            pair = (min(number, partner), max(number, partner))
            pairs.add(pair)
        seen.add(number)

    return sorted(pairs)


pairs = find_pairs(list_of_numbers, target_number)

for a, b in pairs:
    print(f"{a} and {b} sums to the target_number {target_number}")

print(f"Found {len(pairs)} different pairs.")
