from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
import time
from selenium.webdriver.support.ui import Select
import pyautogui

path = os.getcwd() + '/geckodriver'

text_to_speech = ['Внимание!!!  Отключился рабочий ввод', 'Внимание!!!  Отключился резервный ввод', 'Внимание!!!  Отключился агрегат номер один',
                  'Внимание!!! Отключился агрегат номер два', 'Внимание!!! Отключился агрегат номер три', 'Внимание!!! Отключился фидер Рабочий', 'Внимание!!! Отключился фидер Беговой',
                  'Внимание!!! Отключился фидер Октябрьский', 'Внимание!!! Отключился фидер Клинический', 'Внимание!!! Отключился фидер Запасной автомат',
                  'Внимание!!! Неисправность агрегата номер один', 'Внимание!!! Неисправность агрегата номер два', 'Внимание!!! Неисправность агрегата номер три',
                  'Внимание!!! Неисправность вводов', 'Внимание!!! Короткое замыкание в РЭ УУ Шестьсот вольт', 'Внимание!!! Неисправность цепей управления в РЭ УУ шестьсот вольт', 'Внимание!!! нет напряжения Собственных Нужд']


for text in text_to_speech:
    driver = webdriver.Firefox(executable_path=path)
    driver.get('https://apihost.ru/voice')
    select = Select(driver.find_element_by_id('speaker'))
    select.select_by_value('omazh')
    time.sleep(5)
    elem = driver.find_element_by_id('from')
    elem.clear()

    elem.send_keys(text)
    speech = driver.find_element_by_id('loader')
    speech.click()

    pyautogui.press('down')

    pyautogui.press('enter')

    time.sleep(5)


    driver.close()
