import requests

base_url="https://api.github.com/"
token="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"
headers = {
    "Authorization": f"Token {token}",
}

#___________________________get team by name__________________

def Gteam(org):
    url = base_url + "orgs/" + org + "/teams/karanApi"
    print(url)
    response=requests.get(url,headers=headers)
    print(response)
    print(response.json())
Gteam("karanApi")

## response 200