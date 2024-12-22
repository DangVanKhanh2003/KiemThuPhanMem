from selenium.webdriver.chrome.options import Options  # For Chrome
# or use from selenium.webdriver.edge.options import Options if you're using Edge
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@given('I launch Eage browser')
def step_impl(context):
    options = Options()
    options.add_argument('--lang=en-US')  # Set language to English (or any other supported language)
    options.add_argument('--encoding=UTF-8')  # Ensure UTF-8 encoding

    context.driver = webdriver.Chrome(options=options)  # Use Chrome with the options
    # For Edge, use: context.driver = webdriver.Edge(options=options)
    context.driver.maximize_window()


@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    wait = WebDriverWait(context.driver, 10)

    # Locate the username and password input fields
    username_field = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')))
    password_field = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')))

    # Clear and enter the username and password
    username_field.clear()
    username_field.send_keys(username)
    password_field.clear()
    password_field.send_keys(password)


@when('Click on Login button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    login_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
    login_button.click()


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 10)
        # Correct XPath (removed extra quotes)
        dashboard_text_element = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6')))

        # Check if the element is displayed
        assert dashboard_text_element.is_displayed(), "Dashboard text is not displayed!"
    except Exception as e:
        print(f"Lỗi: {e}")
        assert False, f"Không thể đăng nhập: {e}"
    finally:
        context.driver.close()


@then('Login Invalid')
def step_impl(context):
    try:
        # Wait for the error message to appear
        wait = WebDriverWait(context.driver, 10)
        error_message = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'))).text
        assert "Invalid credentials" in error_message, f"Expected 'Invalid credentials' message, but got '{error_message}'"
    except Exception as e:
        assert False, f"Test Failed: {str(e)}"
    finally:
        context.driver.quit()
