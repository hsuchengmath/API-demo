

import requests
# obj = requests.get('http://api.conceptnet.io/c/en/bike').json()
# print(obj['edges'])

json_format = {'value':123}
obj = requests.post('https://hsucheng-api-test.herokuapp.com/test_post',json=json_format)
print(type(obj.))