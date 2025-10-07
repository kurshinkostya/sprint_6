import allure
from utils.urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    @allure.step("Инициализация BasePage")
    def __init__(self, driver):
        self.driver = driver

    # поиск элементов 

    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не найден элемент по локатору: {locator}"
        )

    @allure.step("Найти все элементы по локатору: {locator}")
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не найдены элементы по локатору: {locator}"
        )

    # проверки и ожидания 

    @allure.step("Проверить, что элемент видим: {locator}")
    def is_element_visible(self, locator, time=5) -> bool:
        """Возвращает True, если элемент видим, иначе False."""
        try:
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить, что элемент кликабелен: {locator}")
    def is_element_clickable(self, locator, time=5) -> bool:
        """Возвращает True, если элемент кликабелен."""
        try:
            WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидать, пока элемент исчезнет: {locator}")
    def wait_until_invisible(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    # работа с окнами и страницами 

    @allure.step("Перейти по адресу: {url}")
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.MAIN_PAGE
        self.driver.get(url)

    @allure.step("Получить текущий URL страницы")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на вкладку браузера с индексом {window_number}")
    def switch_to_window(self, window_number: int = 0):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step("Ожидать, пока URL перестанет быть 'about:blank'")
    def wait_until_url_not_blank(self, time=10):
        WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))

    # универсальные действия

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator, time=10):
        """Безопасный клик по элементу."""
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не кликабелен: {locator}"
        )
        element.click()

    @allure.step("Ввод текста '{text}' в поле: {locator}")
    def input_text(self, locator, text, time=10):
        """Очистить поле и ввести текст."""
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)
