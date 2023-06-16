import requests

def get_random_joke(language='en'):
    url = f'https://official-joke-api.appspot.com/jokes/{language}/random'
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        if 'setup' in joke and 'punchline' in joke:
            setup = joke['setup']
            punchline = joke['punchline']
            return f"{setup}\n{punchline}"
    return "Failed to fetch a joke."

# Запрос у пользователя выбора языка
language = input("Выберите язык шутки (en - английский, es - испанский, ru - русский): ")

random_joke = get_random_joke(language)
print(random_joke)
