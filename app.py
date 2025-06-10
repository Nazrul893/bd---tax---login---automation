from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ BD Tax Bot is Running on Render!'

@app.route('/login')
def login_to_tax():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://secure.incometax.gov.bd/Registration/Login")
        time.sleep(2)

        driver.find_element(By.ID, "LOGON_NAME").send_keys("range1dhaka13")
        driver.find_element(By.ID, "LOGON_PASS").send_keys("*1234*")
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(3)

        page = driver.page_source
        driver.quit()

        if "Dashboard" in page or "logout" in page.lower():
            return "✅ Login Successful!"
        else:
            return "❌ Login Failed!"

    except Exception as e:
        return f"⚠️ Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
