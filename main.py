import sys

from reports.salary import salary_report
from worker_data import WorkerData


def create_workers_data_list(file_name: str) -> list[WorkerData]:
    with open(file_name, "r") as f:
        columns: list[str] = f.readline().rstrip().split(",")
        worker_list: list[WorkerData] = []
        for line in f:
            worker: dict[str, int | str] = {}
            values = line.rstrip().split(",")
            for idx, value in enumerate(values):
                try:
                    value = int(value)
                except ValueError:
                    pass
                worker[columns[idx]] = value
            worker_list.append(WorkerData(**worker))
    return worker_list


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        workers_data = create_workers_data_list(filename)
        salary_report(workers_data)
