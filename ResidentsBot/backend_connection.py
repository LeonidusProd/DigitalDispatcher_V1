import requests


def get_test_data():
    response = requests.get('http://localhost:8000/api/v1/test/')
    return response.json().get('test_data')
