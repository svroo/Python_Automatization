# Add a flag that changes the behavior when present. The `recipe_cli_step3.py` script is as follows

import argparse


def main(character, number):
    print(character * number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="A number")
    parser.add_argument("-c", type=str, help="character to print", default="#")
    parser.add_argument(
        "-U",
        action="store_true",
        default=False,
        dest="uppercase",
        help="Uppercase the character",
    )
    args = parser.parse_args()

    if args.uppercase:
        args.c = args.c.cupper()
    main(args.c, args.number)
