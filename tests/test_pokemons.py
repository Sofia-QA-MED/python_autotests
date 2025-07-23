import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'your_token'
HEADER = {'Content-type' : 'application/json', 'trainer_token':'your_token'}
TRAINER_ID = '22343'
TRAINER_NAME = 'SofiaSpy'

def test_status_code():
    responce = requests.get(url =  f'{URL}/trainers')
    assert responce.status_code == 200

def test_trainer_name():
    responce_get = requests.get(url =  f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce_get.json()['data'][0]['trainer_name'] == TRAINER_NAME

