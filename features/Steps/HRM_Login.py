from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'launch browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when(u'Open URL')
def open_url(context):
    context.driver.get('https://www.orangehrm.com/')

# behave -f allure_behave.formatter:AllureFormatter -o reports/ features
@then(u'compare if the URL has been opened')
def get_title(context):
    a = context.driver.find_element(By.XPATH, "/html/body/nav/div/a/img").is_displayed()
    assert a is True


@then(u'close')
def close_browser(context):
    context.driver.close()
