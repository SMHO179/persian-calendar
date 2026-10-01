import argparse

import jdatetime

from .cli import render_calendar


def main():
    parser = argparse.ArgumentParser(
        prog="pcal",
        description="Persian calendar for terminal",
    )

    parser.add_argument(
        "-m",
        "--month",
        type=int,
        help="Persian month",
    )

    parser.add_argument(
        "-y",
        "--year",
        type=int,
        help="Persian year",
    )

    args = parser.parse_args()

    today = jdatetime.date.today()

    year = args.year or today.year
    month = args.month or today.month

    if not 1 <= month <= 12:
        parser.error("month must be between 1 and 12")

    render_calendar(year, month)


if __name__ == "__main__":
    main()
