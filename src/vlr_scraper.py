from playwright.sync_api import Playwright, sync_playwright

from src import settings


class VLRScraper:
    config = settings.SCRAPER_CONFIG
    webPage = config["base_url"]
    delay = config["rate_limit_delay"]

    def __init__(self, headless=False):
        print("Initializing VLR scraper")
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.page = self.browser.new_page()
        print("Browser is running")

    def navigate_to_base_page(self):
        print("Navigating to base page")
        self.page.goto(self.webPage)
        print("Current page is %s", self.page.title())

    def close(self):
        print("Closing VLR scraper")
        self.browser.close()
        self.playwright.stop()
        print("VLR scraper closed")