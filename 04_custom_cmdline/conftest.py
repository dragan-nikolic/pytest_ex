import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa", help="my option: qa or uat"
    )
    parser.addoption(
        "--date_column", action="store", help="date column for filtering data"
    )
    parser.addoption(
        "--no-docker", action="store_true", help="if true do not start docker"
    )


def pytest_sessionstart(session):
    no_docker = session.config.getoption('--no-docker')
    print(f'******* no-docker: {no_docker}')

    if not no_docker:
        print('*** run docker ***')
    else:
        print('*** dont run docker')

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

@pytest.fixture
def date_column(request):
    return request.config.getoption("--date_column")
