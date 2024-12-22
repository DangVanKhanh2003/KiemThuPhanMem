from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given('I launch the browser amdin')
def step_impl(context):
    context.driver = webdriver.Edge()  # or another driver like Firefox, Edge, etc.
    context.driver.maximize_window()

@then('I navigate to the Admin menu')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    admin_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Admin']")))
    admin_menu.click()
    time.sleep(2)


@then('I should see all the elements on the Admin/User Management page')
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 10)
        elements = [
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input',
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div',
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div',
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div',
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]',
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]',
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
        ]
        for element in elements:
            assert wait.until(EC.presence_of_element_located((By.XPATH, element))).is_displayed()
    except Exception as e:
        print(f"Element verification failed: {e}")
        assert False, "Some elements are missing!"


@then('I search for a user with username "{username}"')
def step_impl(context, username):
    search_field = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input')
    search_field.clear()
    search_field.send_keys(username)
    search_button = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
    search_button.click()
    time.sleep(2)


@then('I should see results matching "{username}"')
def step_impl(context, username):
    results = context.driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]')
    assert any(username in result.text for result in results), f"No matching results for {username}"


@then('I fill the search fields with test data')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Admin")
    context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(2)


@then('I reset the search fields')
def step_impl(context):
    reset_button = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]')
    reset_button.click()
    time.sleep(2)


@then('I should see all fields cleared')
def step_impl(context):
    username_field = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input')
    assert username_field.get_attribute("value") == "", "Fields are not cleared!"


@then('I click on the "+ Add" button')
def step_impl(context):
    add_button = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
    add_button.click()
    time.sleep(2)


@then('I should be redirected to the Add User page')
def step_impl(context):
    header = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]')
    assert header.is_displayed(), "Not redirected to Add User page!"


@then('I should see the number of elements in the toaster div')
def step_impl(context):
    try:
        # Chờ cho đến khi toaster div xuất hiện
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '///*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]'))
        )

        # Tìm tất cả các phần tử con bên trong toaster div
        toaster_elements = context.driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]//*')

        # Đếm số lượng phần tử con trong toaster div
        number_of_elements = len(toaster_elements)

        # In ra số lượng phần tử
        print(f"Number of elements in toaster div: {number_of_elements}")

        # Kiểm tra xem số lượng phần tử có đúng như mong đợi hay không (tùy theo yêu cầu của bạn)
        assert number_of_elements > 0, "no elements found in toaster div!"
    except Exception as e:
        # Nếu không tìm thấy phần tử, in ra thông báo lỗi
        assert False, f"Error occurred while counting elements in toaster div: {str(e)}"

@then(u'I should see "No Records Found"')
def step_impl(context):
    try:
        # Chờ cho đến khi toaster div xuất hiện
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="oxd-toaster_1"]'))
        )

        # Tìm tất cả các phần tử con bên trong toaster div
        toaster_elements = context.driver.find_elements(By.XPATH, '//*[@id="oxd-toaster_1"]//*')

        # Đếm số lượng phần tử con trong toaster div
        number_of_elements = len(toaster_elements)

        # Kiểm tra xem số lượng phần tử có đúng như mong đợi hay không (tùy theo yêu cầu của bạn)
        assert number_of_elements > 0, "exist elements found in toaster div!"

    except Exception as e:
        # Nếu không tìm thấy phần tử, in ra thông báo lỗi
        assert False, f"Error occurred while checking 'No Records Found' message: {str(e)}"


@then('I close the browser admin')
def step_impl(context):
    context.driver.quit()