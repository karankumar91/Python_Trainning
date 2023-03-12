headers = {
    "Authorization": f"Token {token}",
}
# # Send the GET request to list the teams
response = requests.get(base_url, headers=headers)

print(response)
# print(response.json())