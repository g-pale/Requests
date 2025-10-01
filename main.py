import requests
import pprint

params = {
    'q' : 'Language: html'
}
response = requests.get('https://api.github.com/search/repositories', params = params)

print(f'Status code: {response.status_code}')

pprint.pprint(response.json())


