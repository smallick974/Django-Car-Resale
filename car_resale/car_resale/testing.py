import json
from settings import BASE_DIR

with open(BASE_DIR / 'constants.json') as file:
        file = json.load(file)
        print(file)