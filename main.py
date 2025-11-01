# main.py
#from src.settings import DB_CONFIG, SCRAPER_CONFIG
#from src.database_manager import DatabaseManager
from src.vlr_scraper import VLRScraper

def run():
    scraper = VLRScraper(headless=False)
    scraper.navigateToBasePage()

    input("Press Enter to continue...")
    scraper.close()

if __name__ == "__main__":
    run()