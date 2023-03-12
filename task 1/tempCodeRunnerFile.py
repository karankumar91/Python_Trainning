def Gteam(org):
    url = base_url + "orgs/" + org + "/teams/karanApi"
    print(url)
    response=requests.get(url,headers=headers)
    print(response)
    print(response.json())
Gteam("karanApi")