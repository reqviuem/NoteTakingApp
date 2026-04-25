from importlib.metadata import files

import requests
endpoint = "http://127.0.0.1:8000/api/"

with open("test.md", "rb") as f:
    get_response = requests.post(endpoint, data={"title": "My first md"}, files={"file": f}) # HTTP Request
print(get_response.text)




