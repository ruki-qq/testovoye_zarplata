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
def csv_data_hourly_rate():
    return """id,email,name,department,hours_worked,hourly_rate
    1,alice@example.com,Alice Johnson,Marketing,160,50
    2,bob@example.com,Bob Smith,Design,150,40
    3,carol@example.com,Carol Williams,Design,170,60"""

@pytest.fixture
def csv_data_rate():
    return """department,id,email,name,hours_worked,rate
    HR,101,grace@example.com,Grace Lee,160,45
    Marketing,102,henry@example.com,Henry Martin,150,35
    HR,103,ivy@example.com,Ivy Clark,158,38"""

@pytest.fixture
def csv_data_salary():
    return """email,name,department,hours_worked,salary,id
    karen@example.com,Karen White,Sales,165,50,201
    liam@example.com,Liam Harris,HR,155,42,202
    mia@example.com,Mia Young,Sales,160,37,203"""

@pytest.fixture
def csv_data_invalid():
    return """email,name,department,hours_worked,salary,id
    karen@example.com,Karen White,Sales,raz,50,201
    liam@example.com,Liam Harris,HR,dva,42,202
    mia@example.com,Mia Young,Sales,tri,37,203"""

@pytest.fixture
def csv_data_extra():
    return """email,name,department,hours_worked,salary,id,extra
        karen@example.com,Karen White,Sales,raz,50,201,ignore
        liam@example.com,Liam Harris,HR,dva,42,202,ignore
        mia@example.com,Mia Young,Sales,tri,37,203,ignore"""

@pytest.fixture
def csv_data_missing():
    return """email,name,department,hours_worked,salary
        karen@example.com,Karen White,Sales,raz,50
        liam@example.com,Liam Harris,HR,dva,42
        mia@example.com,Mia Young,Sales,tri,37"""