import requests
from bs4 import BeautifulSoup

class ssense:
    def __init__(self):
        self.headers = {
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-US,en;q=0.9if-none-match: "3cee1-f+6fygp2lrc1pL+m5Z+ITkWbRBw"',
        'referer': 'https://www.ssense.com/en-us/men',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }
        self.url = 'https://www.ssense.com/en-us/'

    def keywords_search_words(self, user_message):
        words = user_message.split()[1:]
        keywords = '/'.join(words)
response = requests.get('https://www.ssense.com/en-us/',headers = headers)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(response)