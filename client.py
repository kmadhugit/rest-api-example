# https://stackoverflow.com/questions/4476373/simple-url-get-post-function-in-python
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
# # POST with JSON
# import json
# r = requests.post(url, data=json.dumps(payload))
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
PARAMS = {'name': 'madhu'}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)
data = r.json()
print(type(r),type(data),data)


r = requests.post(url=URL, params=PARAMS)
data = r.json()
print(type(r),type(data),data)

