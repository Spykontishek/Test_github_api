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

@allure.title('Позитивная проверка создания нового публичного репозитория, затем получение списка созданных репозиториев с подтверждением, что созданный репозиторий там присутствует и удаление данного репозитория')
@allure.description('Каждый запрос должен вернуть правильный код ответа и иметь необходимую информацию в теле ответа')
def test_create_check_delete_repository():
    headers = {"Authorization": "Bearer " + TOKEN, "X-GitHub-Api-Version": "2022-11-28", "Accept": "application/vnd.github+json"}
    data = {"name": REPOSITORY_NAME, "description": "This is your first repo!", "homepage": Data.MAIN_URL, "private": False, "is_template": True}
    response_reg = requests.post(Data.REG_REPO_URL, headers=headers, json=data)
    assert response_reg.status_code == 201
    assert 'id' in response_reg.text
    response = requests.get(Data.GET_LIST_OF_REPO_URL, headers=headers)
    assert response.status_code == 200
    assert REPOSITORY_NAME in response.text
    response_del = requests.delete(Data.DEL_REPO_URL + GITHUB_USERNAME + '/' + REPOSITORY_NAME, headers=headers)
    assert response_del.status_code == 204
