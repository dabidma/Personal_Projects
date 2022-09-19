import requests


def search(query):
    url = f'https://www.ssense.com/en-us/men/designers/{query}'

    html = requests.get(url=url)

print('hello')

