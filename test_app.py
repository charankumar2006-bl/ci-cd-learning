
from app import greet, get_version


def test_greet():
    assert greet("Charan") == "Hello, Charan!"


def test_version():
    assert get_version() == "1.0.1"
