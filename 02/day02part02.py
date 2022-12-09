from typing import List


def does_it_work() -> bool:
    sample_strategy_guide = [
        ["A", "Y"],  # Draw. A-A = 3 + 1 = 4 => 4
        ["B", "X"],  # Lose. B-A = 0 + 1 = 1 => 5
        ["C", "Z"],  # Win. C-A = 6 + 1 = 7 => 12
        ["A", "Z"],  # Win. A-B = 6 + 2 = 8 => 20
        ["B", "X"],  # Lose. B-A = 0 + 1 = 1 => 21
        ["C", "Y"],  # Draw. C-C = 3 + 3 = 6 => 27
        ["A", "X"],  # Lose. A-C = 0 + 3 = 3 => 30
        ["B", "Y"],  # Draw. B-B = 3 + 2 = 5 => 35
        ["C", "Z"],  # Win. C-A = 6 + 1 = 7 => 42
    ]
    expected_result = 42
    result = get_total_score(sample_strategy_guide)
    print(
        f"The test result is {result}. The expected result "
        f"was {expected_result}."
    )
    return result == expected_result


def get_total_score(expected_scores: List[List[str]]) -> int:
    rps_score_mapping = {"A": 1, "B": 2, "C": 3}
    # Rock beats Scissors, Paper beats Rock, Scissors beat Paper
    winner_mapping = {"A": "C", "B": "A", "C": "B"}
    my_score = 0
    for i in expected_scores:
        adversary_choice = i[0]
        # Compare the strings to find out if there was a
        # win or a tie, since we don't care about a loss
        # (we are only calculating my score)
        if i[1] == "X":     # Lose
            my_choice = winner_mapping[adversary_choice]
        elif i[1] == "Y":   # Draw
            my_choice = i[0]
            my_score += 3
        else:               # Win
            my_choice = winner_mapping[winner_mapping[adversary_choice]]
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
