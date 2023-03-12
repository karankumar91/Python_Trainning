import requests

base_url="https://api.github.com/"
token="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"
headers = {
    "Authorization": f"Token {token}",
}

# # Send the GET request to list the teams 

response = requests.get(base_url, headers=headers)
print(response)
print(response.json())

#_____ response 200 ______