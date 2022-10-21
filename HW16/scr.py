import subprocess
import time
from selenium import webdriver
subprocess.run("docker rm -f selenium_chrome", shell=True, check=True)
port = 4444
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-dev-shm-usage")
subprocess.run("docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug",
                       shell=True, check=True)
time.sleep(5)
driver = webdriver.Remote(
        command_executor=f'http://localhost:{port}/wd/hub',
        options=options
    )
driver.get("http://google.com")