import pytest
from helpers import random_email, random_name, random_pass


@pytest.fixture
def generate_reg_data():
    payload = {
        "email": random_email(),
        "password": random_pass(),
        "name": random_name()
    }
    return payload