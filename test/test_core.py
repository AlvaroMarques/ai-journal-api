import pytest
from api.core import *
from importlib.resources import files
from pathlib import Path


def test_secret():
    secret = load_secrets("FOOBAR")
    print(secret)
    print(secret.get())


def test_client():
    client = make_client("OPENAI_API_KEY")
    model_name = load_model_name("API_MODEL_ID")
    print(model_name)
    prompt = (files("api.prompts") / "01.md").read_text()
    json_information_path = Path(__file__).parent / "data" / "output.json"
    with open(json_information_path, "r") as json_f:
        json_information = json_f.read()

    prompt = "\n".join([prompt, json_information])
    print(prompt)

    print(get_response(client, model_name, prompt))
