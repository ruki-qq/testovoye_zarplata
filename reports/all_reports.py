from workers_data import WorkerData


def salary_report(workers_data: list[WorkerData]):
    report: dict[str, list[dict[str, dict[str, int | str]]]] = {}
    for worker in workers_data:
        worker_salary: dict[str, dict[str, str]] = {
            worker.name: {
                "hours": worker.hours_worked,
                "rate": worker.hourly_salary,
                "result_salary": worker.result_salary,
            }
        }
        if worker.department not in report:
            report[worker.department] = []
        report[worker.department].append(worker_salary)
    print(report)
