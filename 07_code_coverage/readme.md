# pytest code coverage tool

## Requirements
* Python (3.10+)

For the instructions how to setup pytest and run the tests refer to the root README.

## Generate coverage reports

### Create html report using coverage
```shell
$ coverage run -m pytest tests/unit/test_bank_app.py
$ coverage html
```

### Create html report using pytest-cov
```shell
$ pytest tests/unit/test_bank_app.py --cov --cov-report=html:coverage_report
```

## References

* [Coverage.py documentation](https://coverage.readthedocs.io/en/7.6.9/)
* [pytest-cov documentation](https://pytest-cov.readthedocs.io/en/latest/reporting.html)
* [Code coverage with pytest](https://medium.com/@sumanrbt1997/code-coverage-with-pytest-1f72653b0bf2)
* [How To Generate Beautiful & Comprehensive Pytest Code Coverage Reports (With Example)](https://pytest-with-eric.com/pytest-best-practices/pytest-code-coverage-reports/)
