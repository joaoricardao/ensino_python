import requests
response = requests.get('http://ifpb.edu.br/')
response.ok
response.text[:40000]
