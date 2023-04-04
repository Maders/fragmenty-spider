import scrapy
import re


def extract_id(row):
    raw_number = row.css("td .table-cell-value.tm-value::text").get().strip()
    return ''.join(re.findall(r'\d', raw_number))


def extract_number(row):
    return row.css('div.tm-value::text').get()


def extract_minimum_bid(row):
    raw_minimum_bid = row.css(
        "td.thin-last-col .table-cell-value::text").re_first(r'([\d,]+)')
    return int(raw_minimum_bid.replace(',', ''))


def extract_minimum_bid_in_usd(row):
    raw_minimum_bid_in_usd = row.css(
        "td.thin-last-col .table-cell-desc.wide-only::text").re_first(r'\$([\d,]+)')
    return int(raw_minimum_bid_in_usd.replace(',', ''))


def memorability_score(number):
    # Ignore the first three characters (the three 8s)
    number = number[3:]

    # Define weights for each pattern type
    repeated_patterns_weight = 2
    sequence_patterns_weight = 1
    alternating_patterns_weight = 2
    palindrome_patterns_weight = 1
    repeated_8s_weight = 1

    total_weight = max(repeated_patterns_weight, sequence_patterns_weight,
                       alternating_patterns_weight, palindrome_patterns_weight, repeated_8s_weight)

    # Check for repeated patterns (e.g., 1111, 2222, 3333)
    repeated_patterns = sum(len(match)
                            for match in re.findall(r'(\d)\1{2,}', number))

    # Check for sequence patterns (e.g., 1234, 2345, 3456)
    sequence_patterns = 0
    for i in range(len(number) - 3):
        if number[i:i+4] in '0123456789012' or number[i:i+4] in '9876543210987':
            sequence_patterns += 1  # len(number[i:i+4])

    # Check for alternating patterns (e.g., 1212, 2323, 3434)
    alternating_patterns = sum(len(match)
                               for match in re.findall(r'(\d\d)\1{1,}', number))

    # Check for palindromes (e.g., 12321, 3443)
    palindrome_patterns = sum(1 for i in range(len(number) // 2)
                              if number[i] == number[-(i + 1)])

    # Check for repeated 8s after the first three characters
    repeated_8s = sum(len(match) for match in re.findall(r'(8)\1{2,}', number))

    total_patterns_score = (repeated_patterns * repeated_patterns_weight +
                            sequence_patterns * sequence_patterns_weight +
                            alternating_patterns * alternating_patterns_weight +
                            palindrome_patterns * palindrome_patterns_weight +
                            repeated_8s * repeated_8s_weight)

    # Normalize the score to a range of 0 to 1
    score = total_patterns_score / (len(number) * total_weight)

    return min(score, 1)


class MyprojectItem(scrapy.Item):
    id = scrapy.Field()
    number = scrapy.Field()
    minimumBid = scrapy.Field()
    minimumBidInUSD = scrapy.Field()
    auctionEndTimestamp = scrapy.Field()
    memorabilityScore = scrapy.Field()


class FragmentNumberSpider(scrapy.Spider):
    name = "fragment-number"
    allowed_domains = ["fragment.com"]
    start_urls = ["https://fragment.com/numbers"]

    def parse(self, response):
        for row in response.css('tbody.tm-high-cells tr.tm-row-selectable'):
            item = MyprojectItem()
            auctionEndTimestamp = row.css(
                'time[datetime]::attr(datetime)').get()

            item['id'] = extract_id(row)
            item['number'] = extract_number(row)
            item['minimumBid'] = extract_minimum_bid(row)
            item['minimumBidInUSD'] = extract_minimum_bid_in_usd(row)
            item['auctionEndTimestamp'] = auctionEndTimestamp
            item['memorabilityScore'] = memorability_score(extract_id(row))
            yield item
