import pytest
import allure
import requests
from conftest import reg
import os
from dotenv import load_dotenv
from data import Data

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("TOKEN")
REPOSITORY_NAME = os.getenv("REPOSITORY_NAME")

@allure.title('Позитивная проверка удаления репозитория')
@allure.description('Запрос должен вернуть правильный код ответа')
def test_delete_repository(reg):
    headers = {"Authorization": "Bearer " + TOKEN, "X-GitHub-Api-Version": "2022-11-28", "Accept": "application/vnd.github+json"}
    response = requests.delete(Data.DEL_REPO_URL+GITHUB_USERNAME+'/'+REPOSITORY_NAME, headers=headers)
    assert response.status_code == 204