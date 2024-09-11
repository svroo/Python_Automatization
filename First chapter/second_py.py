import delorean
from decimal import Decimal


class PriceLog(object):
    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price

    def __repr__(self):
        return "<PriceLog ({}, {}, {})>".format(
            self.timestamp, self.product_id, self.price
        )

    @classmethod
    def parse(cls, text_log):
        """Parse from a text log with the format
        [<timestamp>] - SALE - PRODUCT: <product_id> - PRICE: $<price>
        to a PriceLog object

        Args:
            text_log (_type_): _description_
        """

        divide_id = text_log.split(" - ")
        tmp_string, _, product_string, price_string = divide_id
        timestamp = delorean.parse(tmp_string.strip("[]"))
        product_id = int(product_string.split(":")[-1])
        price = Decimal(price_string.split("$")[-1])
        return cls(timestamp=timestamp, product_id=product_id, price=price)


# So, the parsing can be done as follows:
log = "[2018-05-05T12:58:59.998903] - SALE - PRODUCT: 897 - PRICE: $17.99"

print(PriceLog.parse(log))
