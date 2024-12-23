class UnitDetailsPage:
    def __init__(self, page):
        self.page = page
        self.UNIT_LIST = '.units-list.tiled'
        self.UNIT_ITEM = '.storage-unit.tiled'
        self.UNIT_IMAGE = '.unit-image'
        self.FIRSTNAME_INPUT = 'input[name="Form.FirstName"]'
        self.LASTNAME_INPUT = 'input[name="Form.LastName"]'
        self.EMAIL_INPUT = 'input[name="Form.EmailAddress"]'
        self.PHONE_INPUT = 'input[name="Form.PhoneNumber"]'
        self.RESERVE_BUTTON = 'button[type="submit"]'
        self.CONFIRMATION_MESSAGE = '.confirmation-message'

    def select_unit(self, unit_type):
        self.page.wait_for_selector(self.UNIT_LIST)
        self.page.locator(self.UNIT_ITEM).filter(has_text=unit_type).locator(self.UNIT_IMAGE).first.click()
        return True

    def fill_reservation_form(self, firstname, lastname, email, phone):
        self.page.fill(self.FIRSTNAME_INPUT, firstname)
        self.page.fill(self.LASTNAME_INPUT, lastname)
        self.page.fill(self.EMAIL_INPUT, email)
        self.page.fill(self.PHONE_INPUT, phone)

    def submit_reservation(self):
        self.page.click(self.RESERVE_BUTTON)
        self.page.wait_for_selector(self.CONFIRMATION_MESSAGE)
        return self.page.inner_text(self.CONFIRMATION_MESSAGE)