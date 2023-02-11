from typing import List, Tuple, Dict
from pathlib import Path
import sys


INPUT_FILE_PATH = Path("input.txt")
TASK_NUMBER = 9
STARTING_POINT = (0, 0)

MOVE_HEAD_FUNCTIONS = {
    "R": lambda head, tail, steps: play_x_axis(head, tail, steps, 1),
    "L": lambda head, tail, steps: play_x_axis(head, tail, steps, -1),
    "U": lambda head, tail, steps: play_y_axis(head, tail, steps, 1),
    "D": lambda head, tail, steps: play_y_axis(head, tail, steps, -1)
}


def play_x_axis(head: Dict[str, int], tail: Dict[str, int], steps: int, offset: int) -> Tuple[Dict[str, int]]:
    for _ in range(steps):
        head["x"] += offset
        if not is_tail_touching_head(head, tail):
            tail = move_tail(head, tail)
    return head, tail


def play_y_axis(head: Dict[str, int], tail: Dict[str, int], steps: int, offset: int) -> Tuple[Dict[str, int]]:
    for _ in range(steps):
        head["y"] += offset
        if not is_tail_touching_head(head, tail):
            tail = move_tail(head, tail)
    return head, tail


def move_tail(head: Dict[str, int], tail: Dict[str, int]) -> Dict[str, int]:
    tail_x_diff = head["x"] - tail["x"]
    tail_y_diff = head["y"] - tail["y"]

    tail_x_offset = min(max(tail_x_diff, -1), 1)
    tail_y_offset = min(max(tail_y_diff, -1), 1)

    tail["x"] += tail_x_offset
    tail["y"] += tail_y_offset
    tail["visited"].add((tail["x"], tail["y"]))

    return tail


def play_round(head: Dict[str, int], tail: Dict[str, int, set[Tuple[int, int]]], move_action: str, move_steps: int) -> Tuple[Dict[str, int]]:

    move_head_function = MOVE_HEAD_FUNCTIONS.get(move_action)

    try:
        head, tail = move_head_function(head, tail, move_steps)
    except TypeError:
        print(f"You fool, no such action as {move_action}")
        sys.exit()

    return head, tail


def is_tail_touching_head(head: Dict[str, int], tail: Dict[str, int]) -> bool:
    return abs(tail["x"] - head["x"]) <= 1 and abs(tail["y"] - head["y"]) <= 1


def get_amount_of_visited_tail_spots(game_instructions: List[Tuple[str, int]]) -> int:
    """
    This function calculates the amount of visited tail spots.
    @param game_instructions: A list of tuples that contains the game instructions
    return: amount of unique spots that the tail visited.
    """

    head = {"x": 0, "y": 0}
    tail = {"x": 0, "y": 0, "visited": {STARTING_POINT}}

    for game_instruction in game_instructions:
        move_action = game_instruction[0]
        move_steps = game_instruction[1]
        head, tail = play_round(head, tail, move_action, move_steps)

    return len(tail["visited"])


def get_game_instructions_from_file_path(file_path: Path) -> List[Tuple[str, int]]:
    """
    This function gets a file path and retruns the game instructions from it.
    """

    game_instructions = []
    raw_game_instructions_data = file_path.read_text().splitlines()

    for instruction in raw_game_instructions_data:
        split_instruction = instruction.split(" ")
        move_action = split_instruction[0]
        move_steps = int(split_instruction[-1])
        game_instructions.append((move_action, move_steps))

    return game_instructions


def main():
    """
    The main function of the program.
    """

    print(f"Advent of Code - Day {TASK_NUMBER}")
    
    first_task_game_instructions = get_game_instructions_from_file_path(INPUT_FILE_PATH)
    first_task_visited_tail_spots = get_amount_of_visited_tail_spots(first_task_game_instructions)
    print(f"First task: {first_task_visited_tail_spots}")


if __name__ == "__main__":
    main()