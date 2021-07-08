from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Основной класс в котором содержатся самые необходимые функции для работы с selenium
class BasePage:

    # Инициализация драйвера (браузера) selenium через конструктор.
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://tmall.ru/"

    # Функция которая выполняет поиск одного элемента и возвращает его.
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    # Функция которая выполняет поиск нескольких элементов и возвращает их.
    # Эта функция возвращает список из элементов.
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    # Функция перехода в конкретный url и запуска браузера selenium-а.
    def go_to_site(self):
        return self.driver.get(self.base_url)
