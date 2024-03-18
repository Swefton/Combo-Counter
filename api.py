from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

PATH = 'C:\Program Files (x86)\msedgedriver.exe'


def scrape_website(username, password):
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    s = Service(executable_path=PATH)
    
    driver = webdriver.Edge(service=s, options=options)
    wait = WebDriverWait(driver, 10)
    
    driver.get('data:,')
    
    driver.get("https://msu-sp.transactcampus.com/eAccounts/AccountSummary.aspx")
    
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#input28')))
    driver.find_element(By.CSS_SELECTOR,"#input28").send_keys(username)
    driver.find_element(By.CSS_SELECTOR,"#input36").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'input[value="Sign in"]').click()
    
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#MainContent_DivPanelBoard_3')))
    driver.find_element(By.CSS_SELECTOR, '#MainContent_DivPanelBoard_3').click()
    
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#MainContent_mprWeekValue')))
    remaining_swipes = driver.find_element(By.CSS_SELECTOR,"#MainContent_mprWeekValue").text

    driver.quit()

    return remaining_swipes