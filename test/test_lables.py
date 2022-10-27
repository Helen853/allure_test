import allure
from allure_commons.types import Severity
from selene import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'eroshenkoam')
@allure.feature('Задачи в репозитоории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#81")


@allure.step('Открываем декоратор')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозитория {repo}')
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text("eroshenkoam/allure-example")).click()


@allure.step('Открываем таб Issues')
def open_issue_tab():
    s("#issues-tab").click()


@allure.step('Проверяем наличие Issue с номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
