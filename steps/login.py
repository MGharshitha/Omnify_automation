
from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Lunch the chrome browser')
def step_impl(context):
    context.browser = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
    print("hi")
    time.sleep(10)


@given('I am at the Account/Login page')
def step_impl(context):
    context.browser.get('https://www.eventzalley.com')
    print("1")
    button = context.browser.find_element(By.XPATH, "//span[text()='Log In | Sign Up']")
    button.click()
    print("2")
    context.browser.maximize_window()
    pass


@when('I fill the account email textbox with value \'myname@mymail.com\'')
def step_impl(context):
    email = context.browser.find_element(By.ID, "email")
    email.send_keys("harshithamgb@gmail.com")
    print("3")


@when('I fill the password textbox with value \'mypassword\'')
def step_impl(context):
    password = context.browser.find_element(By.ID, "password")
    password.send_keys("User@123")
    print("4")


@when('I click the login button')
def step_impl(context):
    z = context.browser.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/section/form/div[1]/div["
                                               "6]/button/span[1]/p")
    z.click()
    time.sleep(20)
    print("5")


@then('I should be at the home page')
def step_impl(context):
    assert True
    # profile = context.browser.find_element(By.XPATH, "//*[@id='mainContent']/header/div/div[2]/div/svg")
    profile = context.browser.find_element(By.XPATH, "//div[@class = 'MuiBox-root jss44']")

    profile.click()
    print(6)
    time.sleep(10)
    pass


@Then('Then click on the logout button')
def step_impl(context):
    logout = context.browser.find_element(By.XPATH, "//li[@role= 'menuitem']")
    logout.click()
    time.sleep(10)

    context.browser.close()

