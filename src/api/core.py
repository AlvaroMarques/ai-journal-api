import requests
import os


from api.models import *
from openai import OpenAI
from dotenv import load_dotenv


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
