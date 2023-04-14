import re


def id(row):
    raw_number = row.css("td .table-cell-value.tm-value::text").get().strip()
    return ''.join(re.findall(r'\d', raw_number))


def number(row):
    return row.css('div.tm-value::text').get()


def minimum_bid(row):
    raw_minimum_bid = row.css(
        "td.thin-last-col .table-cell-value::text").re_first(r'([\d,]+)')
    return int(raw_minimum_bid.replace(',', ''))


def minimum_bid_in_usd(row):
    raw_minimum_bid_in_usd = row.css(
        "td.thin-last-col .table-cell-desc.wide-only::text").re_first(r'\$([\d,]+)')
    return int(raw_minimum_bid_in_usd.replace(',', ''))
