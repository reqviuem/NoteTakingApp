import json
from importlib.metadata import files

import requests

endpointSave = "http://127.0.0.1:8000/api/"
endpointCheck = "https://api.languagetool.org/v2/check"

# with open("test.md", "rb") as f:
#     get_response = requests.post(endpointSave, data={"title": "My first md"}, files={"file": f}) # HTTP Request
# print(get_response.text)

with open("test.md", "r", encoding="utf-8") as f:
    content = f.read()
    get_response = requests.post(endpointCheck, data={"text": content, "language": "en-US"})  # HTTP Request

data = get_response.json()
print(json.dumps(data, indent=2))
matches = data["matches"]

print("Grammar Issues")
for match in matches:
    sentence = match["context"]["text"]
    message = match["message"]
    suggestion = match["replacements"]

    print(f"Sentence : {sentence}")
    print(f"Issue    : {message}")
    if suggestion:
        print(f"Fix      : {suggestion[0]['value']}")
    print("---")
