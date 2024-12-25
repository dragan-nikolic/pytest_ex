# Demo custom command line variables

For info how to run the tests refer to the 01_pytest_hello readme file.

## Expected results

### Example 1 

command: $ pytest -v test_class.py

result: test_qa passed, 3 failed

### Example 2

command: $ pytest -v --env uat --date_column load_date test_class.py

result: test_uat passed, 3 failed

### Example 3

command: $ pytest -v --date_column load_date test_class.py

result: test_uat failed, 3 passed
