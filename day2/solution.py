import pathlib

def parse_input(filename: str) -> list[list[str]]:
    """Parses the file given by filename and returns a list of commands
    where each command is a list [instruction, value].
    """
    with open(filename) as f:
        planned_course = f.readlines()
    commands = [command.split() for command in planned_course]
    return commands


def follow_commands_p1(commands: list[list[str]]) -> tuple[int, int]:
    """Part 1: Uses the list of commands to calculate the final horizontal 
    position and depth and returns them."""
    horizontal = 0
    depth = 0
    for command in commands:
        match [command[0], int(command[1])]:
            case ['forward', magnitude]:
                horizontal += magnitude
            case ['down', magnitude]:
                depth += magnitude
            case ['up', magnitude]:
                depth -= magnitude
    return horizontal, depth


def follow_commands_p2(commands: list[list[str]]) -> tuple[int, int]:
    """Part 2: Uses the list of commands to calculate the final horizontal
    position and depth and returns them. For part 2 depth is determined
    by aim and horizontal movement."""
    horizontal = 0
    depth = 0
    aim = 0
    for command in commands:
        match [command[0], int(command[1])]:
            case ['forward', magnitude]:
                horizontal += magnitude
                depth += magnitude * aim
            case ['down', magnitude]:
                aim += magnitude
            case ['up', magnitude]:
                aim -= magnitude
    return horizontal, depth


if __name__ == "__main__":
    input_file_path = pathlib.Path(__file__).parent / "input.txt"
    commands = parse_input(input_file_path)

    horizontal, depth = follow_commands_p1(commands)
    print(f"Part 1: {horizontal * depth}")

    horizontal, depth = follow_commands_p2(commands)
    print(f"Part 2: {horizontal * depth}")    
