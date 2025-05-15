# Worker Management System

A Python tool for managing worker data, calculating salaries, and generating formatted reports. Handles CSV input and produces both JSON reports and CLI-friendly outputs.

## Features

- **CSV Data Ingestion**: Read worker data from CSV files with flexible field support
- **Salary Calculation**: 
  - Supports multiple rate types (`hourly_rate`, `rate`, `salary`)
  - Automatic rate prioritization logic
  - Hours worked × rate calculation
- **Report Generation**:
  - JSON salary reports grouped by department
- **Type Safety**: Uses Python dataclasses for data validation

## Installation

1. **Prerequisites**:
   - Python 3.11+

2. **Clone repository**:
   ```bash
   git clone https://github.com/ruki-qq/testovoye_zarplata.git
   cd testovoye_zarplata
   
3.  **Create venv and install requirements**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

4.  **Run tests**
    ```bash
    pytest -vvv
    
5.  **Run main.py**
    ```bash
    python main.py [files] --report [report name]
    *Example*
    python main.py csv/data1.csv csv/data2.csv csv/data3.csv --report salary
