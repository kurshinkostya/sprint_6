import allure
from pages.base_page import BasePage
from utils.locators import YaScooterOrderPageLocator as Locators

class YaScooterOrderPage(BasePage):

    # ввод пользовательских данных 
    @allure.step("Ввести имя: {first_name}")
    def input_first_name(self, first_name):
        self.find_element(Locators.FIRST_NAME_INPUT).send_keys(first_name)

    @allure.step("Ввести фамилию: {last_name}")
    def input_last_name(self, last_name):
        self.find_element(Locators.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step("Ввести адрес: {address}")
    def input_address(self, address):
        self.find_element(Locators.ADDRESS_INPUT).send_keys(address)

    @allure.step("Ввести метро: {subway}")
    def input_subway(self, subway):
        self.find_element(Locators.SUBWAY_FIELD).send_keys(subway)
        self.find_element(Locators.SUBWAY_HINT_BUTTON(subway)).click()

    @allure.step("Ввести телефон: {telephone}")
    def input_telephone_number(self, telephone):
        self.find_element(Locators.TELEPHONE_NUMBER_FIELD).send_keys(telephone)

    @allure.step("Нажать 'Далее'")
    def go_next(self):
        self.find_element(Locators.NEXT_BUTTON).click()

    # ввод аренды 
    @allure.step("Заполнить данные аренды")
    def fill_rent_data(self, data):
        # выбор даты
        self.find_element(Locators.DATE_FIELD).send_keys(data['date'])

        # выбор периода аренды
        self.find_element(Locators.RENTAL_PERIOD_FIELD).click()
        options = self.find_elements(Locators.RENTAL_PERIOD_LIST)
        options[data['rental_period']].click()

        # выбор цвета
        checkboxes = self.find_elements(Locators.COLOR_CHECKBOXES)
        for index in data['color']:
            checkboxes[index].click()

        # комментарий для курьера
        self.find_element(Locators.COMMENT_FOR_COURIER_FIELD).send_keys(data['comment_for_courier'])

    @allure.step("Нажать 'Заказать'")
    def click_order(self):
        self.find_element(Locators.ORDER_BUTTON).click()

    @allure.step("Принять заказ")
    def click_accept_order(self):
        self.find_element(Locators.ACCEPT_ORDER_BUTTON).click()

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.find_element(Locators.ORDER_COMPLETED_INFO).text

    @allure.step("Заполнить данные пользователя")
    def fill_user_data(self, data):
        self.input_first_name(data['first_name'])
        self.input_last_name(data['last_name'])
        self.input_address(data['address'])
        self.input_subway(data['subway_name'])
        self.input_telephone_number(data['telephone'])

    # проверка ошибок
    def is_first_name_error_displayed(self):
        return self.is_element_visible(Locators.INCORRECT_FIRST_NAME_MESSAGE)

    def is_last_name_error_displayed(self):
        return self.is_element_visible(Locators.INCORRECT_LAST_NAME_MESSAGE)

    def is_address_error_displayed(self):
        return self.is_element_visible(Locators.INCORRECT_ADDRESS_MESSAGE)

    def is_subway_error_displayed(self):
        return self.is_element_visible(Locators.INCORRECT_SUBWAY_MESSAGE)

    def is_telephone_error_displayed(self):
        return self.is_element_visible(Locators.INCORRECT_TELEPHONE_NUMBER_MESSAGE)
