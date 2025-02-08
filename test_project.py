import pytest
from project import load_config, extract_phone_number, process_data
from scrapper import WebScraper

@pytest.fixture
def config():
    return load_config()

@pytest.fixture
def scraper(config):
    return WebScraper(config)

def test_load_config(config):
    """ Test that the config file loads correctly. """
    assert "webdriver_path" in config
    assert "scraping" in config

def test_extract_phone_number(scraper):
    """ Test that extract_phone_number returns a string. """
    url = "https://www.google.es/maps/place/Chasoal+Estilistas/@38.9913264,-3.9279378,17z/data=!3m1!4b1!4m6!3m5!1s0xd6bc369bfef27af:0xf8c1ab7cb3b67928!8m2!3d38.9913264!4d-3.9279378!16s%2Fg%2F12qfbnfpp?authuser=0&hl=es&entry=ttu&g_ep=EgoyMDI1MDIwNS4wIKXMDSoASAFQAw%3D%3D"  # Replace with a real test case
    result = extract_phone_number(url, scraper)
    assert isinstance(result, str)

def test_process_data():
    """ Test that process_data runs without errors. """
    try:
        process_data()
        assert True
    except Exception:
        assert False, "process_data() failed."
