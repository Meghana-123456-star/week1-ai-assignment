import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
data = response.json()

print("JOKE:")
print(data["setup"])
print(data["punchline"])

with open("output.txt", "a") as file:
    file.write(f"Joke: {data['setup']} - {data['punchline']}\n")