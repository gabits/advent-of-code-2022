from typing import List


def get_elves_max_kcal(input_list: List[str]) -> int:
    """
    Given a flat list with numbers (item calories) and empty strings
    (dividers between elves), get the highest cumulative count of
    calories being carried by an elf.

    For this challenge, I decided to try and build an algorithm of
    linear complexity with only one loop and not performing any other
    operations on the list.
    """
    max_kcal_sum = 0
    current_elf_kcal_sum = 0
    for i in range(len(input_list)):
        # If the current item is a space, end the count for the current
        # elf and update the max value if the current one is higher.
        if input_list[i] == '':
            if current_elf_kcal_sum > max_kcal_sum:
                max_kcal_sum = current_elf_kcal_sum
            # Then, reset the calorie counter for the current elf, as
            # we'll start counting calories for a new one.
            current_elf_kcal_sum = 0
        else:
            # Increase the elf's counter with the current item's calorie
            # amount
            current_elf_kcal_sum += int(input_list[i])
    return max_kcal_sum


if __name__ == "__main__":
    with open("./day01_input.txt") as f:
        elves_kcal_count = [line.replace('\n', '') for line in f.readlines()]
    result = get_elves_max_kcal(elves_kcal_count)
    print(result)
