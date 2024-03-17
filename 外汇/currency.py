from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.11meigui.com/tools/currency')

rows = driver.find_elements(By.XPATH, '//table//tr')
#print(rows)

with open('currency.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Currency Name', 'Currency Code'])  # CSV header

    rows = driver.find_elements(By.XPATH, '//table//tr')
    
    for row in rows[2:-1]:
        cells = row.find_elements(By.TAG_NAME, 'td')
        
        
        if len(cells) >= 5: 
            currency_name = cells[1].text.strip()  
            currency_code = cells[4].text.strip() 
            writer.writerow([currency_name,currency_code])

driver.quit()