

import requests
# obj = requests.get('http://api.conceptnet.io/c/en/bike').json()
# print(obj['edges'])

json_format = {'value':123}
obj = requests.post('http://0.0.0.0:3000/test_post',json=json_format)
print(obj.text)