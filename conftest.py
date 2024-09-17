import pytest
import requests
import os
from dotenv import load_dotenv
from data import Data

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("TOKEN")
REPOSITORY_NAME = os.getenv("REPOSITORY_NAME")

@pytest.fixture
def reg():
    headers = {"Authorization": "Bearer " + TOKEN, "X-GitHub-Api-Version": "2022-11-28", "Accept": "application/vnd.github+json"}
    data = {"name": REPOSITORY_NAME, "description": "This is your first repo!", "homepage": Data.MAIN_URL, "private": False, "is_template": True}
    requests.post(Data.REG_REPO_URL, headers=headers, json=data)

@pytest.fixture
def reg_and_del():
    headers = {"Authorization": "Bearer " + TOKEN, "X-GitHub-Api-Version": "2022-11-28", "Accept": "application/vnd.github+json"}
    data = {"name": REPOSITORY_NAME, "description": "This is your first repo!", "homepage": Data.MAIN_URL, "private": False, "is_template": True}
    requests.post(Data.REG_REPO_URL, headers=headers, json=data)
    yield
    requests.delete(Data.DEL_REPO_URL + GITHUB_USERNAME + '/' + REPOSITORY_NAME, headers=headers)

