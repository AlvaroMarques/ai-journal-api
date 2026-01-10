import pytest
from api.core import *


def test_secret():
    secret = load_secrets("FOOBAR")
    print(secret)
    print(secret.get())


def test_client():
    client = make_client("OPENAI_API_KEY")
    model_name = "gpt-4.1-nano-2025-04-14"
    prompt = "Hello!"
    print(get_response(client, model_name, prompt))
