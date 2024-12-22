from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Setup and Teardown
@given('launch Eage browser')
def launch_browser(context):
    context.driver = webdriver.Edge()  # Use Chrome as per the feature description
    context.driver.maximize_window()

@when('open orange hrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then('verify that the logo is present on the page')
def verify_logo(context):
    try:
        # Chờ cho phần tử xuất hiện trong tối đa 10 giây
        wait = WebDriverWait(context.driver, 10)
        logo = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/h5")))
        assert logo.is_displayed() is True
    except Exception as e:
        print(f"Lỗi: {e}")
        assert False, f"Không thể tìm thấy logo: {e}"

@then('verify that the username text is present on the page')
def verify_username_text(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        username_label = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/label')))
        assert username_label.is_displayed(), "Username text is not displayed!"
    except Exception as e:
        assert False, f"Username text verification failed: {e}"

@then('verify that the password text is present on the page')
def verify_password_text(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        password_label = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[1]/label')))
        assert password_label.is_displayed(), "Password text is not displayed!"
    except Exception as e:
        assert False, f"Password text verification failed: {e}"

@then('verify that the login button is present on the page')
def verify_login_button(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')))
        assert login_button.is_displayed(), "Login button is not displayed!"
    except Exception as e:
        assert False, f"Login button verification failed: {e}"

@then('verify that the username input is present on the page')
def verify_username_input(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        assert username_input.is_displayed(), "Username input is not displayed!"
    except Exception as e:
        assert False, f"Username input verification failed: {e}"

@then('verify that the password input is present on the page')
def verify_password_input(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        assert password_input.is_displayed(), "Password input is not displayed!"
    except Exception as e:
        assert False, f"Password input verification failed: {e}"

@then('close browser')
def close_browser(context):
    context.driver.quit()  # Use quit to ensure all browser instances and WebDriver sessions are closed
