# https://stepik.org/lesson/237240/step/9?unit=209628
# 3.6.9 Задание: запуск автотестов для разных языков интерфейса
# import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_cart_button_is_present(browser):
    browser.get(link)
    # time.sleep(10)

    # проверка на наличие кнопки:
    button = browser.find_element_by_class_name('btn-add-to-basket')
    assert button is not None, 'The button is absent'
