import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

url = "https://httpbin.org/basic-auth/Evgeny/1234"
response = requests.get(url, auth=HTTPBasicAuth("Evgeny", "1234"))
print("Basic:", response.json())

url = "https://httpbin.org/digest-auth/auth/Evgeny/1234"
response = requests.get(url, auth=HTTPDigestAuth("Evgeny", "1234"))
print("Digest:", response.json())

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30"
url = "https://httpbin.org/bearer"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url, headers=headers)
print("Bearer:", response.json())
