import time
from bs4 import BeautifulSoup
from selenium import webdriver
import ezsheets
import datetime

def scrape_data():
    driver = webdriver.Chrome()
    url = "https://sahko.tk/"
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    price = soup.find("span", {"id": "price_now"})

    try:
        if price:
            price = price.text.strip()
            print(price)
            return price
        else:
            print("price not found")

    finally:
        driver.quit()

def update_spreadsheet(price):
    # Load the spreadsheet
    s = ezsheets.Spreadsheet("https://docs.google.com/spreadsheets/d/1Ki1CImh8fCWARHBk-PH3dN4FI2yQ55V-KL6Z1lOMOBc/edit")
    # Access the first sheet
    sh = s.sheets[0]
    time_now = datetime.datetime.now().strftime("%d:%m:%y,:%H:%M:%S")
    all_rows = sh.getRows()

    for i, row in enumerate(all_rows, start=1):
        if row[0] == '':
            sh.updateRow(i, [time_now, price])
            break
        else:
            pass
            
def main():
    price = scrape_data()
    update_spreadsheet(price)

if __name__ == "__main__":
    main()