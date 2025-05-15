import pytest


def test_hourly_salary_uses_hourly_rate(my_worker_hourly_rate):
    assert my_worker_hourly_rate.hourly_salary == 20


def test_hourly_salary_uses_rate_if_others_none(my_worker_rate):
    assert my_worker_rate.hourly_salary == 500


def test_hourly_salary_uses_salary_if_others_none(my_worker_salary):
    assert my_worker_salary.hourly_salary == 1000


def test_hourly_salary_all_none_raises_error(my_worker_none):
    with pytest.raises(TypeError):
        my_worker_none.hourly_salary


def test_result_salary_calculation(my_worker_hourly_rate):
    assert (
        my_worker_hourly_rate.result_salary
        == my_worker_hourly_rate.hourly_salary * my_worker_hourly_rate.hours_worked
    )
