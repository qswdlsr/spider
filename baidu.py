import requests
r = requests.get("https://www.baidu.com")
print(r.text)
print(r.status_code)
print(r.text)
