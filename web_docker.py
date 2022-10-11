import time

from selenium import webdriver
import subprocess

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

port = 4347

try:
    subprocess.run(f"docker run -d --name selenium_chrome -p"
                   f" {port}:4444 -v "
                   f"/dev/shm:/dev/shm selenium/standalone-chrome",
                   shell=True,check=True)
    time.sleep(5)
    print("docker started")
    driver = webdriver.Remote(
            command_executor=f'http://localhost:{port}/wd/hub',
                          options=options)

    driver.get("https://google.com")
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/img")
    print(element.get_attribute("src"))

    driver.close()
except subprocess.CalledProcessError:
    print("not started")
finally:
    subprocess.run("docker rm --force selenium_chrome", shell=True,check=True)
