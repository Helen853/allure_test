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

