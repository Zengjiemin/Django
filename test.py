import requests

res = requests.post('http://localhost:8000/add_student', data={"age":"10", "name":"name"})
print(res.text)
