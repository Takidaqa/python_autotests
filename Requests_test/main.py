import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'f695185ab643c6d8f55a6f3437b8fe74'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "aleksandrk.qa@yandex.ru",
    "password": "13100Ylibka"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Сквиртл",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_change = {
    "pokemon_id": "26468",
    "name": "Покемон",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
body_pokebol = {
	"pokemon_id": "26468"
}

# Регистрация тренера
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

# Активация тренера
'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

# Создание покемона
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

# Смена имени покемона
response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

# Поймать покемона в покебол
response_pokebol = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokebol)
print(response_pokebol.text)

message = response_create.json()['message']
print(message) 

