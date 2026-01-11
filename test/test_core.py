import pytest
from api.core import *
from importlib.resources import files
from pathlib import Path


class FakeResponse(dict):
    def __init__(self, data: dict):
        super().__init__(data)
        self.model = data.get("model", "test-model")

    @property
    def output_text(self) -> str:
        texts = []
        for item in self.get("output", []):
            if item.get("type") == "message":
                for block in item.get("content", []):
                    if block.get("type") == "output_text":
                        texts.append(block.get("text", ""))
        return "".join(texts)


@pytest.fixture()
def openai_hello_world_response_text():
    with open(Path(__file__).parent / "data" / "openai.json") as openai_json:
        return json.load(openai_json)


@pytest.fixture()
def openai_hello_world_response_obj(openai_hello_world_response_text):
    return FakeResponse(openai_hello_world_response_text)


def test_secret():
    secret = load_secrets("FOOBAR")
    print(secret)
    print(secret.get())


def test_client(monkeypatch, openai_hello_world_response_obj):
    client = make_client("OPENAI_API_KEY")

    monkeypatch.setattr(
        client.responses,
        "create",
        lambda *args, **kwargs: openai_hello_world_response_obj,
    )

    model_name = load_model_name("API_MODEL_ID")
    prompt = (files("api.prompts") / "01.md").read_text()
    json_path = Path(__file__).parent / "data" / "output.json"

    responses = make_journal_prompt(client, model_name, prompt, json_path)

    for response in responses:
        print(response)
        print(get_journal_entry(response))
