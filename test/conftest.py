import pytest

@pytest.fixture
def numeros():
    return 5, 7  # da 12 → coincide con tu test

@pytest.fixture
def numeros_flotantes():
    return 0.1, 0.2