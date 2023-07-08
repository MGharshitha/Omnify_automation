from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Set your LambdaTest username and access key
username = "harshithamgb"
access_key = "K11I34l6jl3GsGVteQu3o18RPcVuo6di5bNUL6LsrkmE3KQnWK"

# Set desired capabilities for the test environment
chrome_options = Options()
chrome_options.add_argument("browserName=chrome")
chrome_options.add_argument("version=latest")
chrome_options.add_argument("platform=WIN10")
chrome_options.add_argument("name=LambdaTest Sample Test")

# Set up the remote WebDriver
driver = webdriver.chrome(
    command_executor="https://"+username+":"+access_key+"@hub.lambdatest.com/wd/hub",
    options=chrome_options
)

# Navigate to a webpage
driver.get("https://www.example.com")

# Perform some actions
element = driver.find_element_by_name("q")
element.send_keys("LambdaTest")
element.send_keys(Keys.RETURN)

# Wait for the results page to load
driver.implicitly_wait(10)

# Print the page title
print("Page title:", driver.title)

# Take a screenshot
driver.save_screenshot("screenshot.png")

# Close the browser
driver.quit()
