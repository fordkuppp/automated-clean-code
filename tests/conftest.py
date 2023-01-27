from os.path import dirname, join

import pytest


@pytest.fixture
def test_file_1() -> str:
    return join(dirname(__file__), "fixtures/1.txt")


@pytest.fixture
def test_file_2() -> str:
    return join(dirname(__file__), "fixtures/2.txt")
