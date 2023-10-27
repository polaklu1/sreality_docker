import os
from scraper.sreality.spiders.sreality_spider import SrealitySpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Scraper:
    def __init__(self):
        settings_file_path = 'scraper.sreality.settings'
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.process = CrawlerProcess(get_project_settings())
        self.spider = SrealitySpider

    def run_spider(self):
        self.process.crawl(self.spider)
        self.process.start()


if __name__ == '__main__':
    scraper = Scraper()
    scraper.run_spider()
