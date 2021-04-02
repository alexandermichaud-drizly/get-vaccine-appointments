from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from time import sleep, localtime

def check_registration():
    running = True
    options = Options()
    options.add_argument("start-maximized")
    options.headless = True

    while running:
        driver = uc.Chrome(options=options)
        # Set useragent to googlebot
        # driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'})
        driver.get("https://vini.nh.gov/providers/s/")
        e = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'years old or older.')]")))
        now = localtime()

        if e.text != "I am 30 years old or older.":
            print(e.text)
            notify()
            running = False
            print(f'SITE HAS UPDATED: {now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}')
        else:
            print(f'No changes as of {now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min} Trying again...')
            sleep(30)
        driver.quit()

def notify():
    from os import getenv
    from twilio.rest import Client

    sid = getenv('TWILIO_SID')
    auth_token = getenv('TWILIO_AUTH_TOKEN')

    client = Client(sid, auth_token)

    body_text = "REGISTER NOW: https://vini.nh.gov/providers/s/" 

    message = client.messages.create(
        to="+16033980413",
        from_="+13396744164",
        body=body_text)

    print(body_text)

if __name__ == "__main__":
    check_registration()
