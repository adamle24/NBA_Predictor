from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_nba_injuries():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")

    service = Service("chromedriver.exe") 
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.cbssports.com/nba/injuries/")
    time.sleep(5)  # Wait for JavaScript load

    print("Page loaded successfully!", flush=True)

    teams = driver.find_elements(By.CSS_SELECTOR, "h4.TableBase-title a")  # Extract team names
    rows = driver.find_elements(By.CSS_SELECTOR, "tr")

    injury_data = []
    
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) >= 5:
            player_name = cells[0].text.strip()
            position = cells[1].text.strip()
            injury = cells[3].text.strip()
            injury_status = cells[4].text.strip()

            injury_data.append({
                "player_name": player_name,
                "position": position,
                "injury": injury,
                "injury_status": injury_status
            })

    driver.quit()
    return injury_data
