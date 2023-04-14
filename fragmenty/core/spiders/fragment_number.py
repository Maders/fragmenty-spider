import scrapy
from core.algorithm import memorability_score
from core.items import FragmentItem
from core.extractors import id, number, minimum_bid, minimum_bid_in_usd


class FragmentNumberSpider(scrapy.Spider):
    name = "fragment-number"
    allowed_domains = ["fragment.com"]
    start_urls = ["https://fragment.com/numbers"]

    def parse(self, response):
        for row in response.css('tbody.tm-high-cells tr.tm-row-selectable'):
            item = FragmentItem()
            auctionEndTimestamp = row.css(
                'time[datetime]::attr(datetime)').get()

            item['id'] = id(row)
            item['number'] = number(row)
            item['minimumBid'] = minimum_bid(row)
            item['minimumBidInUSD'] = minimum_bid_in_usd(row)
            item['auctionEndTimestamp'] = auctionEndTimestamp
            item['memorabilityScore'] = memorability_score(id(row))
            yield item
