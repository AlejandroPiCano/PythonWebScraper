import json
from scrapper import WebScraper
from excel_handler import ExcelHandler

def load_config(config_path="config.json"):
    """ Load configuration from a JSON file. """
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)

def extract_phone_number(url, scraper):
    """ Extract the phone number from a given URL using the WebScraper. """
    return scraper.scrape_data(url)

def process_data():
    """ Reads input Excel, scrapes phone numbers, and writes results to output Excel. """
    config = load_config()
    scraper = WebScraper(config)
    excel_handler = ExcelHandler(config)

    input_data = excel_handler.read_input_data()
    output_data = []

    for row in input_data:
        url, nombre, direccion = row
        telefono = extract_phone_number(url, scraper)
        output_data.append([nombre, telefono, direccion, url])
        print(f"Processed: {nombre}, Teléfono: {telefono}, Dirección: {direccion}, Enlace: {url}")

    scraper.close()
    excel_handler.write_output_data(output_data)
    print(f"Data saved in {config['output_file']}")

def main():
    """ Main function to execute the web scraping process. """
    process_data()

if __name__ == "__main__":
    main()
