import requests
url = 'http://127.0.0.1:5000/gen?len=12'
r = requests.get(url)
assert r.status_code == 201
assert len(r.content) == 12

url = 'http://127.0.0.1:5000/gen?len=-12'
r = requests.get(url)
assert r.status_code == 201
# assert len(r.content) == 12

url = 'http://127.0.0.1:5000/gen?len=-12abc'
