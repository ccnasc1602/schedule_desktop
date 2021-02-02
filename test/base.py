import json
import pytest

def load_data(file):
    with open(file, 'r') as f:
        return json.load(f)

@pytest.fixture
def user_data_fake():
    return load_data('datafake/user_fake.json')