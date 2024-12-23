class HomePage:
    def __init__(self, page):
        self.page = page
        self.SEARCH_INPUT = 'input[name="searchLocation"]'
        self.SEARCH_BUTTON = 'button[type="submit"]'
    
    def navigate_to_home(self, url):
        self.page.goto(url)
    
    def search_location(self, location):
        self.page.fill(self.SEARCH_INPUT, location)
        self.page.click(self.SEARCH_BUTTON)