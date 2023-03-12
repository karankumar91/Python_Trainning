
import requests,json

base_url="https://api.github.com/"
token="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"

# def get_req(owner,repo):
#     url=base_url + "repos/" + owner + "/"+ repo +"/collaborators"
#     response=requests.get(url,auth-(token,''))
#     print (response)
# get_req("kanuu91052","portfolio")


# def get_user():
#     url = base_url + "user"
#     print(url)
#     # todo = {"name": "karan_10"}
#     response = requests.get(url, auth=(token, ''))
#     print(response)
#     print(response.json())
# get_user()

#### username


def get_user(username):
    url = base_url + "user/" + username
    print(url)
    # todo = {"name": "karan_10"}
    response = requests.get(url,auth=(token, ''))
    print(response)
    print(response.json())
get_user("124080651")