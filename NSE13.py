from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time 

# Path to chromedriver
path = "chromedriver.exe"

data = {'Stock Name':[],'Current Price':[],'%changed':[],'Volume':[]}

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# Set up Chrome service
service = Service(executable_path=path)
driver = Chrome(service=service, options=chrome_options)

# Target URL
url = "https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%2050"

# Example of adding headers
driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
})
driver.get(url)

# Wait for the table rows using tag name (tr)
wait = WebDriverWait(driver, 20)  # Increased wait time to 20 seconds
table_rows = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))

# Extract and print the %CHNG values from the 8th <td> in each row
for row in table_rows:
    try:
        tds = row.find_elements(By.TAG_NAME, 'td')
        if len(tds) >= 8:
            data['Stock Name'].append(tds[0].text)
            data['%changed'].append(tds[7].text)
            data['Current Price'].append(tds[9].text)
            data['Volume'].append(tds[8].text)
    except Exception as e:
        continue  
    
time.sleep(20)
driver.quit()
df = pd.DataFrame(data)
df.to_csv('Assignment_selenium.csv',index=False)
df
