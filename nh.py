from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import localtime

def check_registration():
    running = True
    options = Options()
    options.headless = True

    while running:
        driver = webdriver.Chrome(executable_path="/Users/alexanderrodionmichaud/Documents/chromedriver", chrome_options=options)
        driver.get("https://vini.nh.gov/providers/s/")
        e = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'years old or older.')]")))
        now = localtime()

        if e.text != "I am 30 years old or older.":
            print(e.text)
            notify()
            running = False
            print(f'SITE HAS UPDATED: {now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}')
        else:
            print(f'No changes as of {now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec} Trying again...')
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
