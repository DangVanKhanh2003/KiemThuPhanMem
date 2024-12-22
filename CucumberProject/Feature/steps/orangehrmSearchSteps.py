from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options
from behave import given, when, then
import time

from selenium.webdriver.support.wait import WebDriverWait


@given('I launch the browser')
def step_impl(context):
    context.driver = webdriver.Edge()  # Use Chrome as per the feature description
    context.driver.maximize_window()

@when('I open the OrangeHRM homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

@when('I click on the Search input')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    search_icon = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')))
    search_icon.click()

@then('I should see the Search input field')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    search_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')))
    assert search_input.is_displayed(), "Search input field is not displayed"

@then('I enter "{input_value}" in the Search input')
def step_impl(context, input_value):
    wait = WebDriverWait(context.driver, 10)
    search_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')))
    search_input.clear()
    search_input.send_keys(input_value)
    search_input.send_keys(Keys.RETURN)
    time.sleep(2)


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import then


@then('I should see "{xpath_result}" in the results')
def step_impl(context, xpath_result):
    try:
        # Wait for the element to be present and visible
        wait = WebDriverWait(context.driver, 10)
        result = wait.until(EC.presence_of_element_located((By.XPATH, xpath_result)))

        # Check if the result is displayed
        assert result.is_displayed(), f"Result not found for XPath: {xpath_result}"
    except Exception as e:
        # Raise an error if the element is not found
        raise AssertionError(f"Expected result not found for XPath '{xpath_result}': {str(e)}")


@then('I close the browser')
def step_impl(context):
    context.driver.quit()
