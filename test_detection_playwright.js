const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Load the local HTML file
  const filePath = path.join(__dirname, '2.html');
  await page.goto(`file:${filePath}`);

  // Wait for the message to appear
  await page.waitForSelector('#message');

  // Get the text content of the message
  const messageText = await page.$eval('#message', el => el.textContent);

  console.log('Message displayed:', messageText);

  // Get all detection methods
  const detectionMethods = await page.$$eval('#detectionMethods li', elements => 
    elements.map(el => ({
      name: el.textContent.split(':')[0].trim(),
      detected: el.classList.contains('detected')
    }))
  );

  console.log('Detection methods:');
  detectionMethods.forEach(method => {
    console.log(`${method.name}: ${method.detected ? 'Detected' : 'Not Detected'}`);
  });
  
  await browser.close();
})();