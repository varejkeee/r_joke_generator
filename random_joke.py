import requests

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke_data = response.json()
    joke = f"{joke_data['setup']} {joke_data['punchline']}"
    return joke

def main():
    joke = get_joke()
    print("Случайная шутка:")
    print(joke)

if __name__ == '__main__':
    main()
