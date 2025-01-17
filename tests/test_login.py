import pytest
import allure


@allure.epic("Web interface")
@allure.feature("Авторизация")
@allure.story("Login Feature")
@allure.title("Авторизаиця с недействительными учетными данными")
@allure.description("Описание теста")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_failure(login_page):
    with allure.step('Открыть страницу авторизации'): #вот так можно красиво описать шаги
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
       login_page.login('invalid_user', 'invalid_password')
    with allure.step('Url не изменился'):
        assert login_page.url == 'https://zimaev.github.io/pom/'
    with allure.step('Отображается ошибка - Invalid credentials. Please try again.'):
        assert login_page.get_error_message() == 'Invalid credentials. Please try again.'

@allure.feature('Login')
@allure.story('Login with valid credentials')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиця с корректными учетными данными')
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(login_page, dashboard_page, username, password):
    login_page.navigate()
    login_page.login('admin', 'admin')

    dashboard_page.assert_welcome_message("Welcome admin")

# from pages.login_page import LoginPage
# from pages.dashboard_page import DashboardPage

# def test_login_failure(page):
#     login_page = LoginPage(page)
#     login_page.navigate()
#     login_page.login('invalid_user', 'invalid_password')
#     assert login_page.get_error_message() == 'Invalid credentials. Please try again.'
#
#
# @pytest.mark.parametrize('username, password', [
#     ('user', 'user'),
#     ('admin', 'admin')
# ])
# def test_login_success(page, username, password):
#     login_page = LoginPage(page)
#     dashboard_page = DashboardPage(page)
#
#     login_page.navigate()
#     login_page.login(username, password)
#
#     dashboard_page.assert_welcome_message(f"Welcome {username}")
#
#     dashboard_page.assert_welcome_message("Welcome admin")