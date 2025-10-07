import pytest
import allure
from pages.home_page import YaScooterHomePage
from pages.order_page import YaScooterOrderPage
from utils.urls import Urls
from utils.test_data import YaScooterOrderPageData as order_data

@allure.epic("Создание заказа")
class TestYaScooterOrderPage:

    @pytest.mark.parametrize("data_set", ["data_set1", "data_set2"])
    @allure.title("Проверка полного оформления заказа")
    def test_complete_order_flow(self, driver, data_set):
        home = YaScooterHomePage(driver)
        page = YaScooterOrderPage(driver)

        page.go_to_site(Urls.ORDER_PAGE)
        home.click_cookie_accept()

        # заполняем данные пользователя
        page.fill_user_data(order_data.data_sets[data_set])
        page.go_next()

        # заполняем данные аренды
        page.fill_rent_data(order_data.data_sets[data_set])

        # заказываем
        page.click_order()
        page.click_accept_order()

        order_number = page.get_order_number()
        assert order_number, "Номер заказа не получен"
