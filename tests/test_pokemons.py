import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '39959208832e90eb4ec0e487bd138e7a'
HEADER = {'Content-type' : 'application/json', 'trainer_token':'39959208832e90eb4ec0e487bd138e7a'}
TRAINER_ID = '22343'
TRAINER_NAME = 'SofiaSpy'

def test_status_code():
    responce = requests.get(url =  f'{URL}/trainers')
    assert responce.status_code == 200

def test_trainer_name():
    responce_get = requests.get(url =  f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce_get.json()['data'][0]['trainer_name'] == TRAINER_NAME

