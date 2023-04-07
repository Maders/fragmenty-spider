from scrapy.crawler import CrawlerProcess
from core.spiders.fragment_number import FragmentNumberSpider
from scrapy.utils.project import get_project_settings


def handler(event, context):
    process = CrawlerProcess(get_project_settings())

    process.crawl(FragmentNumberSpider)
    process.start()  # the script will block here until the crawling is finished
    return {
        'status': 'done'
    }
