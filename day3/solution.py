import pathlib


def parse_input(filename: pathlib.Path) -> list[str]:
    """Parses the file given by filename and returns the report as a list of numbers
    as strings.
    """
    with open(filename) as f:
        report = f.readlines()
    report = [number.strip() for number in report]
    return report


def get_most_common_bits(report: list[str]) -> str:
    """Takes the report and calculates the most common bits in each column,
    this is then returned as a string.
    """
    transposed = zip(*report)
    most_common_bits = "".join(
        "1" if number.count("1") >= number.count("0") else "0" for number in transposed
    )
    return most_common_bits


def get_least_common_bits(most_common_bits: str) -> str:
    """Uses the number from most_common_bits and flips each bit to return
    the least common bits in each column as a string.
    """
    least_common_bits = "".join("1" if n == "0" else "0" for n in most_common_bits)
    return least_common_bits


def get_oxygen_rating(report: list[str]) -> str:
    """Calculates the oxygen rating from the report using the most_common_bits function
    to filter out numbers that only contain the most common bit in each position
    until only one number is left. Each time numbers are filtered out, the most common bit is recalculated on the remaining
    numbers from the report for a given position.
    """
    for i in range(len(report[0])):
        if len(report) == 1:
            return report[0]

        most_common_bits = get_most_common_bits(report)
        working_report = [
            number for number in report if number[i] == most_common_bits[i]
        ]
        report = working_report[:]
    return working_report[0]


def get_co2_rating(report: list[str]) -> str:
    """Calculates the co2 rating from the report using the least_common_bits function
    to filter out numbers that only contain the least common bit in each position until only
    one number is left. Each time numbers are filtered out, the least common bit is
    recalculated on the remaining numbers from the report for a given position.
    """
    for i in range(len(report[0])):
        if len(report) == 1:
            return report[0]

        most_common_bits = get_most_common_bits(report)
        least_common_bits = get_least_common_bits(most_common_bits)
        working_report = [
            number for number in report if number[i] == least_common_bits[i]
        ]
        report = working_report[:]
    return report[0]


def part_1(report: list[str]) -> None:
    """Uses the report to calculate the answer for part 1."""
    most_common_bits = get_most_common_bits(report)
    least_common_bits = get_least_common_bits(most_common_bits)

    gamma_rate = int(most_common_bits, 2)
    epsilon_rate = int(least_common_bits, 2)

    power_consumption = gamma_rate * epsilon_rate

    print(f"Part 1: {power_consumption}")


def part_2(report: list[str]) -> None:
    """Uses the report to calculate the answer for part 2."""
    oxygen_rating = int(get_oxygen_rating(report), 2)
    co2_rating = int(get_co2_rating(report), 2)

    life_support_rating = oxygen_rating * co2_rating

    print(f"Part 2: {life_support_rating}")


if __name__ == "__main__":
    test_file_path = pathlib.Path(__file__).parent / "test_input.txt"
    input_file_path = pathlib.Path(__file__).parent / "input.txt"

    report = parse_input(input_file_path)

    part_1(report)
    part_2(report)
