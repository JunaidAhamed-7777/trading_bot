from bot.validators import *

print(validate_symbol("btcusdt"))
print(validate_side("LONG"))
print(validate_order_type("market"))
print(validate_quantity(0.001))