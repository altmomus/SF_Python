# Основной тестовый файл (все функции теста находятся в этом файле).
from os import terminal_size
from TmallPages import SearchHelper
from selenium import webdriver
import time


# Проверяем работает ли (првильно ли загрузился) сайт.
# Для этого нажимаем на одну из кнопок сайта. 
# Если кнопка нажимается значит сайт правильно загрузился и работает как положено.
def test_tmall_1(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    button = tmall_main_page.find_navigation_button()
    checking = False
    try:
        # Если кнопка нажимается то значение переменной checking меняется на True.
        button.click()
        checking = True
    except:
        # Если такой кнопки нет либо же он не нажимается то значение переменной checking остается False.
        pass
    # Исходя из значении переменной checking результат будет True либо False.
    assert checking


# Проверяем есть ли навигационный бар в сайте.
# Проверяем также есть ли необходимые нам категории товаров (в нашем случае "Электроника" и "Бытовая техника").
def test_tmall_2(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    elements = tmall_main_page.check_navigation_bar()
    print(elements)
    assert "Электроника" and "Бытовая техника" in elements


# Проверяем есть ли необходимые нам категории товаров (в этом случае "Картинки" и "Видео").
# Этот тест будет отрицательным т.к. в навигационном баре нет элементов "Картинки" и "Видео".
def test_tmall_3(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    elements = tmall_main_page.check_navigation_bar()
    assert "Картинки" and "Видео" in elements


# Проверяем есть ли кнопка поиска и функционирует (нажимается) ли.
def test_tmall_4(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    search_button = tmall_main_page.find_search_button()
    checking = False
    try:
        # Если кнопка нажимается то значение переменной checking меняется на True.
        search_button.click()
        checking = True
    except:
        # Если такой кнопки нет либо же он не нажимается то значение переменной checking остается False.
        pass
    # Исходя из значении переменной checking результат будет True либо False.
    assert checking


# Проверяем есть ли кнопка доставки и функционирует (нажимается) ли.
def test_tmall_5(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    shipping_button = tmall_main_page.find_shipping_button()
    checking = False
    try:
        # Если кнопка нажимается то значение переменной checking меняется на True.
        shipping_button.click()
        checking = True
    except:
        # Если такой кнопки нет либо же он не нажимается то значение переменной checking остается False.
        pass
    # Исходя из значении переменной checking результат будет True либо False.
    assert checking


# Проверяем есть ли кнопки первого слайдера и проверяем их на работоспособность.
def test_tmall_6(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    first_slider_buttons = tmall_main_page.find_first_slider_buttons()
    checking_right_button = False
    checking_left_button = False
    try:
        # Если кнопки функционируют то значение переменных checking_right_button
        # и checking_left_button меняются на True.
        first_slider_buttons[0].click()
        time.sleep(2.5)
        checking_right_button = True
        first_slider_buttons[1].click()
        time.sleep(2.5)
        checking_left_button = True
    except:
        # Если такой кнопки нет переменные остаюстся False.
        pass
    # Исходя из значении переменных после тест проверяем их.
    assert checking_right_button and checking_left_button == True


# Проверяем есть ли кнопки второго слайдера и проверяем их на работоспособность.
def test_tmall_7(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    second_slider_button = tmall_main_page.find_second_slider_button()
    # Наводим мышку selenium-а на элемент.
    # Внимание: В это время держите свой курсор мыши вне окны браузера selenium,
    # иначе результат будет False (отрицательным).
    action = webdriver.ActionChains(browser)
    action.move_to_element(second_slider_button)
    action.perform()
    checking = False
    try:
        # По умолчанию второй слайдер движется вправо, поэтому проверяем его нажав 5 раз его левую кнопку.
        # Только после 5 безошибочных нажатии даем переменной checking значение True.
        for _ in range(5):
            second_slider_button.click()
            time.sleep(1.1)
        time.sleep(2)
        checking = True
    except:
        # Если такой кнопки нет значение переменной остается False.
        pass
    # Исходя из значении переменной checking после теста проверяем его.
    assert checking


# Проверяем работает ли пойск по сайту (ищем через пойск 'Ботинки').
def test_tmall_8(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Ботинки")
    tmall_main_page.find_search_button().click()
    elements = tmall_main_page.find_items_of_search()
    assert len(elements) > 0


# Тестируем найдет ли пойск товар с названием 'wadasdwadsg4sfdfesf'.
# Этот тест должен вернуть значение False.
def test_tmall_9(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("wadasdwadsg4sfdfesf")
    tmall_main_page.find_search_button().click()
    elements = tmall_main_page.find_items_of_search()
    assert len(elements) > 0


# Тестируем отображается ли счетчик найденных товаров (т.е. сколько искомых товаров было найдено).
def test_tmall_10(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Ботинки")
    tmall_main_page.find_search_button().click()
    symbols = tmall_main_page.find_counter_value()
    if symbols.text != None:
        assert True
    else:
        assert False


# Тестируем этот же счетчик на пойск "wadasdwadsg4sfdfesf".
# Данный тест должен быть отрицательным.
def test_tmall_11(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("wadasdwadsg4sfdfesf")
    tmall_main_page.find_search_button().click()
    symbols = tmall_main_page.find_counter_value()
    if symbols.text != None:
        assert True
    else:
        assert False


# Тестируем отображается ли панель сортировки.
def test_tmall_12(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Робот пылесос")
    tmall_main_page.find_search_button().click()
    sort_bar = tmall_main_page.find_sort_bar()
    if sort_bar.text != None:
        assert True
    else:
        assert False


# Тестируем удаление рекламы скидки 2$.
def test_tmall_13(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Робот пылесос")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
        assert True
    else:
        assert False


# Тестируем нажимаются ли кнопка "По заказам" панели сортировки.
def test_tmall_14(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Мультиварка")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    check_first_button = False
    try:
        tmall_main_page.find_by_orders_button().click()
        check_first_button = True
    except:
        pass
    assert check_first_button


# Тестируем нажимаются ли кнопка "Новинки" панели сортировки.
def test_tmall_15(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Велосипед")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    check_first_button = False
    try:
        tmall_main_page.find_new_items_button().click()
        check_first_button = True
    except:
        pass
    assert check_first_button


# Тестируем нажимаются ли кнопка "Цена" панели сортировки.
def test_tmall_16(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Аккумулятор")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    check_first_button = False
    try:
        tmall_main_page.find_price_button().click()
        check_first_button = True
    except:
        pass
    assert check_first_button


# Тестируем правильно ли работает переход по товарам.
def test_tmall_17(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Сковородка")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    checking = False
    if add != None:
        add.click()
    item_link = tmall_main_page.find_item_link()
    try:
        item_link.click()
        checking = True
    except:
        pass
    assert checking


# Тестируем отображается ли название у товара.
def test_tmall_18(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Аккумулятор")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    item_title = tmall_main_page.find_item_title()
    if item_title.text != None:
        assert True
    else:
        assert False


# Тестируем отображается ли цена у товара.
def test_tmall_19(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Аккумулятор")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    item_price = tmall_main_page.find_item_price()
    if item_price.text != None:
        assert True
    else:
        assert False


# Тестируем отображается ли счетчик продажи товаров.
def test_tmall_20(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Перчатки")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    item_salve_value = tmall_main_page.find_item_salve_value()
    if item_salve_value.text != None:
        assert True
    else:
        assert False


# Тестируем есть ли картинка товара.
def test_tmall_21(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Перчатки")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    item_image = tmall_main_page.find_item_image()
    if item_image != None:
        assert True
    else:
        assert False


# Тестируем есть ли рейтинг товара.
def test_tmall_22(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Перчатки")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    item_rating = tmall_main_page.find_item_rating()
    if item_rating.text != None:
        assert True
    else:
        assert False


# Проверяем есть ли название компании в товаре.
def test_tmall_23(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Куртки")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    item_company = tmall_main_page.find_item_company()
    if item_company.text != None:
        assert True
    else:
        assert False


# Проверяем категорию электроника на работоспособность.
def test_tmall_24(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    electronic_category = tmall_main_page.find_nav_categories()[0]
    checking = False
    try:
        electronic_category.click()
        checking = True
    except:
        pass
    assert checking


# Тестируем категорию бытовая техника на работоспособность.
def test_tmall_25(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    appliances_category = tmall_main_page.find_nav_categories()[1]
    checking = False
    try:
        appliances_category.click()
        checking = True
    except:
        pass
    assert checking


# Тестируем категорию дом и сад на работоспособность.
def test_tmall_26(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    huose_and_garden_category = tmall_main_page.find_nav_categories()[2]
    checking = False
    try:
        huose_and_garden_category.click()
        checking = True
    except:
        pass
    assert checking


# Тестируем категорию детям и мам на работоспособность.
def test_tmall_27(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    children_and_mothers_category = tmall_main_page.find_nav_categories()[3]
    checking = False
    try:
        children_and_mothers_category.click()
        checking = True
    except:
        pass
    assert checking


# Тестируем категорию мода на работоспособность.
def test_tmall_28(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    fashion_category = tmall_main_page.find_nav_categories()[4]
    checking = False
    try:
        fashion_category.click()
        checking = True
    except:
        pass
    assert checking


# Тестируем категорию супермаркет на работоспособность.
def test_tmall_29(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    supermarket_category = tmall_main_page.find_nav_categories()[5]
    checking = False
    try:
        supermarket_category.click()
        checking = True
    except:
        pass
    assert checking


# Тестируем категорию автотовары на работоспособность.
def test_tmall_30(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    car_goods_category = tmall_main_page.find_nav_categories()[6]
    checking = False
    try:
        car_goods_category.click()
        checking = True
    except:
        pass
    assert checking


# Тестируем слайдер категории электроника на работоспособность.
def test_tmall_31(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.find_nav_categories()[0].click()
    slider_photo = tmall_main_page.find_electronic_category_slider_photo()
    if slider_photo != None:
        assert True
    else:
        assert False


# Проверяем отображается ли картинка категории бытовая техника на работоспособность.
def test_tmall_32(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.find_nav_categories()[1].click()
    slider_photo = tmall_main_page.find_appliances_category_slider_photo()
    if slider_photo != None:
        assert True
    else:
        assert False


# Проверяем отображается ли картинка категории дом и сад на работоспособность.
def test_tmall_33(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.find_nav_categories()[2].click()
    slider_photo = tmall_main_page.find_house_garden_category_slider_photo()
    if slider_photo != None:
        assert True
    else:
        assert False


# Проверяем отображается ли картинка категории детям и мам на работоспособность.
def test_tmall_34(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.find_nav_categories()[3].click()
    slider_photo = tmall_main_page.find_children_mothers_category_slider_photo()
    if slider_photo != None:
        assert True
    else:
        assert False


# Проверяем отображается ли картинка категории мода на работоспособность.
def test_tmall_35(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.find_nav_categories()[4].click()
    slider_photo = tmall_main_page.find_fashion_category_slider_photo()
    if slider_photo != None:
        assert True
    else:
        assert False


# Проверяем отображается ли картинка категории супермаркет на работоспособность.
def test_tmall_36(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.find_nav_categories()[5].click()
    slider_photo = tmall_main_page.find_supermarket_category_slider_photo()
    if slider_photo != None:
        assert True
    else:
        assert False


# Проверяем отображается ли картинка категории супермаркет на работоспособность.
def test_tmall_37(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.find_nav_categories()[6].click()
    slider_photo = tmall_main_page.find_car_goods_category_slider_photo()
    if slider_photo != None:
        assert True
    else:
        assert False


# Проверяем подходит ли нам цена товара (ищем товар с меньшей наценкой (цена < 5000)).
# Тест будет положительным если цена товара будет меньше 5000.
def test_tmall_38(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Танк тигр металл")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    item_price = tmall_main_page.find_item_price()
    index = item_price.text.find(',')
    if int(item_price.text[:index].replace(' ', '')) < 5000:
        assert True
    else:
        assert False


# Проверяем еще раз подходит ли нам цена товара (ищем товар с большей наценкой (цена > 5000)).
# Тест будет отрицательным если цена товара будет равно или меньше 5000.
def test_tmall_39(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Танк тигр металл")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    item_price = tmall_main_page.find_item_price()
    index = item_price.text.find(',')
    if int(item_price.text[:index].replace(' ', '')) > 5000:
        assert True
    else:
        assert False


# Проверяем подходит ли нам цена товара (ищем товар с меньшей наценкой (цена < 400)).
# Тест будет положительным если цена товара будет меньше 400.
def test_tmall_40(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Чехол на айфон 12")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    item_price = tmall_main_page.find_item_price()
    index = item_price.text.find(',')
    if int(item_price.text[:index].replace(' ', '')) < 1000:
        assert True
    else:
        assert False


# Проверяем еще раз подходит ли нам цена товара (ищем товар с большей наценкой (цена > 400)).
# Тест будет отрицательным если цена товара будет равно или меньше 400.
def test_tmall_41(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Чехол на айфон 12")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    item_price = tmall_main_page.find_item_price()
    index = item_price.text.find(',')
    if int(item_price.text[:index].replace(' ', '')) > 400:
        assert True
    else:
        assert False


# Проверяем подходит ли нам цена товара (ищем товар с меньшей наценкой (цена < 2000)).
# Тест будет положительным если цена товара будет меньше 2000.
def test_tmall_42(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Кулер для процессора")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    item_price = tmall_main_page.find_item_price()
    index = item_price.text.find(',')
    if int(item_price.text[:index].replace(' ', '')) < 2000:
        assert True
    else:
        assert False


# Проверяем подходит ли нам цена товара (ищем товар с большей наценкой (цена > 10000)).
# Тест будет отрицательным если цена товара будет равно или меньше 10000.
def test_tmall_43(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Видеокарта gtx 1650")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    item_price = tmall_main_page.find_item_price()
    index = item_price.text.find(',')
    if int(item_price.text[:index].replace(' ', '')) > 10000:
        assert True
    else:
        assert False


# Проверяем отображается ли поле сортировки по брендам.
def test_tmall_44(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Видеокарта gtx 1650")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    brand_choice = tmall_main_page.find_item_brand_choice()[0]
    if brand_choice != None:
        assert True
    else:
        assert False


# Проверяем правильно ли отображаются тексты фильтров "Тип" на товаре "Кулер для процессора".
def test_tmall_45(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Кулер для процессора")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    elements = tmall_main_page.find_item_brand_choice()[1].text
    assert "Теплопроводящая штукатурка" and "Водяное охлаждение" in elements


# Проверяем правильно ли отображаются тексты фильтров "Материал радиатора" на товаре "Кулер для процессора".
def test_tmall_46(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Кулер для процессора")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    elements = tmall_main_page.find_item_brand_choice()[2].text
    assert "Другое" and "Пластик" and "Медь" in elements


# Проверяем правильно ли отображаются тексты фильтров "Размера вентилятора" на товаре "Кулер для процессора".
def test_tmall_47(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Кулер для процессора")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    elements = tmall_main_page.find_item_brand_choice()[3].text
    assert "92x92x25 мм" and "120x120x25 мм" in elements


# Тестируем выводятся ли при поиске товары корректно + проверяем их количество.
def test_tmall_48(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    tmall_main_page.enter_word("Процессоры Intel")
    tmall_main_page.find_search_button().click()
    time.sleep(5)
    add = tmall_main_page.find_advertisement()
    if add != None:
        add.click()
    items = tmall_main_page.find_item_quantity()
    assert len(items) > 7


# Тестируем работает ли переход в службу поддержки.
# Важно: при тесте нельзя двигать компьютерной мышью т.к. это приведет к сбою мышки selenium-а
# (т.е. к отрицательному значению теста).
def test_tmall_49(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    support_button = tmall_main_page.find_support_button()
    action = webdriver.ActionChains(browser)
    action.move_to_element(support_button).perform()
    support_button_link = tmall_main_page.find_support_button_link()
    action.move_to_element(support_button_link).perform()
    time.sleep(1)
    checking = False
    try:
        support_button_link.click()
        checking = True
    except:
        pass
    assert checking


# Тестируем правильно ли отображается станица службы поддержки.
# Важно: при тесте нельзя двигать компьютерной мышью т.к. это приведет к сбою мышки selenium-а
# (т.е. к отрицательному значению теста).
def test_tmall_50(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    support_button = tmall_main_page.find_support_button()
    action = webdriver.ActionChains(browser)
    action.move_to_element(support_button).perform()
    support_button_link = tmall_main_page.find_support_button_link()
    action.move_to_element(support_button_link).perform()
    time.sleep(1)
    support_button_link.click()
    time.sleep(11)
    questions = tmall_main_page.find_support_page_questions()
    assert 'Когда продавец отправит заказ?' and ' Как отследить мою посылку?' and 'Когда я получу свой заказ?' in questions


# Тестируем работает ли кнопка возврата в странице службы поддержки.
# Важно: при тесте нельзя двигать компьютерной мышью т.к. это приведет к сбою мышки selenium-а
# (т.е. к отрицательному значению теста).
def test_tmall_51(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    support_button = tmall_main_page.find_support_button()
    action = webdriver.ActionChains(browser)
    action.move_to_element(support_button).perform()
    support_button_link = tmall_main_page.find_support_button_link()
    action.move_to_element(support_button_link).perform()
    time.sleep(1)
    support_button_link.click()
    time.sleep(11)
    return_button = tmall_main_page.find_support_page_return_button()
    browser.execute_script("arguments[0].scrollIntoView();", return_button)
    checking = False
    try:
        return_button.click()
        checking = True
    except:
        pass
    time.sleep(5)
    assert checking


# Тестируем отображается ли панель "Навигация по AliExpress".
# Важно: при тесте нельзя двигать компьютерной мышью т.к. это приведет к сбою мышки selenium-а
# (т.е. к отрицательному значению теста).
def test_tmall_52(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    mainpage_nav_panel = tmall_main_page.find_mainpage_nav_panel()
    browser.execute_script(
        "arguments[0].scrollIntoView();", mainpage_nav_panel)
    time.sleep(5)
    assert mainpage_nav_panel != None


# Тестируем отображается ли панель "AliExpress на других языках".
# Важно: при тесте нельзя двигать компьютерной мышью т.к. это приведет к сбою мышки selenium-а
# (т.е. к отрицательному значению теста).
def test_tmall_53(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    mainpage_nav_languages = tmall_main_page.find_mainpage_nav_languages()
    browser.execute_script(
        "arguments[0].scrollIntoView();", mainpage_nav_languages)
    time.sleep(5)
    assert mainpage_nav_languages != None


# Тестируем отображается ли панель "Категории товаров".
# Важно: при тесте нельзя двигать компьютерной мышью т.к. это приведет к сбою мышки selenium-а
# (т.е. к отрицательному значению теста).
def test_tmall_54(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    mainpage_nav_categories = tmall_main_page.find_mainpage_nav_categories()
    browser.execute_script(
        "arguments[0].scrollIntoView();", mainpage_nav_categories)
    time.sleep(5)
    assert mainpage_nav_categories != None


# Тестируем отображается ли панель "Группа компании Alibaba".
# Важно: при тесте нельзя двигать компьютерной мышью т.к. это приведет к сбою мышки selenium-а
# (т.е. к отрицательному значению теста).
def test_tmall_55(browser):
    tmall_main_page = SearchHelper(browser)
    tmall_main_page.go_to_site()
    mainpage_nav_group = tmall_main_page.find_mainpage_nav_group()
    browser.execute_script(
        "arguments[0].scrollIntoView();", mainpage_nav_group)
    time.sleep(5)
    assert mainpage_nav_group != None
