import pytest
from api.core import *
from importlib.resources import files


def test_secret():
    secret = load_secrets("FOOBAR")
    print(secret)
    print(secret.get())


def test_client():
    client = make_client("OPENAI_API_KEY")
    model_name = load_model_name("API_MODEL_ID")
    print(model_name)
    prompt = (files("api.prompts") / "00.md").read_text()
    print(prompt)

    print(get_response(client, model_name, prompt))
