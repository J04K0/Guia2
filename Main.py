import requests
import pymongo as mongo

cliente = mongo.MongoClient("mongodb://localhost:27017/")
db = cliente["pokemones"]
coleccion = db["pokemon"]

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=20')
data = response.json()

for pokemon_data in data['results']:
    pokemon_response = requests.get(pokemon_data['url'])
    pokemon_data = pokemon_response.json()
    name = pokemon_data['name']
    types = [t['type']['name'] for t in pokemon_data['types']]
    height = pokemon_data['height']
    pokemon = {'name': name, 'types': types,'height': height}
    coleccion.insert_one(pokemon)
    print(f"Pokemon {name} insertado en la base de datos")

print("Proceso finalizado")
