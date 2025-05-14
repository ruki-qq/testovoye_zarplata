import pytest

from workers_data import WorkerData

# test_workers_fixtures

@pytest.fixture
def my_worker_hourly_rate():
    return WorkerData(
        id=1,
        email="test@example.com",
        name="Test",
        department="Dept",
        hours_worked=40,
        hourly_rate=20,
        rate=None,
        salary=None,
    )

@pytest.fixture
def my_worker_rate():
    return WorkerData(
        id=1,
        email="test@example.com",
        name="Test",
        department="Dept",
        hours_worked=40,
        hourly_rate=None,
        rate=500,
        salary=None,
    )

@pytest.fixture
def my_worker_salary():
    return WorkerData(
        id=1,
        email="test@example.com",
        name="Test",
        department="Dept",
        hours_worked=40,
        hourly_rate=None,
        rate=None,
        salary=1000,
    )

@pytest.fixture
def my_worker_none():
    return WorkerData(
        id=1,
        email="test@example.com",
        name="Test",
        department="Dept",
        hours_worked=40,
        hourly_rate=None,
        rate=None,
        salary=None,
    )

#test_csv_to_objects fixtures

@pytest.fixture
def csv_data():
    return """id,email,name,department,hours_worked,hourly_rate
    1,alice@example.com,Alice Johnson,Marketing,160,50
    2,bob@example.com,Bob Smith,Design,150,40
    3,carol@example.com,Carol Williams,Design,170,60"""