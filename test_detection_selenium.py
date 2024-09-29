from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (make sure you have the appropriate driver installed)
# For example, for Chrome:
driver = webdriver.Chrome()

try:
    # Navigate to the bot detection page
    # Replace with the actual URL where you've hosted the bot detection HTML
    driver.get("http://localhost:8000/bot_detection_page.html")

    # Wait for 1 second
    time.sleep(1)

    # Wait for the message element to be present (adjust timeout as needed)
    message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "message"))
    )

    # Print the detection result
    print("Detection Result:", message.text)

    # Find all detection method elements
    method_elements = driver.find_elements(By.CSS_SELECTOR, "#detectionMethods li")

    # Print each detection method and its result
    for element in method_elements:
        print(element.text)

    # Wait for 1 second
    time.sleep(60)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()