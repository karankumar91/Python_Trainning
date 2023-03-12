import requests

base_url="https://api.github.com/"
token="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"
headers = {
    "Authorization": f"Token {token}",
}

#_________________________________Patch_________________________

def PaTeams(org):
    url = base_url + "orgs/" + org + "/teams/karanApi"
    print(url)
    data = {
  "id": 7404613,
  "name": "karanApi",
  "slug": "justice-league",
}
    response = requests.patch(url,auth=(token, ''),headers=headers, json=data)
    print(response)
    print(response.json())

PaTeams("karanApi")

##### response 200
