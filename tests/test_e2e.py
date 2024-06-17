import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get('/')
    assert b'Calculate Minimum Eating Speed for Koko' in rv.data


def test_minimum_speed(client):
    data = {
        'piles': '3,6,7,11',
        'hours': '8'
    }
    rv = client.post('/', data=data, follow_redirects=True)
    assert b'Minimum Eating Speed Required:' in rv.data
    assert b'4' in rv.data


def test_empty_input(client):
    data = {
        'piles': '',
        'hours': ''
    }
    rv = client.post('/', data=data, follow_redirects=True)
    assert b'Invalid input. Please provide valid values.' in rv.data


def test_large_input(client):
    data = {
        'piles': '1000000000,1000000000,1000000000,1000000000,1000000000',
        'hours': '5'
    }
    rv = client.post('/', data=data, follow_redirects=True)
    assert b'Minimum Eating Speed Required:' in rv.data
    assert b'1000000000' in rv.data


def test_invalid_hours(client):
    data = {
        'piles': '10,20,30',
        'hours': 'abc'
    }
    rv = client.post('/', data=data, follow_redirects=True)
    assert b'Invalid input. Please provide valid values.' in rv.data
