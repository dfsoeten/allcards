import requests
import json

page = 1
data = []

while True:
    r = requests.get('https://api.magicthegathering.io/v1/cards?page=' + str(page))

    print('Requesting cards from page ' + str(page))

    if r.status_code != 200 or not json.loads(r.content.decode())['cards']:
        with open('cards.json', 'w') as outfile:
            json.dump(data, outfile)

        print('Finished after looping through ' + str(page) + ' pages with ' + str(len(data)) + ' results')
        exit(0)
    else:
        page += 1
        data.extend(json.loads(r.content.decode())['cards'])




