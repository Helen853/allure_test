import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_github():
    with allure.step('Открываем главную страницу'):
        browser.open("https://github.com")

    with allure.step('Ищем репозиторий'):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Открывает таб issues'):
        s("#issues-tab").click()

    with allure.step('Проверяем наличие issues с номером 81'):
        s(by.partial_text("#81")).should(be.visible)


def steps_decorator_steps():
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

