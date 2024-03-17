from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys
import csv
from IPython.display import display, Image
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup




if len(sys.argv) != 3:
    print("Usage: python3 yourcode.py <date> <currency_code>")
    sys.exit(1)

date = sys.argv[1]
string_date = datetime.strptime(date, "%Y%m%d").date()
formatted_date = string_date.strftime("%Y-%m-%d")

currency_code = sys.argv[2]


currency = {}
with open('./currency.csv', mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        currency[row['Currency Code']] = row['Currency Name']
#print(currency)
currency_name = currency.get(currency_code, None)
if not currency_name:
    print(f"Currency code {currency_code} not found in mapping.")
    sys.exit(1)


chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.boc.cn/sourcedb/whpj/")

    date_input = driver.find_element(By.ID, 'erectDate')
    date_input.clear()
    date_input.send_keys(formatted_date)

    end_input = driver.find_element(By.ID, 'nothing')
    end_input.clear()
    end_input.send_keys(formatted_date)

    currency_select = Select(driver.find_element(By.NAME, "pjname"))
    currency_select.select_by_visible_text(currency_name)


    
    search_button = driver.find_element(By.CLASS_NAME, "search_btn")


    time.sleep(1)
    driver.execute_script("executeSearch();")

    time.sleep(5)
    page_html = driver.page_source
    soup = BeautifulSoup(page_html, 'html.parser')
    table = soup.find('div', attrs={'class': 'BOC_main publish'}).find('table')
    tr = table.find_all('tr')
    sell_price = tr[3].get_text().split()[3]
    

    with open("result.txt", "w") as file:
        file.write(sell_price)


finally:
    driver.quit()
