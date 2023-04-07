from scrapy.crawler import CrawlerProcess
from core.spiders.fragment_number import FragmentNumberSpider
from scrapy.utils.project import get_project_settings


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(FragmentNumberSpider)
    process.start()


if __name__ == "__main__":
    main()
