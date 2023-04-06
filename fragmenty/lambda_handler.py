import scrapy
from scrapy.crawler import CrawlerProcess
from core.spiders.fragment_number import FragmentNumberSpider


def lambda_handler(event, context):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        # other Scrapy settings
    })

    process.crawl(FragmentNumberSpider)
    process.start()  # the script will block here until the crawling is finished
