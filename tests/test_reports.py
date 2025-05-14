import json
from reports.all_reports import salary_report


def test_salary_report_single_worker(capsys, my_worker_hourly_rate):
    report = json.loads(salary_report([my_worker_hourly_rate]))

    assert "Dept" in report
    assert len(report["Dept"]) == 1
    assert report["Dept"][0]["Test"]["hours"] == 40
    assert report["Dept"][0]["Test"]["rate"] == 20
    assert report["Dept"][0]["Test"]["result_salary"] == 800


def test_salary_report_multiple_workers_same_department(
    capsys, my_worker_hourly_rate, my_worker_rate
):
    workers = [
        my_worker_hourly_rate,
        my_worker_rate,
    ]
    salary_report(workers)
    report = json.loads(salary_report(workers))

    assert len(report["Dept"]) == 2
    assert report["Dept"][0]["Test"]["result_salary"] == 800
    assert report["Dept"][1]["Test1"]["result_salary"] == 20000


def test_salary_report_multiple_departments(
    capsys, my_worker_hourly_rate, my_worker_salary
):
    workers = [
        my_worker_hourly_rate,
        my_worker_salary,
    ]
    report: dict[str] = json.loads(salary_report(workers))

    assert "Dept" in report and "Dept1" in report
    assert report["Dept"][0]["Test"]["rate"] == 20
    assert report["Dept1"][0]["Test2"]["rate"] == 1000


def test_salary_report_uses_rate_when_hourly_rate_missing(capsys, my_worker_rate):
    report = json.loads(salary_report([my_worker_rate]))

    assert report["Dept"][0]["Test1"]["rate"] == 500
    assert report["Dept"][0]["Test1"]["result_salary"] == 20000


def test_salary_report_empty_input(capsys):
    report = json.loads(salary_report([]))
    assert report == {}
