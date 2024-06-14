import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa", help="my option: qa or uat"
    )
    parser.addoption(
        "--date_column", action="store", help="date column for filtering data"
    )


@pytest.fixture
def env(request):
    return request.config.getoption("--env")

@pytest.fixture
def date_column(request):
    return request.config.getoption("--date_column")
