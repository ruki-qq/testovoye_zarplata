import pytest

from workers_data import create_workers_data_list_v1


def test_create_workers_data_list_v1_valid_hourly_rate(tmp_path, csv_data_hourly_rate):
    file_path = tmp_path / "workers.csv"
    file_path.write_text(csv_data_hourly_rate)
    workers = create_workers_data_list_v1(str(file_path))
    assert len(workers) == 3
    worker = workers[0]
    assert worker.id == 1
    assert worker.email == "alice@example.com"
    assert worker.name == "Alice Johnson"
    assert worker.department == "Marketing"
    assert worker.hours_worked == 160
    assert worker.hourly_rate == 50
    assert worker.hourly_salary == 50
    assert worker.result_salary == 160 * 50


def test_create_workers_data_list_v1_valid_rate(tmp_path, csv_data_rate):
    file_path = tmp_path / "workers.csv"
    file_path.write_text(csv_data_rate)
    workers = create_workers_data_list_v1(str(file_path))
    worker = workers[1]
    assert worker.hours_worked == 150
    assert worker.rate == 35
    assert worker.hourly_salary == 35
    assert worker.result_salary == 150 * 35


def test_create_workers_data_list_v1_valid_salary(tmp_path, csv_data_salary):
    file_path = tmp_path / "workers.csv"
    file_path.write_text(csv_data_salary)
    workers = create_workers_data_list_v1(str(file_path))
    worker = workers[2]
    assert worker.hours_worked == 160
    assert worker.salary == 37
    assert worker.hourly_salary == 37
    assert worker.result_salary == 160 * 37


def test_create_workers_data_list_v1_invalid_type(tmp_path, csv_data_invalid):
    file_path = tmp_path / "workers.csv"
    file_path.write_text(csv_data_invalid)
    with pytest.raises(TypeError):
        create_workers_data_list_v1(str(file_path))


def test_create_workers_data_list_v1_missing_required_field(tmp_path, csv_data_missing):
    file_path = tmp_path / "workers.csv"
    file_path.write_text(csv_data_missing)
    with pytest.raises(TypeError):
        create_workers_data_list_v1(str(file_path))


def test_create_workers_data_list_v1_extra_column(tmp_path, csv_data_extra):
    file_path = tmp_path / "workers.csv"
    file_path.write_text(csv_data_extra)
    with pytest.raises(TypeError):
        create_workers_data_list_v1(str(file_path))
