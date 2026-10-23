import sender_stand_request
import data


def get_kit_body(name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = name
    return kit_body


def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]


def positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == name


def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400


def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("a" * 511)


def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400(get_kit_body(""))


def test_create_kit_512_letters_in_name_get_error_response():
    negative_assert_code_400(get_kit_body("a" * 512))


def test_create_kit_special_symbols_in_name_get_success_response():
    positive_assert("№%@,")


def test_create_kit_spaces_in_name_get_success_response():
    positive_assert(" A Aaa ")


def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")


def test_create_kit_without_name_get_error_response():
    negative_assert_code_400({})


def test_create_kit_number_type_in_name_get_error_response():
    negative_assert_code_400(get_kit_body(123))
