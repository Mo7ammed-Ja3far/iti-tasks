import re


def count_vowels(input_string: str) -> int:
    return sum(1 for char in input_string if char.lower() in "aeiou")


def find_i_locations(input_string: str) -> list[int]:
    return [index for index, char in enumerate(input_string) if char.lower() == "i"]


def all_longest_strings(input_array: list[str]) -> list[str]:
    if not input_array:
        return []
    max_len = max(len(s) for s in input_array)
    return [s for s in input_array if len(s) == max_len]


def min_boxes_for_apples(apples: list[int], capacity: list[int]) -> int:
    total_apples = sum(apples)
    sorted_capacity = sorted(capacity, reverse=True)

    boxes_used = 0
    current_capacity = 0

    for cap in sorted_capacity:
        if current_capacity >= total_apples:
            break
        current_capacity += cap
        boxes_used += 1

    return boxes_used if current_capacity >= total_apples else -1


if __name__ == "__main__":
    text = "ITI Internship"
    print("Vowels count:", count_vowels(text))

    print("'i' locations:", find_i_locations(text))

    sample_array = ["aba", "aa", "ad", "vcd", "aba"]
    print("Longest strings:", all_longest_strings(sample_array))

    apples = [2, 3, 1]  # Total = 6 apples
    boxes = [4, 2, 5]  # Capacities
    print("Min boxes needed:", min_boxes_for_apples(apples, boxes))