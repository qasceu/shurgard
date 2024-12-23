class DatePicker:
    def __init__(self, page):
        self.page = page
        self.DATE_INPUT = '#reservation-datepicker'
        self.DATE_DAY = '.flatpickr-day'
        
    def select_date(self, date):
        self.page.locator(self.DATE_INPUT).click()
        self.page.locator(self.DATE_DAY).filter(has_text=date).click()