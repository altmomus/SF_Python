import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# Создаем фикстуру, которая будет исполнена лишь 1 раз за тестовую сессию.
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()
