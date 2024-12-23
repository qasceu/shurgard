import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.unit_details_page import UnitDetailsPage
from utils.date_picker import DatePicker

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.mark.parametrize("location, unit_type", [
    ("Brussels", "1,5 m"),
])
def test_reserve_unit(browser_context, location, unit_type):
    page = browser_context
    
    # Page objects
    home_page = HomePage(page)
    unit_details_page = UnitDetailsPage(page)
    date_picker = DatePicker(page)
    
    # Test steps
    home_page.navigate_to_home("https://www.shurgard.com/en-be")
    page.wait_for_selector("#onetrust-accept-btn-handler", timeout=20000)
    page.click("#onetrust-accept-btn-handler")
    home_page.search_location(location)
    assert unit_details_page.select_unit(unit_type), f"Unit '{unit_type}' not found in '{location}'!"
    
    unit_details_page.fill_reservation_form(
        firstname="John",
        lastname="Doe",
        email="john.doe@example.com",
        phone="+1234567890"
    )
    date_picker.select_date("28")
    # confirmation_message = unit_details_page.submit_reservation()
    # assert "successfully reserved" in confirmation_message.lower(), "Reservation failed!"