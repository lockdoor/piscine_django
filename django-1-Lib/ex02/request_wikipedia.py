import requests

word="Hello"

req = requests.get(f"https://en.wikipedia.org/w/api.php?action=query&prop=info&titles=Earth&format=json")
print (req.status_code)
print (req.json())
