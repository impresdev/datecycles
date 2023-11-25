# Datecycles

`Datecycles` is a simple Python package designed for generating a series of dates based on a weekly, fortnightly, 4-weekly, monthly, or quarterly basis.

## Installation

Install `Datecycles` using pip:

```bash
pip install datecycles
```

## Usage

### Command-Line Interface

Use `Datecycles` from the command line as follows:

```bash
datecycles <start_date> <cycle_period> <cycle_count>
```

- `start_date`: Start date in YYYY-MM-DD format.
- `cycle_period`: Cycle period, one of 52 (weekly), 26 (fortnightly), 13 (4-weekly), 12 (monthly), or 4 (quarterly).
- `cycle_count`: Number of cycles to generate.

#### Example

```bash
datecycles 2023-01-01 13 5
# 2023-01-01
# 2023-01-29
# 2023-02-26
# 2023-03-26
# 2023-04-23
```

This command generates five 4-weekly dates starting from January 1, 2023.

### In Python Scripts

Import and use `Datecycles` in your Python script:

```python
from datecycles.core import generate_cycle_dates

cycle_dates = generate_cycle_dates("2023-01-01", 12, 5)
for date in cycle_dates:
    print(date)
```

## Development

### Running Tests

Run unit tests using:

```bash
pytest
```

## Dependencies

- Python 3.x
- `python-dateutil` package

Install dependencies using:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Building

Build and install `Datecycles` using:

```bash
pip install wheel
python setup.py sdist bdist_wheel
pip install dist/datecycles-0.1.1-py3-none-any.whl
```

## Contributing

Contributions to `Datecycles` are welcome! Please submit pull requests with accompanying unit tests.

## License

`Datecycles` is released under the MIT License.

## Contact

For questions or feedback, please open an issue on the GitHub repository.
