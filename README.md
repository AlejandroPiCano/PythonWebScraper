# Web Scraper Project


#### Video Demo: https://youtu.be/29yoEVL-bIw

#### Name: Alejandro Miguel Pi Cano 
#### Edx username: AlejandroPi
#### Github username: AlejandroPiCano
#### City, Country: Ciudad Real, Spain


## Description:
This project automates web scraping using **Selenium** and stores the results in an **Excel file**. The input, output, and scraping settings are **configurable via a JSON file**.

The **Python-based web scraper** extracts business phone numbers from **Google Maps** using **Selenium** automation. It reads an **input Excel file** containing a list of business URLs, names, and addresses, then navigates to each URL, scrapes the phone number, and saves the extracted data to a new **output Excel file**. The project demonstrates proficiency in **web automation, data extraction, and file handling**.

How it Works
1. Reads the **input Excel file** containing business details.
2. Uses **Selenium** to open the Google Maps URL for each business.
3. Extracts the phone number if available.
4. Saves the results in an **output Excel file**.
5. The entire process is **configurable via `config.json`**, making it flexible and easy to modify.

This project showcases skills in **Python automation, Selenium for web interaction, Excel file handling with `openpyxl`, JSON configuration management, and automated testing with `pytest`**. It applies **real-world web scraping techniques**, handling dynamic content, waiting for elements to load, and structuring the project following best software development practices.

Features:
- **Dynamic configuration** using `config.json` (no hardcoded paths)
- **Automated web scraping** with `Selenium`
- **Excel data handling** (`openpyxl` for reading/writing `.xlsx` files)
- **Automated testing** with `pytest`
- **Error handling & logging** for reliability

## Installation:
```sh
pip install -r requirements.txt
