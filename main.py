import os
from argparse import ArgumentParser
from typing import List

from src.handler import Handler


def parse_inputs(input_str: str) -> List[str]:
    return input_str.strip().split(" ")

if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument(
        "-file", help="path to input file containing the car parking system events"
    )
    args = parser.parse_args()
    if not os.path.isfile(args.file):
        raise FileNotFoundError(f"File: {args.file} does not exist")

    events_cache: Handler = Handler()
    with open(args.file, "r") as f:
        init_str: str = f.readline()
        events_cache.init_parking_lot(parse_inputs(init_str))

        for line in f:
            try:
                print(f"{events_cache.handle(parse_inputs(line))}")
            except Exception as e:
                print(f"Reject - {str(e)}")
