import pytest
import json


def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        default='qa',
        help='environment option: qa or uat',
        choices=('qa', 'uat')
    )


@pytest.fixture
def td(request):
    env = request.config.getoption("--env")

    with open(f"environments/{env}/data.json", "r") as read_file:
        return json.load(read_file)
