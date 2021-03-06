import requests

from configuration import SERVICE_URL

from src.baseclasses.response import Response
# from src.schemas.post import POST_SCHEMA
from src.pydantic_schemas.post import Post


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(Post)


def test_equal():
    assert 1 == 1, 'Numbers are not equal'


def test_is_not_equal():
    assert 1 != 2, 'Numbers are equal'
