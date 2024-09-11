# In the python interpreter, make the following imports. REmember to activate your vitualenv, as describen in the Creating a virtual enviroment recipe:
import delorean
from decimal import Decimal

# Enter the log to parse:
log = "[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99"

# Split the log into its parts, which are divided by - (note the space before and after the dash). We ignore the SALE part as it doesn't add any relevant information:
divide_it = log.split(" - ")
timestamp_string, _, product_string, price_string = divide_it

# Patse the timestamp into a datetime object
timestamp = delorean.parse(timestamp_string.strip("[]"))

# Parse the product_id into an integer:
product_id = int(product_string.split(":")[-1])

# Parse the price into a Decimal type:
price = Decimal(price_string.split("$")[-1])

# Now you have all of the values in native PYthon format:
print("hora:", timestamp, "\nId:", product_id, "\nPrecio:", price)
