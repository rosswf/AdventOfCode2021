from itertools import pairwise
from typing import List


def parse_input(filename: str) -> List[int]:
    """Parses the file given by filename and returns a list of integers
    where each value in the list is a line from filename.
    """
    with open(filename) as f:
        measurements = f.readlines()
    measurements = [*map(int, measurements)]
    return measurements


def check_increasing(measurements: List[int]) -> int:
    """Pairs the values in measurements and returns how many pairs are
    increasing.
    """
    paired = pairwise(measurements)
    paired_increasing = map(lambda p: p[0] < p[1], paired)
    return sum(paired_increasing)


def get_three_measurement_sums(measurements: List[int]) -> List[int]:
    """Takes a list of measurements and returns the sums of each 3 consecutive
    values in the list.
    """
    measurement_sums = [
        measurements[i - 2] + measurements[i - 1] + measurements[i]
        for i in range(2, len(measurements))
    ]
    return measurement_sums


if __name__ == "__main__":
    measurements = parse_input("input.txt")

    part1_solution = check_increasing(measurements)

    three_measurement_sums = get_three_measurement_sums(measurements)
    part2_solution = check_increasing(three_measurement_sums)

    print(f"Part 1: {part1_solution}")
    print(f"Part 2: {part2_solution}")
