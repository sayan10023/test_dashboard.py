from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dashboard():
    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("detach", True)  # Prevents browser from closing
    
    # Initialize driver
    driver = None
    
    try:
        # Initialize WebDriver with automatic driver management
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        
        driver.get("https://auth.segwise.ai/en/login")
        
        # Login process
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email.send_keys("qa@segwise.ai")
        
        password = driver.find_element(By.NAME, "password")
        password.send_keys("segwise_test")
        
        login_button = driver.find_element(
            By.XPATH, "//button[contains(., 'Login')]"
        )
        login_button.click()
        
        # Dashboard verification
        WebDriverWait(driver, 15).until(
            EC.url_contains("dashboard") |
            EC.presence_of_element_located((By.XPATH, "//*[contains(., 'Dashboard')]"))
        )
        print("✔ Login successful - Browser will remain open")
        
        # Keep browser open indefinitely
        input("Press Enter to close the browser...")  # Remove this line if you want it to stay open without prompt
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        if driver:
            print("Current URL:", driver.current_url)
            print("Page title:", driver.title)
            input("Press Enter to close the browser after error...")  # Optional

if __name__ == "__main__":
    test_dashboard()
    print("Test completed - Browser remains open")