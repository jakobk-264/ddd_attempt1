import pytest

from ddd_attempt1.app import create_app
from ddd_attempt1.settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)
