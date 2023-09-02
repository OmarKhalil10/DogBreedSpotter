"""
Send a request to flask application

Since we have 1 Flask methods, we shall send 1 requests to dog-breed-spotte.
"""
import requests

url = "https://dog-breed-spotter-t6mbhrffxa-oa.a.run.app"

# Method
resp = requests.get(f"{url}/", verify=False)
print(resp.content.decode())

# <Response [index.html content]>

# Method [live check]
r = requests.get(f"{url}/")
print(r)

# <Response [200]>