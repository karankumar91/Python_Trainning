import requests

base_url="https://api.github.com/"
token="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"
headers = {
    "Authorization": f"Token {token}",
}

#________________Post_________________________________#

def Teams(org):
    url = base_url + "orgs/" + org + "/teams"
    print(url)
    data = {
  "id": 1,
  "name": "Justice League",
  "slug": "justice-league",

}

    response = requests.post(url,auth=(token, ''),headers=headers, json=data)
    print(response)
    print(response.json())

Teams("karanApi")

#### response 422