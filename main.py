import argparse

from reports import REPORTS
from workers_data import create_workers_data_list_v1


def main():
    parser = argparse.ArgumentParser(
        description="Parse arguments to generate reports based on workers data"
    )
    parser.add_argument(
        "files", nargs="+", help="Paths to CSV files containing workers data"
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Generate reports based on workers data",
        choices=REPORTS,
    )
    args: argparse.Namespace = parser.parse_args()

    for filename in args.files:
        workers_data = create_workers_data_list_v1(filename)
        print(REPORTS[args.report](workers_data))


if __name__ == "__main__":
    main()
