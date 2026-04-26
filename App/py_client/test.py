import json
import os
from importlib.metadata import files

import requests

endpointSave = "http://127.0.0.1:8000/api/save/"
endpointCheck = "https://api.languagetool.org/v2/check"
endpointList = "http://127.0.0.1:8000/api/list/"

# # LIST
# print("----LISTING ALL THE MD FILES----")
# get_response = requests.get(endpointList)
# data = get_response.json()
# mds = data["models"]
# for md in mds:
#     print(md)

# SAVE
print("----SAVE----")
directory = "."
files = os.listdir(directory)
md_files = [f for f in files if f.endswith('.md')]
for md in md_files:
    filepath = os.path.join(directory, md)  # full path
    with open(filepath, "rb") as f:
        get_response = requests.post(endpointSave, data={"title": md.replace('.md', '')}, files={"file": f})

# print("\n")

# print("----GRAMMAR CHECK----")
#
# # CHECK GRAMMAR
# with open("test.md", "r", encoding="utf-8") as f:
#     content = f.read()
#     get_response = requests.post(endpointCheck, data={"text": content, "language": "en-US"})  # HTTP Request
# data = get_response.json()
# matches = data["matches"]
#
# print("Grammar Issues")
# for match in matches:
#     sentence = match["context"]["text"]
#     message = match["message"]
#     suggestion = match["replacements"]
#
#     print(f"Sentence : {sentence}")
#     print(f"Issue    : {message}")
#     if suggestion:
#         print(f"Fix      : {suggestion[0]['value']}")
#     print("---")
