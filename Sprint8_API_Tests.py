def test_example():
    assert 2 + 2 == 4

import requests

# Reemplaza esta URL con la de tu API real
URL = "https://api.example.com/v1/kits"
HEADERS = {"Content-Type": "application/json"}

def test_create_kit_with_1_char():
    kit_body = {"name": "a"}
    response = requests.post(URL, json=kit_body, headers=HEADERS)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def test_create_kit_with_511_chars():
    kit_body = {"name": "a" * 511}
    response = requests.post(URL, json=kit_body, headers=HEADERS)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def test_create_kit_with_0_chars():
    kit_body = {"name": ""}
    response = requests.post(URL, json=kit_body, headers=HEADERS)
    assert response.status_code == 400

def test_create_kit_with_512_chars():
    kit_body = {"name": "a" * 512}
    response = requests.post(URL, json=kit_body, headers=HEADERS)
    assert response.status_code == 400

def test_create_kit_with_special_chars():
    kit_body = {"name": "№%@"}
    response = requests.post(URL, json=kit_body, headers=HEADERS)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def test_create_kit_with_spaces():
    kit_body = {"name": " A Aaa "}
    response = requests.post(URL, json=kit_body, headers=HEADERS)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def test_create_kit_with_numbers():
    kit_body = {"name": "123"}
    response = requests.post(URL, json=kit_body, headers=HEADERS)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def test_create_kit_without_name_field():
    kit_body = {}
    response = requests.post(URL, json=kit_body, headers=HEADERS)
    assert response.status_code == 400

def test_create_kit_with_number_as_name():
    kit_body = {"name": 123}
    response = requests.post(URL, json=kit_body, headers=HEADERS)
    assert response.status_code == 400

C:\Users\usuario\projects\qa-project-Urban-Grocers-app-es


On branch main
Your branch is up to date with 'origin/main'.
    configuration.py

    data.py

    sender_stand_request.py

    create_kit_name_kit_test.py

    README.md

    .gitignore

UrbanGrocersClean/
│
├── configuration.py
├── data.py
├── sender_stand_request.py
├── create_kit_name_kit_test.py
├── README.md
└── .gitignore

File → Open...

