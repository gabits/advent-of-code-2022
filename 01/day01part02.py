from typing import List


def get_elves_max_kcal(input_list: List[str]) -> int:
    """
    Given a flat list with numbers (item calories) and empty strings
    (dividers between elves), get the sum of the three highest
    cumulative counts of calories being carried by the elves.
    """
    top_three_max_kcal_sums = [0, 0, 0]
    current_elf_kcal_sum = 0
    for i in range(len(input_list)):
        # If the current item is a space, end the count for the current
        # elf and update the max value if the current one is higher.
        if input_list[i] == '':
            for j in range(len(top_three_max_kcal_sums)):
                if current_elf_kcal_sum > top_three_max_kcal_sums[j]:
                    # Add the new sum to the list in the highest position
                    # possible, meaning that the highest counts are always
                    # the first, for comparison purposes.
                    top_three_max_kcal_sums.insert(j, current_elf_kcal_sum)
                    break
            top_three_max_kcal_sums = top_three_max_kcal_sums[:3]
            # Then, reset the calorie counter for the current elf, as
            # we'll start counting calories for a new one.
            current_elf_kcal_sum = 0
        else:
            # Increase the elf's counter with the current item's calorie
            # amount
            current_elf_kcal_sum += int(input_list[i])
    return sum(top_three_max_kcal_sums)


if __name__ == "__main__":
    with open("./day01_input.txt") as f:
        elves_kcal_count = [line.replace('\n', '') for line in f.readlines()]
    result = get_elves_max_kcal(elves_kcal_count)
    print(result)
