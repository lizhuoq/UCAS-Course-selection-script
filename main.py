from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from matplotlib import pyplot as plt
import ddddocr
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

from utils import driverOption, click, dataCollection, loop, ocrCal



driver_path = r'C:\Program Files\Google\Chrome\Application'

driver = webdriver.Chrome(driver_path, options=driverOption())

driver.get('https://sep.ucas.ac.cn/')



while True:
    username_input = driver.find_element(By.ID, 'userName1')
    password_input = driver.find_element(By.ID, 'pwd1')
    username_input.send_keys('lizhuoqun221@mails.ucas.ac.cn')
    password_input.send_keys('yangyang137')
    captcha_image = driver.find_element(By.ID, 'certCode1')
    captcha_image.screenshot('captcha.png')

    image = Image.open('captcha.png')
    image = image.crop((100, 0, 250, 45))
    image.save('captcha.png')

    ocr = ddddocr.DdddOcr(beta=True)
    with open('captcha.png', 'rb') as f:
        image = f.read()

    res = ocr.classification(image)
    print(res)

    captcha_image.send_keys(res)


    login_button = driver.find_element(By.ID, 'sb1')
    login_button.click()

    wait = WebDriverWait(driver, 3)

    try:
        wait.until(EC.url_to_be('https://sep.ucas.ac.cn/appStore'))
        break
    except:
        print("验证码输入错误，正在刷新页面...")
        driver.refresh()

# sleep(1)

click(driver, By.LINK_TEXT, '选课系统')

    # courseSelectionButton = driver.find_element(By.LINK_TEXT, '选课系统')
    # courseSelectionButton.click()
    # print(driver.current_url)

click(driver, By.LINK_TEXT, '选修课程', loop=False)
# courseSelectionButton = driver.find_element(By.LINK_TEXT, '选修课程')
# courseSelectionButton.click()

click(driver, By.LINK_TEXT, '选择课程')
# courseSelectionButton = driver.find_element(By.LINK_TEXT, '选择课程')
# courseSelectionButton.click()

sleep(2)

frame = driver.find_element(By.ID, 'id_951')
print(frame.is_selected())
frame.click()
print(frame.is_selected())

sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

click(driver, By.XPATH, '//button[contains(text(), "新增加本学期研究生课程")]')

sleep(1)


# xpath_expression = "//tr[td/a/span[text()='081203M07007H']]/td/input[@type='checkbox']"
# checkbox = driver.find_element(By.XPATH, xpath_expression)
loop(driver, By.XPATH, '081203M07007H')

# dataCollection(driver, By.ID, 'adminValidateImg', r'D:\UCAS-Course selection script\data')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

ocrImage = driver.find_element(By.ID, 'adminValidateImg')
ocrImage.screenshot('ocrCal.png')

image = Image.open('ocrCal.png')
res = ocrCal('ocrCal.png', import_onnx_path='models\ocr_1.0_299_3000_2023-06-07-12-34-41.onnx', \
             charsets_path='models\charsets.json')

vcode = driver.find_element(By.ID, 'vcode')
vcode.send_keys(res)

submit_button = driver.find_element(By.XPATH, "//button[@name='sb' and @value='y']")
submit_button.click()

sleep(2)

current_url = driver.current_url

confirm_button = driver.find_element(By.XPATH, "//button[text()='确定']")
confirm_button.click()

print(f'[{datetime.datetime.now()}]选课完成！')