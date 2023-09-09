import requests
from questionary import select

def get_random_joke(category=None):
    url = 'https://official-joke-api.appspot.com/jokes/random' #something wrong with languages

    params = {}
    if category:
        params['category'] = category

    response = requests.get(url, params=params)
    if response.status_code == 200:
        joke = response.json()
        if 'setup' in joke and 'punchline' in joke:
            setup = joke['setup']
            punchline = joke['punchline']
            return f"{setup}\n{punchline}"
    return "Failed to fetch a joke."

# Define the categories for the joke
categories = [
    'General',
    'Programming',
    'Puns',
    'Spooktober',
    'Christmas'
]

# Prompt user to select a category for the joke
selected_category = select(
    'Choose a category for the joke:',
    choices=categories
).ask()

random_joke = get_random_joke(selected_category.lower())
print(random_joke)
