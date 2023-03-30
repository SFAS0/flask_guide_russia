import requests

url = 'http://127.0.0.1:5000/api/jobs'
json_data = {
    'id': 10,
    'job': 'Инженер ракетчик',
    'work_size': 24, "collaborators": '2, 3',
    "is_finished": False,
    "team_leader": 1
}
response = requests.post(url=url, json=json_data)
print(response.json())

# id уже существует
url = 'http://127.0.0.1:5000/api/jobs'
json_data = {
    'id': 10,
    'job': 'Инженер ракетчик',
    'work_size': 24, "collaborators": '2, 3',
    "is_finished": False,
    "team_leader": 1
}
response = requests.post(url=url, json=json_data)
print(response.json())

# не хватает id
url = 'http://127.0.0.1:5000/api/jobs'
json_data = {
    'job': 'Инженер ракетчик',
    'work_size': 24, "collaborators": '2, 3',
    "is_finished": False,
    "team_leader": 1
}
response = requests.post(url=url, json=json_data)
print(response.json())
# пустой запрос
url = 'http://127.0.0.1:5000/api/jobs'
json_data = {}
response = requests.post(url=url, json=json_data)
print(response.json())
