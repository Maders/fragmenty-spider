# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FragmentItem(scrapy.Item):
    id = scrapy.Field()
    number = scrapy.Field()
    minimumBid = scrapy.Field()
    minimumBidInUSD = scrapy.Field()
    auctionEndTimestamp = scrapy.Field()
    memorabilityScore = scrapy.Field()
