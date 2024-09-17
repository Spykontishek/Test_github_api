import pytest
import allure
import requests
from conftest import reg_and_del
import os
from dotenv import load_dotenv
from data import Data

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("TOKEN")
REPOSITORY_NAME = os.getenv("REPOSITORY_NAME")

@allure.title('Позитивная проверка получения информации о созданном репозитории')
@allure.description('Запрос должен вернуть правильный код и и иметь "id" в теле ответа')
def test_get_list_of_repositories(reg_and_del):
    headers = {"Authorization": "Bearer " + TOKEN, "X-GitHub-Api-Version": "2022-11-28", "Accept": "application/vnd.github+json"}
    response = requests.get(Data.GET_LIST_OF_REPO_URL, headers=headers)
    assert response.status_code == 200
    assert REPOSITORY_NAME in response.text