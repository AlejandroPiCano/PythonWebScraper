from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebScraper:
    def __init__(self, config):
        """ Initialize WebDriver and settings from config.json """
        service = Service(config["webdriver_path"])
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, config["scraping"]["wait_time"])
        
    def scrape_data(self, url):
        """ Extract the phone number from a given URL """
        try:
            self.driver.get(url)
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "DUwDvf")))

            try:
                phone_element = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Teléfono')]")
                phone = phone_element.get_attribute("aria-label").replace("Teléfono: ", "").strip()
            except Exception:
                phone = "Teléfono no encontrado"

            return phone
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None

    def close(self):
        """ Close the WebDriver session """
        self.driver.quit()
