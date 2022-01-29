import pytest

from src.baseclasses.response_second import ResponseNew
from src.pydantic_schemas.user import User
from src.enums.global_enums import GlobalErrorMessage


# resp = requests.get(SERVICE_URL_2)
# print(resp.json())
# print(resp.__getstate__())

@pytest.mark.production
@pytest.mark.development
def test_getting_users_list(do_request, calculate, make_number):
    response = do_request
    test_object = ResponseNew(response)
    test_object.assert_status_code(200).validate(User)

    assert calculate(10, 15) == 25, GlobalErrorMessage.WRONG_NUMBER.value
    assert make_number < 9999, GlobalErrorMessage.WRONG_NUMBER.value


def test_users_say_hello(say_hello):
    assert say_hello == 14, GlobalErrorMessage.WRONG_NUMBER.value


@pytest.mark.production
@pytest.mark.skip('[ISSUE-2345] we don`t need this test now')
def test_another():
    assert 2 == 2, 'It`s not ok'


@pytest.mark.development
@pytest.mark.parametrize('value_one, value_two, result',[
    (1, 2, 3),
    (3, 3, 6),
    (4, 3, 7)
])
def test_calculation(calculate, value_one, value_two, result):
    assert calculate(value_one, value_two) == result


def test_fail():
    assert 1 == 2, 'It`s not ok'
