import requests

r = requests.get("https://coreyms.com", verify=False)
print(r.status_code)
print(r.ok)