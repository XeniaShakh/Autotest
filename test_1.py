from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common import NoSuchElementException
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser \
        .get('https://www.saucedemo.com/')
    sleep(1)

    # введение доступов
    browser \
        .find_element(By.CSS_SELECTOR, "#user-name")   \
        .send_keys("standard_user")
    sleep(0.2)
    browser \
        .find_element(By.CSS_SELECTOR, "#password") \
        .send_keys("secret_sauce")
    sleep(0.2)

    # клик на Войти
    browser \
        .find_element(By.CSS_SELECTOR, "#login-button") \
        .click()
    sleep(1)

    return browser


def test_title(browser):
    assert browser.title == "Swag Labs"
    assert "Products" in browser.page_source


def test_login(browser):
    # 2клик на Войти
    try:
        browser \
            .find_element(By.CSS_SELECTOR, "#login-button")
        assert False
    except NoSuchElementException:
        assert True


def test_sort(browser):

    # Сортировка стрелочка
    browser \
        .find_element(By.CSS_SELECTOR, ".select_container") \
        .click()
    sleep(1)

    # Сортировка
    browser \
        .find_element(By.CSS_SELECTOR, ".product_sort_container") \
        .click()
    sleep(1)
    browser \
        .find_element(By.XPATH, '//option[contains(text(),"Name (Z to A)")]') \
        .click()
    sleep(1)


def test_add(browser):

    # Добавление товара
    browser \
        .find_element(By.XPATH, '//div[contains(text(),"Test.allTheThings() T-Shirt (Red)")]') \
        .find_element(By.XPATH, '//button[contains(text(),"Add to cart")]') \
        .click()
    sleep(1)

    # Переход на страницу товара
    browser \
        .find_element(By.XPATH, '//div[contains(text(),"Sauce Labs Onesie")]') \
        .click()
    sleep(1)

    # Добавление товара на странице товара
    browser \
        .find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie") \
        .click()
    sleep(1)

    # Возврат к каталогу товаров
    browser \
        .find_element(By.CSS_SELECTOR, "#back-to-products") \
        .click()
    sleep(1)

    # Переход в корзину
    browser \
        .find_element(By.CSS_SELECTOR, "#shopping_cart_container") \
        .click()
    sleep(1)

    # Проверка оплаты
    browser \
        .find_element(By.CSS_SELECTOR, "#checkout") \
        .click()
    sleep(1)

    # Введение данных
    browser \
        .find_element(By.CSS_SELECTOR, "#first-name")   \
        .send_keys("IVAN")
    sleep(0.2)
    browser \
        .find_element(By.CSS_SELECTOR, "#last-name") \
        .send_keys("IVANOV")
    sleep(0.2)
    browser \
        .find_element(By.CSS_SELECTOR, "#postal-code") \
        .send_keys("5555 2222 2222 5555")
    sleep(0.2)

    # Клик на продолжить
    browser \
        .find_element(By.CSS_SELECTOR, "#continue") \
        .click()
    sleep(3)

    # assert True
