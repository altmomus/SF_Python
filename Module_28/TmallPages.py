from BaseApp import BasePage
from selenium.webdriver.common.by import By


# Класс в котором содержатся пути (локаторы) к конкретным элементам сайта.
# Если структура сайта изменится (именна классов, xpath и т.д.), 
# во многих случаях достаточно будет лишь изменить путь к элементу. 
class TmallSeacrhLocators:

    LOCATOR_TMALL_SEARCH_FIELD = (By.ID, "search-key")
    LOCATOR_TMALL_SEARCH_BUTTON = (By.CLASS_NAME, "search-button")
    LOCATOR_TMALL_NAVIGATION_BAR = (By.CLASS_NAME, "aerCategoryText")
    LOCATOR_TMALL_FIND_ITEMS = (
        By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/div[1]/li[1]/div/div[1]/div/a')
    LOCATOR_TMALL_SHIPPING_BUTTON = (By.ID, "switcher-info")
    LOCATOR_TMALL_COUNTER_VALUE = (
        By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/span/span/span')
    LOCATOR_TMALL_FIRST_SLIDER_RIGHT_BUTTON = (
        By.XPATH, '//*[@id="2124579560"]/div/div/div/div/div[1]')
    LOCATOR_TMALL_FIRST_SLIDER_LEFT_BUTTON = (
        By.XPATH, '//*[@id="2124579560"]/div/div/div/div/div[2]')
    LOCATOR_TMALL_SECOND_SLIDERT_BUTTON = (
        By.XPATH, '//*[@id="aePlusBanners_6584900070"]/div/div[1]/div[1]')
    LOCATOR_TMALL_SORT_BAR = (
        By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]')
    LOCATOR_TMALL_ADV = (By.XPATH, '/html/body/div[7]/div[2]/div/a')
    LOCATOR_TMALL_BY_ORDERS_BUTTON = (
        By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/span/span[2]')
    LOCATOR_TMALL_NEW_ITEMS_BUTTON = (
        By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/span/span[3]')
    LOCATOR_TMALL_PRICE_BUTTON = (
        By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/span/span[4]')
    LOCATOR_TMALL_ITEM_LINK = (
        By.XPATH, '//*[@id="module-9905746940"]/div[1]/div/div/div[1]/a/img')
    LOCATOR_TMALL_ITEM_TITLE = (By.CLASS_NAME, 'item-title')
    LOCATOR_TMALL_ITEM_PRICE = (By.CLASS_NAME, 'price-current')
    LOCATOR_TMALL_ITEM_SALVE_VALUE = (
        By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/div[1]/li[1]/div/div[2]/div/div[6]/div/span/a')
    LOCATOR_TMALL_ITEM_IMAGE = (
        By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/div[1]/li[1]/div/div[1]/div/a/img')
    LOCATOR_TMALL_ITEM_RATING = (
        By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/div[1]/li[1]/div/div[2]/div/div[6]/a/span')
    LOCATOR_TMALL_ITEM_COMPANY = (By.CLASS_NAME, 'store-name')
    LOCATOR_TMALL_NAV_CATEGORIES = (By.CLASS_NAME, 'aerCategoryText')
    LOCATOR_TMALL_ELECTRONIC_CATEGORY_SLIDER_PHOTO = (
        By.XPATH, '//*[@id="7120684850"]/div/div/div/div/div/div/div/div')
    LOCATOR_TMALL_APPLIANCES_CATEGORY_SLIDER_PHOTO = (
        By.XPATH, '//*[@id="aePlusBanners_8660912930"]/div/div[2]/div[1]/div/div/div[1]/a/img')
    LOCATOR_TMALL_HOUSE_GARDEN_CATEGORY_SLIDER_PHOTO = (
        By.XPATH, '//*[@id="aePlusBanners_4135398250"]/div/div[2]/div[1]/div/div/div[1]/a/img')
    LOCATOR_TMALL_CHILDREN_MOTHERS_CATEGORY_SLIDER_PHOTO = (
        By.XPATH, '//*[@id="aePlusBanners_5606428650"]/div/a/img')
    LOCATOR_TMALL_FASHION_CATEGORY_SLIDER_PHOTO = (
        By.XPATH, '//*[@id="aePlusBanners_1586846490"]/div/div[2]/div[1]/div/div/div[1]/a/img')
    LOCATOR_TMALL_SUPERMARKET_CATEGORY_SLIDER_PHOTO = (
        By.XPATH, '//*[@id="aePlusBanners_8580526290"]/div/div[2]/div[1]/div/div/div[1]/a/img')
    LOCATOR_TMALL_CAR_GOODS_CATEGORY_SLIDER_PHOTO = (
        By.XPATH, '//*[@id="aePlusBanners_9797265590"]/div/a/img')
    LOCATOR_TMALL_ITEM_BRAND = (By.CLASS_NAME, 'inner-item')
    LOCATOR_TMALL_ITEM_QUANTITY = (By.CLASS_NAME, 'item-img')
    LOCATOR_TMALL_SUPPORT_BUTTON = (
        By.XPATH, '//*[@id="nav-global"]/div[3]/span')
    LOCATOR_TMALL_SUPPORT_BUTTON_LINK = (
        By.XPATH, '//*[@id="nav-global"]/div[3]/ul/li[1]/a')
    LOCATOR_TMALL_SUPPORT_PAGE_QUESTIONS = (
        By.CLASS_NAME, 'question-item__dAiEMaRK')
    LOCATOR_TMALL_SUPPORT_PAGE_RETURN = (
        By.XPATH, '//*[@id="helphub"]/div[6]/div/div[2]/div[1]/div[2]')
    LOCATOR_TMALL_MAINPAGE_NAV_PANEL = (
        By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/div[1]')
    LOCATOR_TMALL_MAINPAGE_NAV_PANEL_LANGUAGES = (
        By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/div[2]')
    LOCATOR_TMALL_MAINPAGE_NAV_PANEL_CATEGORIES = (
        By.XPATH, '/html/body/div[2]/div[1]/div/div[2]')
    LOCATOR_TMALL_MAINPAGE_NAV_PANEL_GROUP = (
        By.XPATH, '/html/body/div[2]/div[1]/div/div[3]')


# Класс в котором содержатся вспомогательные методы для работы с поиском.
class SearchHelper(BasePage):

    # Функция ввода текста в поле input (для дальнейшего поиска элемента и т.д.).
    def enter_word(self, word):
        search_field = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    # Получаем список навигационного бара для дальнейшей обработки
    def check_navigation_bar(self):
        all_list = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    # Получаем кнопку (ссылку) одной категории для дальнейшей обработки
    def find_navigation_button(self):
        buttons_list = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_NAVIGATION_BAR, time=2)
        return buttons_list[0]

    # Находим кнопку поиска
    def find_search_button(self):
        search_button = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_SEARCH_BUTTON, time=2)
        return search_button

    # Находим кнопку информации о доставке
    def find_shipping_button(self):
        shipping_button = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_SHIPPING_BUTTON, time=2)
        return shipping_button

    # Находим кнопки навигации первого слайдера
    def find_first_slider_buttons(self):
        first_slider_buttons = []
        first_slider_buttons.append(self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_FIRST_SLIDER_RIGHT_BUTTON, time=2))
        first_slider_buttons.append(self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_FIRST_SLIDER_LEFT_BUTTON, time=2))
        return first_slider_buttons

    # Находим левую кнопку навигации второго слайдера
    def find_second_slider_button(self):
        second_slider_button = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_SECOND_SLIDERT_BUTTON, time=2)
        return second_slider_button

    # Находим элементы поиска (т.е. те элементы которые были найдены при поиске)
    def find_items_of_search(self):
        items_of_search = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_FIND_ITEMS, time=2)
        return items_of_search

    # Находим левую кнопку навигации второго слайдера
    def find_counter_value(self):
        counter_value = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_COUNTER_VALUE, time=2)
        return counter_value

    # Находим панель фильтрации
    def find_sort_bar(self):
        sort_bar = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_SORT_BAR, time=2)
        return sort_bar

    # Находим рекламу скидки 2 баксов
    def find_advertisement(self):
        adv = self.find_element(TmallSeacrhLocators.LOCATOR_TMALL_ADV, time=2)
        return adv

    # Находим кнопу "По заказам"
    def find_by_orders_button(self):
        adv = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_BY_ORDERS_BUTTON, time=2)
        return adv

    # Находим кнопу "Новинки"
    def find_new_items_button(self):
        adv = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_NEW_ITEMS_BUTTON, time=2)
        return adv

    # Находим кнопу "Цена"
    def find_price_button(self):
        adv = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_PRICE_BUTTON, time=2)
        return adv

    # Находим первый попавшийся товар и кликаем его
    def find_item_link(self):
        items = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_FIND_ITEMS, time=2)
        return items[0]

    # Находим название товара
    def find_item_title(self):
        item_title = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_ITEM_TITLE, time=2)
        return item_title

    # Находим цену товара
    def find_item_price(self):
        item_title = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_ITEM_PRICE, time=2)
        return item_title

    # Находим сколько товаров было продано
    def find_item_salve_value(self):
        item_salve_value = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_ITEM_SALVE_VALUE, time=2)
        return item_salve_value

    # Находим фото товара
    def find_item_image(self):
        item_image = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_ITEM_IMAGE, time=2)
        return item_image

    # Находим рейтинг товара
    def find_item_rating(self):
        item_rating = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_ITEM_RATING, time=2)
        return item_rating

    # Находим комапанию товара
    def find_item_company(self):
        item_company = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_ITEM_COMPANY, time=2)
        return item_company

    # Находим категории товаров в главной странице
    def find_nav_categories(self):
        nav_categories = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_NAV_CATEGORIES, time=2)
        return nav_categories

    # Находим картинку слайдера категории электроника
    def find_electronic_category_slider_photo(self):
        electronic_category_slider_photo = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_ELECTRONIC_CATEGORY_SLIDER_PHOTO, time=2)
        return electronic_category_slider_photo

    # Находим картинку слайдера категории бытовая техника
    def find_appliances_category_slider_photo(self):
        appliances_category_slider_photo = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_APPLIANCES_CATEGORY_SLIDER_PHOTO, time=2)
        return appliances_category_slider_photo

    # Находим картинку слайдера категории дом и сад
    def find_house_garden_category_slider_photo(self):
        house_garden_category_slider_photo = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_HOUSE_GARDEN_CATEGORY_SLIDER_PHOTO, time=2)
        return house_garden_category_slider_photo

    # Находим картинку слайдера категории детям и мам
    def find_children_mothers_category_slider_photo(self):
        children_mothers_category_slider_photo = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_CHILDREN_MOTHERS_CATEGORY_SLIDER_PHOTO, time=2)
        return children_mothers_category_slider_photo

    # Находим картинку слайдера категории мода
    def find_fashion_category_slider_photo(self):
        fashion_category_slider_photo = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_FASHION_CATEGORY_SLIDER_PHOTO, time=2)
        return fashion_category_slider_photo

    # Находим картинку слайдера категории супермаркет
    def find_supermarket_category_slider_photo(self):
        supermarket_category_slider_photo = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_SUPERMARKET_CATEGORY_SLIDER_PHOTO, time=2)
        return supermarket_category_slider_photo

    # Находим картинку слайдера категории автотовары
    def find_car_goods_category_slider_photo(self):
        car_goods_category_slider_photo = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_CAR_GOODS_CATEGORY_SLIDER_PHOTO, time=2)
        return car_goods_category_slider_photo

    # Находим поле выбора бренда товаров
    def find_item_brand_choice(self):
        item_brand_choice = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_ITEM_BRAND, time=2)
        return item_brand_choice

    # Находим количество товаров
    def find_item_quantity(self):
        item_quantity = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_ITEM_QUANTITY, time=2)
        return item_quantity

    # Находим панель помощь в главном меню
    def find_support_button(self):
        support_button = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_SUPPORT_BUTTON, time=2)
        return support_button

    # Находим кнопку службы поддержки в главном меню
    def find_support_button_link(self):
        support_button_link = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_SUPPORT_BUTTON_LINK, time=2)
        return support_button_link

    # Находим частые вопросы со страницы службы поддержки
    def find_support_page_questions(self):
        support_page_questions = self.find_elements(
            TmallSeacrhLocators.LOCATOR_TMALL_SUPPORT_PAGE_QUESTIONS, time=2)
        page_questions = [
            x.text for x in support_page_questions if len(x.text) > 0]
        return page_questions

    # Находим кнопку возврата со страницы службы поддержки
    def find_support_page_return_button(self):
        support_page_return_button = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_SUPPORT_PAGE_RETURN, time=2)
        return support_page_return_button

    # Находим панель "Навигация по AliExpress" в подвале сайта
    def find_mainpage_nav_panel(self):
        mainpage_nav_panel = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_MAINPAGE_NAV_PANEL, time=2)
        return mainpage_nav_panel

    # Находим панель "AliExpress на других языках" в подвале сайта
    def find_mainpage_nav_languages(self):
        mainpage_nav_languages = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_MAINPAGE_NAV_PANEL_LANGUAGES, time=2)
        return mainpage_nav_languages

    # Находим панель "Категории товаров" в подвале сайта
    def find_mainpage_nav_categories(self):
        mainpage_nav_categories = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_MAINPAGE_NAV_PANEL_CATEGORIES, time=2)
        return mainpage_nav_categories

    # Находим панель "Группа компании Alibaba" в подвале сайта
    def find_mainpage_nav_group(self):
        mainpage_nav_group = self.find_element(
            TmallSeacrhLocators.LOCATOR_TMALL_MAINPAGE_NAV_PANEL_GROUP, time=2)
        return mainpage_nav_group
