from typing import List


def does_it_work() -> bool:
    sample_strategy_guide = [
        ["A", "Y"],  # A-B = 6 + 2 = 8 => 8
        ["B", "X"],  # B-A = 0 + 1 = 1 => 9
        ["C", "Z"],  # C-C = 3 + 3 = 6 => 15
        ["A", "Z"],  # A-C = 0 + 3 = 3 => 18
        ["B", "X"],  # B-A = 0 + 1 = 1 => 19
        ["C", "Y"],  # C-B = 0 + 2 = 2 => 21
        ["A", "X"],  # A-A = 3 + 1 = 4 => 25
        ["B", "Y"],  # B-B = 3 + 2 = 5 => 30
        ["C", "Z"],  # C-C = 3 + 3 = 6 => 36
    ]
    expected_result = 36
    result = get_total_score(sample_strategy_guide)
    print(
        f"The test result is {result}. The expected result "
        f"was {expected_result}."
    )
    return result == expected_result


def get_total_score(expected_scores: List[List[str]]) -> int:
    rps_score_mapping = {"A": 1, "B": 2, "C": 3}
    mapping_to_adversary = {"X": "A", "Y": "B", "Z": "C"}
    # Rock beats Scissors, Paper beats Rock, Scissors beat Paper
    winner_mapping = {"A": "C", "B": "A", "C": "B"}
    my_score = 0
    for i in expected_scores:
        adversary_choice = i[0]
        my_choice = mapping_to_adversary[i[1]]
        # Compare the strings to find out if there was a
        # win or a tie, since we don't care about a loss
        # (we are only calculating my score)
        if adversary_choice == my_choice:
            my_score += 3
        elif winner_mapping[my_choice] == adversary_choice:
            my_score += 6
        my_score += rps_score_mapping[my_choice]
    return my_score


if __name__ == "__main__":
    assert does_it_work()
    with open("./day02_input.txt") as f:
        # Transform the input into a list of lists
        strategy_guide = [line.replace('\n', '').split(" ") for line in f.readlines()]
    result = get_total_score(strategy_guide)
    print(result)
