from .worker_data import WorkerData


def create_workers_data_list_v1(file_name: str) -> list[WorkerData]:
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
