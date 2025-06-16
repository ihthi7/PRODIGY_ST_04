# 🧪 Task-04: Cross-Browser Testing with BrowserStack

This project performs **automated cross-browser login testing** using [Selenium](https://www.selenium.dev/) and [BrowserStack](https://www.browserstack.com/) to ensure compatibility of a web application across different browsers.

## ✅ Objective

Ensure the login functionality of a sample website works consistently on:

- ✅ Google Chrome  
- ✅ Mozilla Firefox  
- ✅ Safari  
- ✅ Microsoft Edge

## 🌐 Tested Site

[https://www.saucedemo.com/](https://www.saucedemo.com/)

**Login Credentials:**  
Username: standard_user  
Password: secret_sauce  


## ⚙️ Tools & Technologies

- 🧪 Selenium WebDriver
- ☁️ BrowserStack Automate
- 🐍 Python
- 📄 Pytest (optional for scaling tests)

## 🧩 How It Works

The script uses `webdriver.Remote()` to connect to BrowserStack’s Selenium Grid and runs the login automation script across different browsers.

Each test:
1. Opens the browser session on BrowserStack.
2. Visits the SauceDemo login page.
3. Enters valid credentials.
4. Verifies successful login by checking the redirected URL.

## 📸 Sample Output

```bash
✅ Login success on Chrome
✅ Login success on Firefox
✅ Login success on Safari
✅ Login success on Edge
```

