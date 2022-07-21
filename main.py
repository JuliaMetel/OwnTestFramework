from selenium import webdriver, common
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Browser settings
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--auto-open-devtools-for-tabs')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(3)

# Page opening
driver.get("https://webglsamples.org/collectibles/index.html")
try:
    elem = driver.find_element('id', 'dollbaseFemale')
    elem.click()
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(('id', 'canvas')))
except common.exceptions.NoSuchElementException:
    print('Element not found')
except common.exceptions.TimeoutException:
    print('3D object not found')
else:
    print('Test passed')
finally:
   driver.quit()