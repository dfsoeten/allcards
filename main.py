import requests
import json

page = 1
data = []


while True:
    r = requests.get('https://api.magicthegathering.io/v1/cards?page=' + str(page))

    print('Requesting cards from page ' + str(page))

    if r.status_code != 200:
        with open('data.json', 'w') as outfile:
            json.dump(data, 'cards.json')

        print('Finished after looping through ')
        exit(0)
    else:
        page += 1

        data.extend(json.loads(r.content.decode())['cards'])




