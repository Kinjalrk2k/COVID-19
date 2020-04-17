import os
if not os.path.exists('data'):
    os.makedirs('data')

import urllib.request, json

api_index_url = 'https://covid19.mathdro.id/api/' # base api url
with urllib.request.urlopen(api_index_url) as url:
    api_index = json.loads(url.read().decode())
    print(api_index)

# grabbing data for confirmned, recovered and deadths in local .json files
for i in ['confirmed', 'recovered', 'deaths']:
    with urllib.request.urlopen(api_index[i]['detail']) as url:
        data = json.loads(url.read().decode())
        print(data)
        with open(os.path.join('data', i+'.json'), 'w') as outf:
            json.dump(data, outf)

# grabbing country data for lookup
with urllib.request.urlopen('https://covid19.mathdro.id/api/countries') as url:
        data = json.loads(url.read().decode())
        print(data)
        with open(os.path.join('data','countries.json'), 'w') as outf:
            json.dump(data, outf)

# last updated timestamp
print('Last updated:', api_index['lastUpdate'])

