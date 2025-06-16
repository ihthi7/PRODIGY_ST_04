from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Replace with your BrowserStack credentials
USERNAME = "ihthishaibrahim_IvxS7z"
ACCESS_KEY = "xLy11F4ejTHsupKCvDmr"

# Test configurations for multiple browsers
browsers = [
    {"os": "Windows", "os_version": "10", "browser": "Chrome", "browser_version": "latest"},
    {"os": "Windows", "os_version": "10", "browser": "Firefox", "browser_version": "latest"},
    {"os": "OS X", "os_version": "Monterey", "browser": "Safari", "browser_version": "latest"},
    {"os": "Windows", "os_version": "11", "browser": "Edge", "browser_version": "latest"}
]

def run_test(config):
    from selenium.webdriver.chrome.options import Options
    options = Options()

    # Set BrowserStack capabilities
    options.set_capability('browserName', config["browser"])
    options.set_capability('browserVersion', config["browser_version"])
    options.set_capability('bstack:options', {
        "os": config["os"],
        "osVersion": config["os_version"],
        "sessionName": "Cross-Browser Login Test - SauceDemo",
        "buildName": "Prodigy Internship Task 4"
    })

    url = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"
    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    try:
        # Test steps
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        assert "inventory" in driver.current_url
        print(f"✅ Login success on {config['browser']}")
    except Exception as e:
        print(f"❌ Test failed on {config['browser']}: {e}")
    finally:
        driver.quit()


# Run test across all configs
for browser_config in browsers:
    run_test(browser_config)
