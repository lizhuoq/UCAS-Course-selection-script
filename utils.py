import time
import matplotlib.pyplot as plt
from PIL import Image
import os
import datetime
import ddddocr

def driverOption():
    from selenium import webdriver
    option = webdriver.ChromeOptions()
    #关闭“chrome正受到自动测试软件的控制”
    #V75以及以下版本
    #option.add_argument('disable-infobars')
    #V76以及以上版本
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    
    option.add_experimental_option("prefs",\
                                   {"credentials_enable_service":False,\
                                    "profile.password_manager_enabled":False})

    #不自动关闭浏览器
    option.add_experimental_option("detach", True)

    return option


def click(driver, by, value, loop=True):
    currentUrl = driver.current_url
    try:
        while driver.current_url == currentUrl:
            button = driver.find_element(by, value)
            button.click()
            if not loop:
                break
    except:
        time.sleep(1)
        click(driver, by, value, loop=loop)


def dataCollection(driver, by, value, path, num=1000):
    i = 0
    with open(os.path.join(path, 'labels.txt'), 'w') as file:
        while i < num:
            vcode = driver.find_element(by, value)
            result = input()
            filename = os.path.join(path, str(i)+'.png')
            vcode.screenshot(filename)
            file.write(str(i)+'.png'+'\t'+result+'\n')
            driver.refresh()
            time.sleep(1)
            i += 1


def loop(driver, by, value):
    xpath_expression = "//tr[td/a/span[text()='"+value+"']]/td/input[@type='checkbox']"
    checkbox = driver.find_element(by, xpath_expression)
    if checkbox.is_enabled():
        print(checkbox.is_enabled())
        print(f'[{datetime.datetime.now()}]已经选择......')
        # checkbox.click()
        time.sleep(2)
        driver.execute_script("$(arguments[0]).click()",checkbox)
    else:
        print(f'[{datetime.datetime.now()}]课程已满，刷新......')
        driver.refresh()
        time.sleep(3)
        loop(driver, by, value)


def ocrCal(image, import_onnx_path, charsets_path):
    ocr = ddddocr.DdddOcr(det=False, ocr=False, import_onnx_path=import_onnx_path, charsets_path=charsets_path)

    with open(image, 'rb') as f:
        image_bytes = f.read()

    res = ocr.classification(image_bytes)
    res = res[:3]
    print(res)

    return int(eval(res))




    

