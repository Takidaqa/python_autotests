import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'f695185ab643c6d8f55a6f3437b8fe74'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '2393'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Сквиртл'

@pytest.mark.parametrize('key, value', [('name', 'Сквиртл'), ('trainer_id', TRAINER_ID),('id', '26474')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value

