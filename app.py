from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/') 

# Selecciona la base de datos y la colección
db = client['pokemones']
collection = db['pokemon']

#guardar tipos de pokemon y contar cuantos hay de cada tipo

types_count = {}
for pokemon in collection.find():
    for type in pokemon['types']:
        if type in types_count:
            types_count[type] += 1
        else:
            types_count[type] = 1

#guardar altura y contar cuantos pokemon hay de cada altura
height_count = {}
for pokemon in collection.find():
    if pokemon['height'] in height_count:
        height_count[pokemon['height']] += 1
    else:
        height_count[pokemon['height']] = 1

#guardar los resultados en un archivo json
import json
with open('types_count.json', 'w') as file:
    json.dump(types_count, file)

#guardar los resultados en un archivo json
with open('height_count.json', 'w') as file:
    json.dump(height_count, file)




