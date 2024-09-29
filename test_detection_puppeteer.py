import asyncio
from pyppeteer import launch

async def test_bot_detection():
    browser = await launch(headless=False)  # Set headless=True for headless mode
    page = await browser.newPage()

    # Navigate to your bot detection page
    await page.goto('http://localhost:8000/bot_detection_page.html')

    # Wait for 3 seconds to allow all detection methods to run
    await asyncio.sleep(3)

    # Extract the detection result
    detection_result = await page.evaluate('''
        () => {
            const messageElement = document.getElementById('message');
            return messageElement ? messageElement.textContent : 'No message found';
        }
    ''')

    print('Detection Result:', detection_result)

    # Extract all detection methods and their results
    detection_methods = await page.evaluate('''
        () => {
            const methodElements = document.querySelectorAll('#detectionMethods li');
            return Array.from(methodElements).map(el => el.textContent);
        }
    ''')

    print('Detection Methods:')
    for method in detection_methods:
        print(method)

    await browser.close()

# Run the async function
asyncio.get_event_loop().run_until_complete(test_bot_detection())