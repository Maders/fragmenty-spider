import scrapy


class FragmentNumberSpider(scrapy.Spider):
    name = "fragment-number"
    allowed_domains = ["fragment.com"]
    start_urls = ["http://fragment.com/"]

    def parse(self, response):
        pass
