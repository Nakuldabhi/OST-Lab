from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 1. Open Chrome
# 2. Navigate to youtube.com
driver.get("https://www.youtube.com")

# 3. Wait 2 seconds
time.sleep(2)

# 4. Maximize window
driver.maximize_window()

# 5. Locate YouTube search box
search_box = driver.find_element(By.NAME, "search_query")

# 6. Enter text
search_box.send_keys("open source software")
search_box.send_keys(Keys.RETURN)

# 8. Wait 5 seconds
time.sleep(5)
driver.save_screenshot("p7_youtube_gui.png")

# 9. Close browser
# driver.quit()
