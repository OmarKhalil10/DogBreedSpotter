"""
Send a request to flask application
"""
import requests

url = "https://flaskapp-cr-v1-yerjarnciq-ue.a.run.app"

# Method 1
resp = requests.get(f"{url}/", verify=False)
print(resp.content.decode())

# Method 2

r = requests.get("https://flaskapp-cr-v1-yerjarnciq-ue.a.run.app")
print(r)

# <Response [200]>
