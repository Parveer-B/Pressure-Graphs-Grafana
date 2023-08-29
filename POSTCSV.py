import json
import base64
import requests

def POSTCSV(file):
    encoded_content = base64.b64encode(file).decode()

    payload = {
        "message": "Add new file via API",
        "content": encoded_content,
        "sha": "2a1eee2ad75007906d74338415bd354a4102bda1"
    }

    payload_json = json.dumps(payload)

    url = 'https://api.github.com/repos/Parveer-B/Pressure-Graphs-Grafana/contents/uploads/extorrdata.csv'
    headers = {
        'Authorization': 'token ' + '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',
        'Accept': 'application/vnd.github+json'
    }

    response = requests.put(url, headers=headers, data = payload_json)
    #response = requests.post(url, headers=headers, files = files)

    if response.status_code == 200:
        print('File successfully created on GitHub.')
    else:
        print('Error:', response.status_code)
        print(response.content)




with open('uploads/extorrdata.csv', 'rb') as file:
    POSTCSV(file.read())
    #POSTCSV(file)
