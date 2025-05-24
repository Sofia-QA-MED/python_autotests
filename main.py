import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '39959208832e90eb4ec0e487bd138e7a'
HEADER = {'Content-type' : 'application/json', 'trainer_token':'39959208832e90eb4ec0e487bd138e7a'}

body_create = {
 "name": "Бульбазавр",
 "photo_id": 12
}

body_change = {
    "pokemon_id": "12331",
    "name": "New Name",
    "photo_id": 2
}

'''Создание покемона'''
responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (responce_create.json())
pokemon_id = responce_create.json()['id']

'''Смена имени покемона'''
body_change = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}
responce_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print (responce_change.json())


'''Поймать покемона в покебол'''
body_add_pokeball = {
  "pokemon_id": pokemon_id  
}
responce_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print (responce_add_pokeball.json())





