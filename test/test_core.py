import pytest
from api.core import *


def test_secret():
    secret = load_secrets("FOOBAR")
    print(secret)
    print(secret.get())


def test_client():
    client = make_client("OPENAI_API_KEY")
    print(client)
