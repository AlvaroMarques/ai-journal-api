import requests
import os


from api.models import Secret, JournalEntry
from openai import OpenAI
from openai.types.responses import Response
from dotenv import load_dotenv
from pathlib import PosixPath
from typing import List
import json


def load_secrets(env_var_name: str) -> Secret:
    load_dotenv()
    api_key = os.getenv(env_var_name)

    return Secret(api_key)


def load_model_name(env_var_name) -> str:
    load_dotenv()

    return os.getenv(env_var_name)


def make_client_from_secret(secret: Secret) -> OpenAI:
    return OpenAI(api_key=secret.get())


def make_client(env_var_name: str) -> OpenAI:
    secret = load_secrets(env_var_name)
    return make_client_from_secret(secret)


def get_response(client: OpenAI, model_name: str, prompt: str):

    resp = client.responses.create(model=model_name, input=prompt)

    return resp


def make_journal_prompt(
    client: OpenAI, model_name: str, prompt_md: str, json_path: PosixPath
) -> List[Response]:
    with open(json_path, "r") as json_f:
        json_information = json.load(json_f)

    responses = []
    for metadata in json_information:
        prompt = "\n".join([prompt_md, json.dumps(metadata)])
        responses.append(get_response(client, model_name, prompt))
    return responses


def get_journal_entry(response: Response) -> JournalEntry:

    return JournalEntry(
        model_name=response.model,
        journal_entry=response.output_text,
        links_accessed=None,
    )
