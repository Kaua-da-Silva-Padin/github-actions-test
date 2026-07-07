import requests
import os

index_path = 'index.html'
tabs = '\t' * 6

def get_rnd_word() -> str:
    response = requests.get('https://random-word-api.herokuapp.com/word?lang=en')
    return response.json()[0] if response.status_code == 200 else 'An error Occured!'

rnd_word = get_rnd_word()
html_content = ''

if os.path.exists(index_path):
    with open(index_path, 'r') as f:
        html_content = f.read()

    with open(index_path, 'w') as f:
        element = f'\n{tabs}<li class="list-group-item list-group-item-primary fs-4 fw-bold fst-italic rounded-2 mb-2">{rnd_word}</li>\n{tabs}<placeholder>'
        
        f.write(html_content.replace(
            '<placeholder>',
            element
        ))