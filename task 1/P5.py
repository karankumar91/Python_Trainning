import requests

base_url="https://api.github.com/"
token="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"
headers = {
    "Authorization": f"Token {token}",
}

#__________________Delete Team__________

def Dteam(org):
    url = base_url + "orgs/" + org + "/teams/karanApi"
    print(url)
    response=requests.delete(url,headers=headers)
    print(response)
    print(response.json())
Dteam("karanApi")

#_____response 204_______