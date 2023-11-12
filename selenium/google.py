from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request

driver = webdriver.Firefox()
driver.get("https://www.google.com/imghp?hl=ko&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("Sphaerophoria menthastri")
elem.send_keys(Keys.RETURN)

time.sleep(3)
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 6

for image in images:
    try:
        image.click()
        time.sleep(5)
        imgUrl = driver.find_element(By.CSS_SELECTOR, ".r48jcc.pT0Scc.iPVvYb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count = count + 1
    except Exception as e:
        print(f"이미지 다운로드 실패: {str(e)}")
        continue

# for image in images:
#     image.click()
#     time.sleep(3)
#     imgUrl = driver.find_element(By.CSS_SELECTOR, ".r48jcc.pT0Scc.iPVvYb").get_attribute("src")
#     urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
#     count = count + 1

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
