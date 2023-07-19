import asyncio
import json
from loguru import logger
from time import sleep

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support import expected_conditions as EC



def get_configs() -> dict:
    with open('configs.txt', 'r') as file:
        configs = json.load(file)
    return configs


def get_driver(headless=True):
    opts = ChromeOptions()
    opts.page_load_strategy = 'eager'
    opts.add_argument('--disable-popup-blocking')
    opts.add_argument('--disable-lazy-loading')
    opts.add_argument('--disable-notifications')
    opts.add_argument('--disable-save-password-bubble')
    if headless:
        opts.add_argument('--headless')
    driver = uc.Chrome(options=opts)

    return driver


def select_server(driver: uc.Chrome, auth_name: str, auth_pass: str, server_num=0):
    """
    Enter the menu server by its number. Its require login and password to be loggined.
    If server number was not found, there will be first (0) server.
    """
    try:
        driver.get('https://aternos.org/servers')
    except:
        pass
    input_name = driver.find_element(By.ID, 'user')
    input_pass = driver.find_element(By.ID, 'password')

    input_name.send_keys(auth_name)
    input_pass.send_keys(auth_pass)

    submit_button = driver.find_element(By.ID, 'login')
    submit_button.click()

    # We need a sleep to avoid errors by unloaded browser page
    sleep(2)

    server_button = driver.find_elements(By.CLASS_NAME, "server-body")
    server_button[server_num].click()

    # We need a sleep again
    sleep(5)


async def launch_server(driver: uc.Chrome):
    try:
        start_server_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='start']/i")))
    except:
        logger.warning('Server start button was not found! Maybe, there is an error.')
    else:
        start_server_button.click()

    # We wait ~2 seconds to find notification button and click it, if it is there
    await asyncio.sleep(2)
    try:
        danger_button = driver.find_element(By.XPATH, '//*[@id="theme-switch"]/dialog/main/div[2]/button[2]')
        danger_button.click()
    except:
        pass


async def stop_server(driver: uc.Chrome):
    try:
        stop_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stop"]')))
    except:
        logger.warning('Server close button was not found! Maybe, there is an error')
    else:
        stop_button.click()


def go_over_block(driver: uc.Chrome):
    try:
        warning_button = driver.find_element(By.XPATH, '/html/body/span[2]/div/div[1]/div[3]/div[2]/div[1]')
        warning_button.click()
    except:
        logger.warning('ADBlock window was not found. Maybe, there is an error.')
    else:
        sleep(4)


async def get_status(driver: uc.Chrome) -> str:
    try:
        status_label = driver.find_element(By.CLASS_NAME, 'statuslabel-label').text
    except:
        logger.error('Server status label was not found! There is an error!')
        return "Оффлайн"
    return str(status_label)


async def timer(driver: uc.Chrome, condition="Онлайн"):
    status = await get_status(driver)
    while status != condition:
        await asyncio.sleep(1)
        try:
            status = await get_status(driver)
        except:
            await go_over_block(driver)
    return


async def get_players(driver: uc.Chrome) -> str:
    try:
        players = driver.find_element(By.XPATH, '//*[@id="read-our-tos"]/main/section/div[3]/div[4]/div[3]/div[1]/div[1]/div[2]/div[2]').text
        players = players.split('/')
        return str(players[0])
    except:
        logger.warning('There is no players. Maybe, it is an error.')
        return '0'


async def get_tps(driver: uc.Chrome) -> str:
    try:
        tps = driver.find_element(By.XPATH, '//*[@id="read-our-tos"]/main/section/div[3]/div[4]/div[3]/div[1]/div[3]/div[2]/div[2]').text
        return str(tps)
    except:
        logger.warning('There is no tps. Maybe, it is an error.')
        return '0'
    

async def get_version(driver: uc.Chrome) -> str:
    try:
        version = driver.find_element(By.XPATH, '//*[@id="version"]').text
        return str(version)
    except:
        logger.error('There is no server version. It is an error.')
        return 'Неизвестно'
    

async def get_ip(driver: uc.Chrome) -> str:
    try:
        ip = driver.find_element(By.XPATH, '//*[@id="ip"]').text
        return str(ip)
    except:
        logger.warning('There is no server ip. It is an error.')
        return 'Неизвестно'
    

async def get_left_time(driver: uc.Chrome):
    try:
        left_time = driver.find_element(By.XPATH, '//*[@id="read-our-tos"]/main/section/div[3]/div[2]/div[1]/div/span[1]').text
        return left_time
    except:
        logger.warning('There is no left time to close server. Maybe it is an error.')
        return '0'
    


if __name__ == "__main__":
    driver = get_driver(headless=False)

    select_server(driver, 0)

    print(get_status(driver))
    input()
