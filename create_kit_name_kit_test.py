import pytest
import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def get_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(name):
    token = get_user_token()
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == name

def negative_assert(name):
    token = get_user_token()
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("a" * 511)

@pytest.mark.xfail(reason="La API no valida la longitud minima del nombre")
def test_create_kit_empty_name_get_error_response():
    negative_assert("")

@pytest.mark.xfail(reason="La API no valida la longitud maxima del nombre")
def test_create_kit_512_letters_in_name_get_error_response():
    negative_assert("a" * 512)

def test_create_kit_allow_english_letters_get_success_response():
    positive_assert("Aaa")

def test_create_kit_allow_russian_letters_get_success_response():
    positive_assert("Мария")

def test_create_kit_has_special_symbols_get_success_response():
    positive_assert("№%@")

def test_create_kit_has_spaces_get_success_response():
    positive_assert(" A Aaa ")

def test_create_kit_has_numbers_get_success_response():
    positive_assert("123")

