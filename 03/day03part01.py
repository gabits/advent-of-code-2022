from typing import List


alphabet = 'abcdefghijklmnopqrstuvwsyz'


def does_it_work() -> bool:
    sample_rucksacks = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]
    expected_result = 157
    result = get_sum_priorities_dupe_items(sample_rucksacks)
    print(
        f"The test result is {result}. The expected result "
        f"was {expected_result}."
    )
    return result == expected_result


def get_sum_priorities_dupe_items(rucksacks: List[str]) -> int:
    sum_of_priorities = 0
    for rucksack in rucksacks:
        middle = len(rucksack) // 2
        for item in rucksack[:middle]:
            if item in rucksack[middle:]:
                sum_of_priorities += alphabet.index(item.lower()) + 1
                if item.isupper():
                    sum_of_priorities += 26
                break
    return sum_of_priorities


if __name__ == "__main__":
    assert does_it_work()
    with open("./day03_input.txt") as f:
        # Transform the input into a list of lists
        rucksacks = [line.replace("\n", "") for line in f.readlines()]
    result = get_sum_priorities_dupe_items(rucksacks)
    print(result)
