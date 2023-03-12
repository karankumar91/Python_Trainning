import requests
import json

### post

# api_url="https://jsonplaceholder.typicode.com/todos/"
# dic={"userid":2,"title":"store data","completes":False}
# print(type(dic))
# response=requests.post(api_url,json=dic)
# print(response)
# print(response.json())
# print(response.headers)


# api_url="https://jsonplaceholder.typicode.com/todos/"
# dic={"userid":2,"title":"store data","completes":False}
# print(type(dic))
# my_header={"content-type":"application/json"}
# response=requests.post(api_url,data= json.dumps(dic),headers=my_header)
# print(response)
# print(response.json())
# print(response.headers)

### put & get

# api_url="https://jsonplaceholder.typicode.com/todos/10"
# response=requests.get(api_url)
# print(response.json())

# dic={"userid":3,"title":"put method practcei","completes":False}
# response=requests.put(api_url,json=dic)
# print(response)
# print(response.json())

### patch

# api_url="https://jsonplaceholder.typicode.com/todos/10"
# todo={"title":"patch practice"}
# print(type(todo))
# response=requests.patch(api_url, json=todo)
# print(response)
# print(response.json())

### delete

api_url="https://jsonplaceholder.typicode.com/todos/10"
response=requests.delete(api_url)
print(response)
print(response.json())




