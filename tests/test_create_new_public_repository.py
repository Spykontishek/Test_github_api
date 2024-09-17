import pytest
import allure
import requests
import os
from dotenv import load_dotenv
from data import Data

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("TOKEN")
REPOSITORY_NAME = os.getenv("REPOSITORY_NAME")

@allure.title('Позитивная проверка создания нового публичного репозитория')
@allure.description('Запрос должен вернуть правильный код и и иметь "id" в теле ответа')
def test_create_repository():
    headers = {"Authorization": "Bearer " + TOKEN, "X-GitHub-Api-Version": "2022-11-28", "Accept": "application/vnd.github+json"}
    data = {"name": REPOSITORY_NAME, "description": "This is your first repo!", "homepage": Data.MAIN_URL, "private": False, "is_template": True}
    response = requests.post(Data.REG_REPO_URL, headers=headers, json=data)
    assert response.status_code == 201
    assert 'id' in response.text

    requests.delete(Data.DEL_REPO_URL + GITHUB_USERNAME + '/' + REPOSITORY_NAME, headers=headers)

