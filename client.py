# https://stackoverflow.com/questions/4476373/simple-url-get-post-function-in-python
# http://docs.python-requests.org/en/master/user/quickstart/
# import requests
# url = 'https://...'
# payload = {'key1': 'value1', 'key2': 'value2'}
#
# # GET
# r = requests.get(url)
#
# # GET with params in URL
# r = requests.get(url, params=payload)
#
# # POST with form-encoded data
# r = requests.post(url, data=payload)
#
# # POST with form-encoded data and params
# r = requests.post(url, params=payload1, data=payload)

# # POST with JSON
# import json
# r = requests.post(url, json=payload)
#
# # Response, status etc
# r.text
# r.status_code


# importing the requests library
import requests

hostname = 'localhost'
port     = 5000

URL = f'http://{hostname}:{port}/get'

# defining a params dict for the parameters to be sent to the API
payload1 = {'name': 'madhu1'}
payload2 = {'name': 'madhu2','age':30}

r = requests.get(url=URL, params=payload1,data=payload2)
data = r.json()
print(type(r),type(data),data)

r = requests.post(url=URL, params=payload1,data=payload2)
data = r.json()
print(type(r),type(data),data)

r = requests.get(url=URL, params=payload1,json=payload2)
data = r.json()
print(type(r),type(data),data)

r = requests.post(url=URL, params=payload1,json=payload2)
data = r.json()
print(type(r),type(data),data)
