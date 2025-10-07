import pytest
import allure
from pages.home_page import YaScooterHomePage
from pages.order_page import YaScooterOrderPage
from utils.urls import Urls
from utils.test_data import YaScooterOrderPageData as order_data

@allure.epic("Домашняя страница")
@allure.suite("Флоу заказа с главной страницы")
class TestYaScooterFullOrderFlow:

    @pytest.mark.parametrize("button", ["top", "bottom"])
    @pytest.mark.parametrize("data_set", ["data_set1", "data_set2"])
    @allure.title("Полный флоу заказа через {button} кнопку с набором данных {data_set}")
    def test_full_order_flow_from_home(self, driver, button, data_set):
        home_page = YaScooterHomePage(driver)
        order_page = YaScooterOrderPage(driver)

        home_page.go_to_site()
        home_page.click_cookie_accept()

        if button == "top":
            home_page.click_top_order_button()
        else:
            home_page.click_bottom_order_button()

        # проверка перехода на страницу заказа
        assert order_page.current_url() == Urls.ORDER_PAGE

        # заполнение данных пользователя
        order_page.fill_user_data(order_data.data_sets[data_set])
        order_page.go_next()

        # заполнение данных аренды
        order_page.fill_rent_data(order_data.data_sets[data_set])

        # заказ и получение номера
        order_page.click_order()
        order_page.click_accept_order()
        order_number = order_page.get_order_number()
        assert order_number, "Номер заказа не получен"
